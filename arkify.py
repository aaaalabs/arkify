#!/usr/bin/env python3
"""
Arkify - Project Breakdown Generator
Phase 0: Ultra-Minimal MVP

Generate beautiful 2x2 project breakdown graphics from YAML input.

Usage:
    python arkify.py examples/ai-todo-app.yaml

Output:
    output/project-name.png
"""

import sys
import yaml
from pathlib import Path

from agents.orchestrator import MiniOrchestrator


def main():
    """Main entry point for Arkify CLI."""

    # Parse command line arguments
    if len(sys.argv) < 2:
        print("Usage: python arkify.py <input.yaml>")
        print("\nExamples:")
        print("  python arkify.py examples/ai-todo-app.yaml")
        print("  python arkify.py examples/saas-mvp.yaml")
        print("  python arkify.py examples/weekend-hack.yaml")
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

    # Validate minimal required fields
    required_fields = ['name', 'hours', 'cost', 'tech_stack', 'learning']
    project = project_data.get('project', {})

    missing_fields = [f for f in required_fields if f not in project]
    if missing_fields:
        print(f"❌ Missing required fields: {', '.join(missing_fields)}")
        print("\nRequired fields in project:")
        print("  - name: Project name")
        print("  - hours: Total hours spent")
        print("  - cost: Total cost in currency")
        print("  - tech_stack: List of technologies")
        print("  - learning: Key lesson learned")
        sys.exit(1)

    # Initialize orchestrator
    print("🎬 Initializing Arkify orchestrator...")
    orchestrator = MiniOrchestrator()

    # Generate breakdown
    print("✨ Generating project breakdown...")
    try:
        output_path = orchestrator.generate(project_data)
        print(f"✅ Success! Generated: {output_path}")
        print(f"\n📱 Share it on LinkedIn, Twitter, or your blog!")
    except Exception as e:
        print(f"❌ Generation failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
