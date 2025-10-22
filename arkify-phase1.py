#!/usr/bin/env python3
"""
Arkify - Project Breakdown Generator
Phase 1: Enhanced Story with 3x3 Grid

Generate beautiful 3x3 project breakdowns with Future Dust palette.

Usage:
    python arkify-phase1.py examples/indie-saas-phase1.yaml

Output:
    output/project-name-phase1.png (900x1200px)
"""

import sys
import yaml
from pathlib import Path

from agents.orchestrator_phase1 import OrchestratorPhase1


def main():
    """Main entry point for Arkify Phase 1 CLI."""

    # Parse command line arguments
    if len(sys.argv) < 2:
        print("Usage: python arkify-phase1.py <input.yaml>")
        print("\nExamples:")
        print("  python arkify-phase1.py examples/indie-saas-phase1.yaml")
        print("  python arkify-phase1.py examples/ai-todo-app.yaml")
        print("\nPhase 1 Features:")
        print("  - 3x3 grid layout (900x1200px)")
        print("  - Future Dust color palette (2025 Color of the Year)")
        print("  - Story arc optimization")
        print("  - Expected vs Reality comparison")
        sys.exit(1)

    input_file = Path(sys.argv[1])

    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)

    # Load project data
    print(f"📖 Loading project data from {input_file}...")
    try:
        with open(input_file, 'r') as f:
            project_data = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading YAML: {e}")
        sys.exit(1)

    # Validate minimal required fields (Phase 0 compatibility)
    required_fields = ['name', 'learning']
    project = project_data.get('project', {})

    missing_fields = [f for f in required_fields if f not in project]
    if missing_fields:
        print(f"❌ Missing required fields: {', '.join(missing_fields)}")
        print("\nMinimal required fields:")
        print("  - name: Project name")
        print("  - learning: Key lesson learned")
        print("\nOptional Phase 1 fields:")
        print("  - tagline: One-line description")
        print("  - results: {users, revenue, signups}")
        print("  - expectations: {timeline, cost}")
        print("  - reality: {timeline, cost, challenges}")
        sys.exit(1)

    # Initialize Phase 1 orchestrator
    print("🎬 Initializing Arkify Phase 1 orchestrator...")
    print("   Using Future Dust palette (WGSN 2025 Color of the Year)")
    orchestrator = OrchestratorPhase1()

    # Generate breakdown
    print("✨ Generating Phase 1 project breakdown...")
    try:
        output_path = orchestrator.generate(project_data)
        print(f"✅ Success! Generated: {output_path}")
        print(f"\n📏 Size: 900x1200px (LinkedIn 4:5 ratio)")
        print(f"🎨 Palette: Future Dust")
        print(f"📱 Share it on LinkedIn for maximum engagement!")
    except Exception as e:
        print(f"❌ Generation failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
