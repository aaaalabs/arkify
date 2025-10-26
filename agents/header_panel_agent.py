"""
Header Panel Agent
Shows project name, tagline, and branding (top-left position)

Autonomy Level: 20% (LOWEST)
- Strict branding requirements (project name MUST be huge)
- Limited layout decisions
- Enforced hierarchy (name > tagline)
- Minimal creative freedom (this is the brand anchor)
"""

from typing import Dict, Any
from PIL import Image, ImageDraw
from agents.panel_agent_base import PanelAgentBase, PanelAgentMessage


class HeaderPanelAgent(PanelAgentBase):
    """
    Autonomous agent for Header panel.

    Signature Style:
    - Project name (HUGE, 72px, electric green)
    - Tagline below (wrapped, 18-24px)
    - Clean, minimal, brand-focused
    - Top-left anchor of entire layout
    """

    def __init__(self):
        super().__init__(agent_id="header_panel_agent")

    def negotiate(self, available_data: Dict[str, Any]) -> PanelAgentMessage:
        """
        Phase 1: Declare data needs.

        Header panel wants:
        - name (project name) - REQUIRED
        - tagline (one-liner description)
        """
        return PanelAgentMessage(
            agent_id=self.agent_id,
            phase="negotiation",
            panel_position=(0, 0),  # Column 0, Row 0 (top-left, prime position)
            data_requested=[
                "name",
                "tagline"
            ],
            visual_weight=0.5,  # MEDIUM (important but not the story)
            color_emphasis="electric_green",
            animation_intent="slide_in"
        )

    def render(self, assigned_data: Dict[str, Any]) -> Image.Image:
        """
        Phase 2: Create Header panel (300x400px).

        Layout Strategy (STRICT):
        1. Project name (72px, electric green, bold) - TOP
        2. Tagline (18-24px, wrapped, cosmic white) - BELOW NAME
        3. Center-aligned vertically in panel
        4. Limited autonomy (branding must be consistent)

        Adaptive Decisions (20% AUTONOMY):
        - Tagline font size (18px if long, 24px if short)
        - Vertical positioning to balance name + tagline
        - Line breaks in tagline (minimal control)
        """
        # Create canvas
        canvas, draw = self.create_panel_canvas(
            bg_color=self.design_system.colors['deep_space']
        )

        # Extract data
        name = assigned_data.get('name', 'Untitled Project')
        tagline = assigned_data.get('tagline', '')

        # === PROJECT NAME (hero element, STRICT) ===
        # MUST be huge (72px), MUST be electric green, MUST be centered
        name_y = self.align_to_grid(120)  # 120 = 15*8px

        self.draw_text(
            draw, name,
            (150, name_y),  # Center of 300px panel
            font_key='huge',
            color='electric_green',
            align='center'
        )

        # === TAGLINE (supporting element) ===
        if tagline:
            tagline_y = name_y + 72 + self.align_to_grid(24)  # 72px (huge font) + 24px gap

            # AUTONOMY: Choose font size based on tagline length
            tagline_font = self._select_tagline_font(tagline)

            # Draw wrapped tagline
            self.draw_wrapped_text(
                draw, tagline,
                x=16,  # 2 grid units margin
                y=tagline_y,
                max_width=268,  # 300 - 32 (margins)
                font_key=tagline_font,
                color='cosmic_white'
            )

        return canvas

    def _select_tagline_font(self, tagline: str) -> str:
        """
        AUTONOMY ZONE: Choose tagline font size.

        Limited autonomy (20%):
        - Short tagline (<40 chars) → 'small' (24px)
        - Long tagline (>=40 chars) → 'tiny' (18px)

        This is the ONLY creative decision this agent makes.
        Everything else is strictly enforced by design system.
        """
        if len(tagline) < 40:
            return 'small'
        else:
            return 'tiny'


# === Example Usage ===
if __name__ == "__main__":
    # Test the Header Panel Agent
    agent = HeaderPanelAgent()

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
    panel.save(output_dir / 'header_panel_arkify.png')
    print(f"✅ Header panel saved to: {output_dir / 'header_panel_arkify.png'}")
