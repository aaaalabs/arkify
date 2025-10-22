"""
Checkpoint Manager

Manages human validation checkpoints during phase execution.
Creates validation packages and waits for human approval.
"""

from typing import Dict, Any, List
from pathlib import Path
from datetime import datetime
import json


class CheckpointManager:
    """
    Manages human-in-the-loop validation checkpoints.

    Creates comprehensive validation packages for human review,
    waits for approval, and collects feedback.
    """

    def __init__(self):
        self.checkpoint_dir = Path('checkpoints')
        self.checkpoint_dir.mkdir(exist_ok=True)
        self.checkpoints: List[Dict[str, Any]] = []

    def create_checkpoint(self, phase: int, results: Dict[str, Any],
                         qa_report: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create validation checkpoint for human review.

        Args:
            phase: Phase number
            results: Implementation results
            qa_report: QA report

        Returns:
            Checkpoint metadata
        """
        checkpoint_id = f"phase-{phase}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        checkpoint_path = self.checkpoint_dir / checkpoint_id
        checkpoint_path.mkdir(exist_ok=True)

        # Generate validation package
        package = self._generate_validation_package(phase, results, qa_report)

        # Save checkpoint
        checkpoint = {
            'id': checkpoint_id,
            'phase': phase,
            'timestamp': datetime.now().isoformat(),
            'package': package,
            'path': str(checkpoint_path),
            'status': 'PENDING'
        }

        # Write checkpoint data
        with open(checkpoint_path / 'checkpoint.json', 'w') as f:
            json.dump(checkpoint, f, indent=2)

        # Write human-readable summary
        self._write_summary(checkpoint_path, phase, package)

        self.checkpoints.append(checkpoint)

        print(f"\n  📦 Validation package created: {checkpoint_path}/")
        print(f"  📋 Review summary: {checkpoint_path}/VALIDATION.md")

        return checkpoint

    def _generate_validation_package(self, phase: int, results: Dict[str, Any],
                                    qa_report: Dict[str, Any]) -> Dict[str, Any]:
        """Generate validation package contents."""
        return {
            'phase_name': f"Phase {phase}",
            'what_changed': self._extract_changes(results),
            'validation_criteria': self._extract_criteria(phase),
            'qa_summary': qa_report,
            'test_examples': self._list_test_outputs(),
            'questions': self._generate_questions(phase, results)
        }

    def _extract_changes(self, results: Dict[str, Any]) -> List[str]:
        """Extract what changed in this phase."""
        changes = []

        if 'code' in results:
            code_changes = results['code']
            if 'new_files' in code_changes:
                for file in code_changes['new_files']:
                    changes.append(f"Added: {file}")
            if 'modified_files' in code_changes:
                for file in code_changes['modified_files']:
                    changes.append(f"Modified: {file}")

        return changes if changes else ["No specific changes documented"]

    def _extract_criteria(self, phase: int) -> List[str]:
        """Get validation criteria for this phase."""
        criteria_map = {
            1: [
                "3x3 grid is visually balanced",
                "Story arc flows logically (Problem → Solution → Reality)",
                "Charts are readable and accurate",
                "Backward compatible (Phase 0 YAMLs still work)",
                "Performance <5 seconds generation time"
            ],
            2: [
                "Architecture diagrams are portfolio-quality",
                "SVG rendering works correctly",
                "Color themes are professional",
                "Diagram complexity is manageable",
                "Performance <60 seconds with diagrams"
            ]
        }
        return criteria_map.get(phase, ["Review code quality", "Test functionality"])

    def _list_test_outputs(self) -> List[str]:
        """List generated test outputs for review."""
        output_dir = Path('output')
        if not output_dir.exists():
            return []

        outputs = []
        for file in output_dir.glob('*.png'):
            outputs.append(str(file))

        return outputs[:10]  # Limit to 10 most recent

    def _generate_questions(self, phase: int, results: Dict[str, Any]) -> List[str]:
        """Generate specific questions for human."""
        questions_map = {
            1: [
                "Does the 3x3 layout feel too crowded or just right?",
                "Are the chart colors professional enough?",
                "Should we add more template variations now or wait for Phase 2?",
                "Is the story arc flow intuitive?"
            ],
            2: [
                "Are the architecture diagrams clear and helpful?",
                "Do the color themes work well together?",
                "Should we add more diagram types?",
                "Is SVG quality high enough for presentations?"
            ]
        }
        return questions_map.get(phase, ["Does everything work as expected?"])

    def _write_summary(self, checkpoint_path: Path, phase: int, package: Dict[str, Any]):
        """Write human-readable validation summary."""
        summary = f"""# Phase {phase} Validation Checkpoint

## What's New

{chr(10).join(f'- {change}' for change in package['what_changed'])}

## Validation Criteria

{chr(10).join(f'- [ ] {criterion}' for criterion in package['validation_criteria'])}

## Test Examples Generated

{chr(10).join(f'- `{example}`' for example in package['test_examples'])}

## Questions for Review

{chr(10).join(f'{i+1}. {q}' for i, q in enumerate(package['questions']))}

## QA Summary

```json
{json.dumps(package['qa_summary'], indent=2)}
```

## Approval

To approve this phase:
1. Review all test examples
2. Verify validation criteria
3. Answer questions above
4. Update `checkpoint.json` with your decision

```json
{{
  "approved": true,
  "comments": "Your feedback here",
  "requested_changes": []
}}
```

---
*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

        with open(checkpoint_path / 'VALIDATION.md', 'w') as f:
            f.write(summary)

    def wait_for_approval(self) -> Dict[str, Any]:
        """
        Wait for human approval (interactive).

        Returns:
            Approval result with feedback
        """
        print("\n" + "="*70)
        print("  🛑 HUMAN VALIDATION REQUIRED")
        print("="*70 + "\n")

        print("Please review the validation package:")
        latest_checkpoint = self.checkpoints[-1]
        print(f"  Location: {latest_checkpoint['path']}/")
        print(f"  Summary:  {latest_checkpoint['path']}/VALIDATION.md\n")

        print("Validation criteria:")
        for criterion in latest_checkpoint['package']['validation_criteria']:
            print(f"  [ ] {criterion}")

        print("\nTest examples:")
        for example in latest_checkpoint['package']['test_examples'][:5]:
            print(f"  - {example}")

        print("\n" + "-"*70)

        # Interactive approval
        while True:
            response = input("\nApprove this phase? (yes/no/defer): ").strip().lower()

            if response == 'yes':
                comments = input("Comments (optional): ").strip()
                return {
                    'approved': True,
                    'comments': comments,
                    'timestamp': datetime.now().isoformat()
                }

            elif response == 'no':
                feedback = input("What needs to change? ").strip()
                requested_changes = input("Specific changes (comma-separated): ").strip().split(',')
                return {
                    'approved': False,
                    'feedback': feedback,
                    'requested_changes': [c.strip() for c in requested_changes],
                    'timestamp': datetime.now().isoformat()
                }

            elif response == 'defer':
                print("\n⏸️  Validation deferred. You can resume later by running:")
                print(f"     python meta_runner.py --resume {latest_checkpoint['id']}")
                exit(0)

            else:
                print("Invalid response. Please enter 'yes', 'no', or 'defer'.")

    def get_checkpoint_status(self, checkpoint_id: str) -> Dict[str, Any]:
        """Get status of a checkpoint."""
        for checkpoint in self.checkpoints:
            if checkpoint['id'] == checkpoint_id:
                return checkpoint
        return {'status': 'NOT_FOUND'}
