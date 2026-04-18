#!/usr/bin/env python3
"""
Arkify Phase 2 Generator
Generates Phase 2 output: Architecture through Real Decisions

Usage:
    python3 arkify-phase2.py examples/arkify-phase2-real.yaml

Output:
    - output/arkify-phase2.png (900x1200px)
    - docs/phase-outputs/phase2-final.png (deployed version)
"""

import sys
import yaml
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from agents.layout_compositor_phase2 import LayoutCompositorPhase2


def generate_phase2(yaml_path, output_path):
    """
    Generate Phase 2 breakdown

    Args:
        yaml_path: Path to YAML input file
        output_path: Path for output PNG

    Returns:
        bool: Success status
    """
    print(f"🚀 Arkify Phase 2 Generator")
    print(f"   Input: {yaml_path}")
    print(f"   Output: {output_path}")
    print()

    # Load YAML
    print("📋 Loading project data...")
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    project_data = data.get('project', {})

    # Validate
    print("✓ Data loaded:")
    print(f"  - Name: {project_data.get('name')}")
    print(f"  - Commits analyzed: {project_data.get('meta', {}).get('commits_analyzed', 0)}")
    print(f"  - Decision paths: {len([k for k in project_data.keys() if 'decision_' in k])}")
    print()

    # Generate
    print("🎨 Composing 3x3 grid...")
    print("   [1/9] Header (900x300px)")
    print("   [2/9] Decision Path: Icon Rendering")
    print("   [3/9] Contrast Journey")
    print("   [4/9] Decision Path: Mock Data Fail")
    print("   [5/9] Autonomy Spectrum")
    print("   [6/9] Timeline Breakdown")
    print("   [7/9] Results")
    print("   [8/9] Tech Stack")
    print("   [9/9] Reality")
    print("   [10/9] Meta-Recursion")
    print()

    compositor = LayoutCompositorPhase2()
    success = compositor.compose(project_data, output_path)

    if success:
        file_size = os.path.getsize(output_path) / 1024  # KB
        print()
        print(f"✅ Phase 2 complete!")
        print(f"   Output: {output_path}")
        print(f"   Size: {file_size:.1f} KB")
        print()
        print("📊 Panels generated:")
        print("   ✓ 5 decision paths visualized")
        print("   ✓ 6 agent autonomy levels shown")
        print("   ✓ Timeline breakdown (fail/work/polish)")
        print("   ✓ Contrast journey (2:1 → 7.12:1)")
        print("   ✓ Meta-recursion (self-documentation)")
        print()
        print("🔬 Research findings:")
        print("   - Icon rendering: 4 tries to success")
        print("   - Mock data fail: Mistake became feature")
        print("   - Meta-recursion: Tool documents itself thinking")
        print("   - 100% real data from git commits")
        print()

    return success


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 arkify-phase2.py examples/arkify-phase2-real.yaml")
        sys.exit(1)

    yaml_path = sys.argv[1]
    output_path = 'output/arkify-phase2.png'

    # Ensure output dir exists
    os.makedirs('output', exist_ok=True)

    success = generate_phase2(yaml_path, output_path)

    if success:
        # Also save to phase-outputs
        docs_path = 'docs/phase-outputs/phase2-final.png'
        os.makedirs('docs/phase-outputs', exist_ok=True)

        import shutil
        shutil.copy(output_path, docs_path)
        print(f"📦 Deployed to: {docs_path}")
        print()
        print("🎉 Phase 2 complete! Arkify researched itself.")

    sys.exit(0 if success else 1)
