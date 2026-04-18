"""
Tech Stack Panel Agent
Shows technology stack with brand icons

Autonomy Level: 40%
- Decides icon layout (grid vs row)
- Controls icon size based on count
- Chooses grouping strategy (frontend/backend/infra)
"""

from typing import Dict, Any, List
from PIL import Image, ImageDraw
from agents.panel_agent_base import PanelAgentBase, PanelAgentMessage
from agents.icon_fetcher import IconFetcher


class TechStackPanelAgent(PanelAgentBase):
    """
    Autonomous agent for Tech Stack panel.

    Signature Style:
    - Brand icons (real logos from SimpleIcons)
    - Clean grid layout
    - Labels below icons
    - Compact and visual
    """

    def __init__(self):
        super().__init__(agent_id="tech_stack_panel_agent")
        self.icon_fetcher = IconFetcher()

    def negotiate(self, available_data: Dict[str, Any]) -> PanelAgentMessage:
        """
        Phase 1: Declare data needs.

        Tech Stack panel wants:
        - tech_stack (list of technologies)
        """
        return PanelAgentMessage(
            agent_id=self.agent_id,
            phase="negotiation",
            panel_position=(0, 1),  # Column 0, Row 1 (left of middle row)
            data_requested=[
                "tech_stack"
            ],
            visual_weight=0.3,  # LOW (supporting detail, not the story)
            color_emphasis="cosmic_white",
            animation_intent="icon_pop"
        )

    def render(self, assigned_data: Dict[str, Any]) -> Image.Image:
        """
        Phase 2: Create Tech Stack panel (300x400px).

        Layout Strategy:
        1. Title at top (24px from top, 8px grid)
        2. Icons in grid layout (2x2, 2x3, or 3x3 depending on count)
        3. Labels below each icon
        4. Adaptive icon size (more icons = smaller size)

        Adaptive Decisions:
        - 2-4 icons → 2x2 grid, 64px icons
        - 5-6 icons → 2x3 grid, 56px icons
        - 7-9 icons → 3x3 grid, 48px icons
        - Center align the grid
        """
        # Create canvas
        canvas, draw = self.create_panel_canvas(
            bg_color=self.design_system.colors['deep_space']
        )

        # Extract data
        tech_stack = assigned_data.get('tech_stack', [])

        # === TITLE (grid-aligned) ===
        title_y = self.align_to_grid(24)  # 24 = 3*8px
        self.draw_text(
            draw, "TECH STACK", (150, title_y),  # Center of 300px panel
            font_key='small_bold',
            color='cosmic_white',
            align='center'
        )

        # === ICONS GRID ===
        if tech_stack:
            # AUTONOMY: Decide layout based on icon count
            layout = self._decide_layout(len(tech_stack))
            icon_size = layout['icon_size']
            cols = layout['cols']

            # Calculate grid positioning
            grid_start_y = self.align_to_grid(88)  # 88 = 11*8px
            cell_height = icon_size + 40  # Icon + label space

            for i, tech in enumerate(tech_stack):
                row = i // cols
                col = i % cols

                # Calculate cell center position
                cell_width = 300 // cols
                x = col * cell_width + cell_width // 2
                y = grid_start_y + (row * cell_height)

                # Fetch and render icon
                try:
                    icon_img = self.icon_fetcher.fetch_icon(tech, size=icon_size)

                    # Center the icon in cell
                    icon_x = x - icon_size // 2
                    icon_y = y

                    canvas.paste(icon_img, (icon_x, icon_y), icon_img if icon_img.mode == 'RGBA' else None)

                    # Label below icon
                    label_y = y + icon_size + 8
                    self.draw_text(
                        draw, tech,
                        (x, label_y),
                        font_key='tiny',
                        color='text_dim',
                        align='center'
                    )
                except Exception as e:
                    # Fallback: Just show label if icon fetch fails
                    self.draw_text(
                        draw, tech,
                        (x, y),
                        font_key='tiny',
                        color='cosmic_white',
                        align='center'
                    )

        return canvas

    def _decide_layout(self, icon_count: int) -> Dict[str, Any]:
        """
        AUTONOMY ZONE: Decide grid layout based on icon count.

        Strategy:
        - Prefer 2-column layouts (cleaner)
        - Use 3-column only when needed
        - Larger icons for fewer items (more visual impact)
        """
        if icon_count <= 4:
            return {'cols': 2, 'icon_size': 64}
        elif icon_count <= 6:
            return {'cols': 2, 'icon_size': 56}
        else:
            return {'cols': 3, 'icon_size': 48}


# === Example Usage ===
if __name__ == "__main__":
    # Test the Tech Stack Panel Agent
    agent = TechStackPanelAgent()

    # Simulate with real Arkify data
    import yaml
    with open('examples/arkify-phase1-real.yaml', 'r') as f:
        data = yaml.safe_load(f)

    project_data = data['project']

    # Negotiation phase
    message = agent.negotiate(project_data)
    print(f"Agent: {message.agent_id}")
    print(f"Visual Weight: {message.visual_weight}")
    print(f"Data Requested: {message.data_requested}")

    # Render phase
    panel = agent.render(project_data)
    print(f"Panel Size: {panel.size}")

    # Validation
    validation = agent.validate(panel)
    print(f"Validation Passed: {validation.passed}")
    if validation.violations:
        print(f"Violations: {validation.violations}")

    # Save test output
    from pathlib import Path
    output_dir = Path('output/test_agents')
    output_dir.mkdir(parents=True, exist_ok=True)
    panel.save(output_dir / 'tech_stack_panel_arkify.png')
    print(f"✅ Tech Stack panel saved to: {output_dir / 'tech_stack_panel_arkify.png'}")
