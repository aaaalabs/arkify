"""
Main Orchestrator Agent

The "Project Manager of Project Managers" that coordinates all
sub-agents to build Arkify phase by phase with human validation.
"""

from typing import Dict, Any, List, Optional
from pathlib import Path
import yaml

from .base_agent import BaseAgent
from .checkpoint_manager import CheckpointManager


class MainOrchestrator(BaseAgent):
    """
    Main Orchestrator coordinates the entire meta-build process.

    Responsibilities:
    - Phase planning and sequencing
    - Sub-agent coordination
    - Human checkpoint management
    - Quality gate validation
    - Milestone breakdown generation
    """

    def __init__(self):
        super().__init__(
            name="Main Orchestrator",
            description="Coordinates all agents to build Arkify phase by phase"
        )
        self.checkpoint_manager = CheckpointManager()
        self.sub_agents: Dict[str, BaseAgent] = {}
        self.current_phase: Optional[int] = None
        self.phase_history: List[Dict[str, Any]] = []

    def register_agent(self, agent: BaseAgent):
        """
        Register a sub-agent.

        Args:
            agent: Sub-agent to register
        """
        self.sub_agents[agent.name] = agent
        print(f"  ✓ Registered: {agent.name}")

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute phase build process.

        Args:
            context: Phase number and requirements

        Returns:
            Phase execution results
        """
        phase = context.get('phase')
        self.current_phase = phase

        print(f"\n{'='*70}")
        print(f"  🎬 PHASE {phase} ORCHESTRATION START")
        print(f"{'='*70}\n")

        # Load phase requirements from ROADMAP
        phase_requirements = self._load_phase_requirements(phase)

        # Execute build pipeline
        try:
            # 1. Planning
            print("📋 Phase 1: PLANNING")
            planning_results = self._execute_planning(phase_requirements)

            # 2. Implementation
            print("\n💻 Phase 2: IMPLEMENTATION")
            implementation_results = self._execute_implementation(planning_results)

            # 3. Quality Assurance
            print("\n✅ Phase 3: QUALITY ASSURANCE")
            qa_results = self._execute_qa(implementation_results)

            # 4. Human Checkpoint
            print(f"\n{'='*70}")
            print(f"  🛑 HUMAN VALIDATION CHECKPOINT")
            print(f"{'='*70}\n")
            checkpoint_result = self.checkpoint_manager.create_checkpoint(
                phase=phase,
                results=implementation_results,
                qa_report=qa_results
            )

            # WAIT FOR HUMAN
            human_approved = self.checkpoint_manager.wait_for_approval()

            if not human_approved['approved']:
                return {
                    'status': 'REJECTED',
                    'phase': phase,
                    'feedback': human_approved['feedback'],
                    'message': 'Human validation failed. Iteration needed.'
                }

            # 5. Generate Milestone Breakdown (Meta!)
            print("\n🎨 Phase 4: GENERATE BREAKDOWN STORY")
            breakdown = self._generate_milestone_breakdown(phase, implementation_results)

            # 6. Finalize
            print("\n🚀 Phase 5: FINALIZE & DEPLOY")
            self._finalize_phase(phase)

            # Record success
            phase_record = {
                'phase': phase,
                'status': 'COMPLETED',
                'planning': planning_results,
                'implementation': implementation_results,
                'qa': qa_results,
                'checkpoint': checkpoint_result,
                'breakdown': breakdown,
                'human_feedback': human_approved.get('comments', '')
            }
            self.phase_history.append(phase_record)

            print(f"\n{'='*70}")
            print(f"  ✅ PHASE {phase} COMPLETE!")
            print(f"{'='*70}\n")
            print(f"  Breakdown story: {breakdown['output_file']}")
            print(f"  Human feedback: {human_approved.get('comments', 'None')}\n")

            return phase_record

        except Exception as e:
            print(f"\n❌ Error during Phase {phase}: {e}")
            import traceback
            traceback.print_exc()
            return {
                'status': 'FAILED',
                'phase': phase,
                'error': str(e)
            }

    def _load_phase_requirements(self, phase: int) -> Dict[str, Any]:
        """Load phase requirements from ROADMAP."""
        # For now, hardcoded. In future, parse ROADMAP.md
        phase_reqs = {
            1: {
                'name': 'Enhanced Story',
                'features': [
                    '3x3 grid layout',
                    'Story Arc Designer agent',
                    'Graph Generator agent',
                    'Multiple template variations'
                ],
                'success_criteria': [
                    'Story arc flows logically',
                    '3x3 grid is balanced',
                    'Charts are accurate',
                    'Backward compatible'
                ]
            },
            2: {
                'name': 'Visual Intelligence',
                'features': [
                    'Architecture diagrams',
                    'Proper SVG rendering',
                    'Color theme system'
                ],
                'success_criteria': [
                    'Diagrams are portfolio-quality',
                    'SVG rendering works',
                    '5+ color themes available'
                ]
            }
        }
        return phase_reqs.get(phase, {})

    def _execute_planning(self, requirements: Dict[str, Any]) -> Dict[str, Any]:
        """Execute planning phase with planning agents."""
        results = {}

        # Architecture planning
        if 'Architecture Designer' in self.sub_agents:
            arch_agent = self.sub_agents['Architecture Designer']
            print(f"  → {arch_agent.name}...")
            results['architecture'] = arch_agent.execute({'requirements': requirements})

        # Story arc planning
        if 'Story Arc Planner' in self.sub_agents:
            story_agent = self.sub_agents['Story Arc Planner']
            print(f"  → {story_agent.name}...")
            results['story_arc'] = story_agent.execute({'requirements': requirements})

        return results

    def _execute_implementation(self, planning: Dict[str, Any]) -> Dict[str, Any]:
        """Execute implementation phase."""
        results = {}

        # Code implementation
        if 'Implementation Agent' in self.sub_agents:
            impl_agent = self.sub_agents['Implementation Agent']
            print(f"  → {impl_agent.name}...")
            results['code'] = impl_agent.execute({'plan': planning})

        # Documentation
        if 'Documentation Agent' in self.sub_agents:
            doc_agent = self.sub_agents['Documentation Agent']
            print(f"  → {doc_agent.name}...")
            results['docs'] = doc_agent.execute({'changes': results.get('code', {})})

        # Testing
        if 'Testing Agent' in self.sub_agents:
            test_agent = self.sub_agents['Testing Agent']
            print(f"  → {test_agent.name}...")
            results['tests'] = test_agent.execute({'code': results.get('code', {})})

        return results

    def _execute_qa(self, implementation: Dict[str, Any]) -> Dict[str, Any]:
        """Execute quality assurance."""
        if 'Quality Assurance Agent' not in self.sub_agents:
            return {'status': 'SKIPPED', 'reason': 'No QA agent registered'}

        qa_agent = self.sub_agents['Quality Assurance Agent']
        print(f"  → {qa_agent.name}...")
        return qa_agent.execute({'implementation': implementation})

    def _generate_milestone_breakdown(self, phase: int, results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Arkify breakdown documenting this phase (Meta!)."""
        if 'Breakdown Generator' not in self.sub_agents:
            return {'status': 'SKIPPED', 'reason': 'No breakdown generator'}

        breakdown_agent = self.sub_agents['Breakdown Generator']
        print(f"  → {breakdown_agent.name}...")
        return breakdown_agent.execute({
            'phase': phase,
            'results': results
        })

    def _finalize_phase(self, phase: int):
        """Finalize phase - git commit, tag, etc."""
        print(f"  → Finalizing Phase {phase}...")
        print(f"  → Git commit: feat: Phase {phase} complete")
        print(f"  → Git tag: v0.{phase}.0")
        # Actual git operations would go here

    def get_phase_summary(self, phase: int) -> Optional[Dict[str, Any]]:
        """Get summary of completed phase."""
        for record in self.phase_history:
            if record['phase'] == phase:
                return record
        return None

    def list_available_agents(self) -> List[str]:
        """List all registered sub-agents."""
        return list(self.sub_agents.keys())
