"""
Generate Arkify Phase 1 output using autonomous panel agents.

Layout:
Row 0: [========== Header 900x400px ==========]
Row 1: [Tech 300x400] [Learning 300x400] [empty 300x400]
Row 2: [Expected 300x400] [Reality 300x400] [Results 300x400]

Total canvas: 900x1200px
"""

import sys
from pathlib import Path
from PIL import Image

# Add agents directory to path
sys.path.insert(0, str(Path.cwd()))

import yaml

# Import all 6 panel agents
from agents.header_panel_agent import HeaderPanelAgent
from agents.expected_panel_agent import ExpectedPanelAgent
from agents.reality_panel_agent import RealityPanelAgent
from agents.tech_stack_panel_agent import TechStackPanelAgent
from agents.learning_panel_agent import LearningPanelAgent
from agents.results_panel_agent import ResultsPanelAgent


def main():
    # Load real Arkify data
    with open('examples/arkify-phase1-real.yaml', 'r') as f:
        data = yaml.safe_load(f)

    project_data = data['project']

    print('🎨 Generating Arkify Phase 1 with 6 autonomous agents...')
    print()

    # Create canvas (900x1200px)
    canvas = Image.new('RGB', (900, 1200), '#22223B')

    # === ROW 0: HEADER (full width) ===
    print('Rendering header_panel_agent (full width)...')
    header_agent = HeaderPanelAgent(full_width=True)
    header_panel = header_agent.render(project_data)
    canvas.paste(header_panel, (0, 0))
    print(f'  ✅ Header placed at (0, 0) - size: {header_panel.size}')
    print()

    # === ROW 1: Tech Stack, Learning, (empty) ===
    panels_row1 = [
        (TechStackPanelAgent(), 0),   # Column 0
        (LearningPanelAgent(), 1),    # Column 1
        # Column 2 empty
    ]

    for agent, col in panels_row1:
        print(f'Rendering {agent.agent_id}...')
        panel = agent.render(project_data)

        x = col * 300
        y = 400  # Row 1 starts at 400px (after header)

        canvas.paste(panel, (x, y))
        print(f'  ✅ Placed at ({col}, 1) -> pixel ({x}, {y})')

    print()

    # === ROW 2: Expected, Reality, Results ===
    panels_row2 = [
        (ExpectedPanelAgent(), 0),    # Column 0
        (RealityPanelAgent(), 1),     # Column 1
        (ResultsPanelAgent(), 2),     # Column 2
    ]

    for agent, col in panels_row2:
        print(f'Rendering {agent.agent_id}...')
        panel = agent.render(project_data)

        x = col * 300
        y = 800  # Row 2 starts at 800px

        canvas.paste(panel, (x, y))
        print(f'  ✅ Placed at ({col}, 2) -> pixel ({x}, {y})')

    # Save final output
    output_path = Path('output/arkify-phase1-final.png')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path)

    print()
    print('=' * 60)
    print(f'✅ COMPLETE: {output_path}')
    print(f'   Size: {canvas.size[0]}x{canvas.size[1]}px')
    print(f'   Layout: Full-width header + 2x3 grid')
    print(f'   Agents: 6 autonomous panel agents')
    print(f'   Icons: ✅ Fixed (cairosvg rendering)')
    print(f'   Data: 100% real Arkify Phase 1 development')
    print('=' * 60)


if __name__ == "__main__":
    main()
