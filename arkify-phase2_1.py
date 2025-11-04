#!/usr/bin/env python3
"""
Arkify Phase 2.1 Generator (Canva Style)
Generates Phase 2.1 output with gradients, real icons, and story-driven layout.

Usage:
    python3 arkify-phase2_1.py examples/arkify-phase2_1-real.yaml

Output:
    - output/arkify-phase2.1.png (1200x1600px)
    - docs/phase-outputs/phase2.1-final.png (deployed version)
"""

import sys
import yaml
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from agents.layout_compositor_phase2_1 import LayoutCompositorPhase21


def generate_phase21(yaml_path, output_path):
    """
    Generate Phase 2.1 breakdown

    Args:
        yaml_path: Path to YAML input file
        output_path: Path for output PNG

    Returns:
        bool: Success status
    """
    print(f"🚀 Arkify Phase 2.1 Generator (Canva Style)")
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
    print(f"  - Tech stack: {', '.join(project_data.get('tech_stack', []))[:60]}")
    print(f"  - Commits analyzed: {project_data.get('meta', {}).get('commits_analyzed', 0)}")
    print()

    # Generate
    print("🎨 Composing 1200x1600px canvas...")
    print("   [1/7] Header: 'Your Mistakes ARE Your Research'")
    print("   [2/7] Panel 1: The Mistake (fail gradient)")
    print("   [3/7] Panel 2: The Catch (success gradient)")
    print("   [4/7] Panel 3: The Insight (insight gradient)")
    print("   [5/7] Panel 4: Tech Stack (REAL brand icons)")
    print("   [6/7] Panel 5: By Numbers (big 28)")
    print("   [7/7] Panel 6: The Meta (∞ recursion)")
    print()

    compositor = LayoutCompositorPhase21()
    success = compositor.compose(project_data, output_path)

    if success:
        file_size = os.path.getsize(output_path) / 1024  # KB
        print()
        print(f"✅ Phase 2.1 complete!")
        print(f"   Output: {output_path}")
        print(f"   Size: {file_size:.1f} KB")
        print(f"   Canvas: 1200x1600px (Instagram portrait 3:4)")
        print()
        print("🎯 Canva-Style Features:")
        print("   ✓ Smooth gradients (diagonal, horizontal)")
        print("   ✓ Real brand icons (Python, Anthropic, GitHub, PIL)")
        print("   ✓ Story arc: Mistake → Learn → Meta")
        print("   ✓ Generous whitespace (600x533px panels)")
        print("   ✓ Viral hook: 'Your Mistakes ARE Your Research'")
        print()
        print("📊 Comparison with Phase 2.0:")
        print("   Phase 2.0: 900x1200px, 9 panels @ 300x300px, flat colors")
        print("   Phase 2.1: 1200x1600px, 6 panels @ 600x533px, gradients + icons")
        print("   Space per panel: +100% 🎉")
        print()

    return success


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 arkify-phase2_1.py examples/arkify-phase2_1-real.yaml")
        sys.exit(1)

    yaml_path = sys.argv[1]
    output_path = 'output/arkify-phase2.1.png'

    # Ensure output dir exists
    os.makedirs('output', exist_ok=True)

    success = generate_phase21(yaml_path, output_path)

    if success:
        # Also save to phase-outputs
        docs_path = 'docs/phase-outputs/phase2.1-final.png'
        os.makedirs('docs/phase-outputs', exist_ok=True)

        import shutil
        shutil.copy(output_path, docs_path)
        print(f"📦 Deployed to: {docs_path}")
        print()
        print("🎉 Phase 2.1 complete! Canva-quality achieved.")
        print("   Ready for LinkedIn, Instagram, Twitter.")
        print("   Mobile-optimized portrait format.")
        print()
        print("🔥 Viral potential: Makes sharers look insightful")
        print("   Hook: 'Your Mistakes ARE Your Research'")

    sys.exit(0 if success else 1)
