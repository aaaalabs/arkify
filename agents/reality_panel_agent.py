"""
Reality Panel Agent
Shows actual project outcomes (contrast with expected)

Autonomy Level: 70%
- Decides which surprises to highlight
- Controls bar visualization
- Chooses text emphasis
"""

from typing import Dict, Any
from PIL import Image, ImageDraw
from agents.panel_agent_base import PanelAgentBase, PanelAgentMessage


class RealityPanelAgent(PanelAgentBase):
    """
    Autonomous agent for Reality panel.

    Signature Style:
    - Electric green accent
    - Bold typography
    - Visual punch (bar element)
    - "Mic drop moment" placement
    """

    def __init__(self):
        super().__init__(agent_id="reality_panel_agent")

    def negotiate(self, available_data: Dict[str, Any]) -> PanelAgentMessage:
        """
        Phase 1: Declare data needs.

        Reality panel wants:
        - reality.timeline (primary)
        - reality.cost (secondary)
        - reality.surprises (key insights)
        - reality.challenges (context)
        """
        return PanelAgentMessage(
            agent_id=self.agent_id,
            phase="negotiation",
            panel_position=(1, 2),  # Column 1, Row 2 (center of bottom row)
            data_requested=[
                "reality.timeline",
                "reality.cost",
                "reality.surprises",
                "reality.challenges"
            ],
            visual_weight=0.6,  # HIGH (this is the payoff panel)
            color_emphasis="electric_green",
            animation_intent="bar_slide"
        )

    def render(self, assigned_data: Dict[str, Any]) -> Image.Image:
        """
        Phase 2: Create Reality panel (300x400px).

        Layout Strategy:
        1. Title at top (24px from top, 8px grid)
        2. Timeline (bold, electric green) - PRIMARY
        3. Cost below timeline
        4. Surprises (bullets) - mid panel
        5. Visual bar at bottom - SIGNATURE ELEMENT

        Adaptive Decisions:
        - If timeline_note exists → show it subtly
        - If surprises > 3 → prioritize most impactful
        - If cost same as expected → dim it (not interesting)
        """
        # Create canvas
        canvas, draw = self.create_panel_canvas(
            bg_color=self.design_system.colors['deep_space']
        )

        # Extract data
        reality = assigned_data.get('reality', {})
        timeline = reality.get('timeline', '')
        cost = reality.get('cost', 0)
        surprises = reality.get('surprises', [])
        timeline_note = reality.get('timeline_note', '')

        # === TITLE (grid-aligned) ===
        title_y = self.align_to_grid(24)  # 24 = 3*8px
        self.draw_text(
            draw, "REALITÄT", (150, title_y),  # Center of 300px panel
            font_key='small_bold',
            color='electric_green',
            align='center'
        )

        # === TIMELINE (primary element) ===
        if timeline:
            timeline_y = self.align_to_grid(72)  # 72 = 9*8px
            timeline_height = self.draw_wrapped_text(
                draw, timeline,
                x=16,  # 2 grid units margin
                y=timeline_y,
                max_width=268,  # 300 - 32 (margins)
                font_key='medium',
                color='electric_green'
            )

            # Mic drop moment (if exists)
            if timeline_note:
                note_y = timeline_y + timeline_height + self.align_to_grid(8)
                self.draw_text(
                    draw, f"({timeline_note})",
                    (150, note_y),
                    font_key='tiny',
                    color='text_dim',
                    align='center'
                )

        # === COST ===
        cost_y = self.align_to_grid(144)  # 144 = 18*8px
        self.draw_text(
            draw, f"€{cost}",
            (150, cost_y),
            font_key='large',
            color='cosmic_white',
            align='center'
        )

        # === SURPRISES (adaptive list) ===
        if surprises:
            surp_y = self.align_to_grid(208)  # 208 = 26*8px

            # Calculate how many surprises fit before bar
            bar_y = 400 - self.align_to_grid(64)  # 64px from bottom
            available_height = bar_y - surp_y
            line_height = self.design_system.line_height  # 24px
            max_items = min(len(surprises), int(available_height / line_height))

            # AUTONOMY: Agent decides which surprises to show
            selected_surprises = self._select_top_surprises(surprises, max_items)

            for i, surprise in enumerate(selected_surprises):
                item_y = surp_y + (i * line_height)

                # Truncate intelligently
                if len(surprise) > 32:
                    surprise = surprise[:29] + "..."

                self.draw_text(
                    draw, f"• {surprise}",
                    (16, item_y),
                    font_key='tiny',
                    color='cosmic_white',
                    align='left'
                )

        # === VISUAL BAR (signature element) ===
        bar_y = 400 - self.align_to_grid(64)  # 64px from bottom
        bar_width = self.align_to_grid(176)  # 176 = 22*8px
        bar_x = (300 - bar_width) // 2  # Centered
        bar_height = self.align_to_grid(16)  # 16 = 2*8px

        draw.rectangle(
            [bar_x, bar_y, bar_x + bar_width, bar_y + bar_height],
            fill=self.design_system.colors['electric_green']
        )

        return canvas

    def _select_top_surprises(self, surprises: list, max_count: int) -> list:
        """
        AUTONOMY ZONE: Agent decides which surprises to prioritize.

        Strategy:
        1. Surprises with numbers (quantifiable) rank higher
        2. Contrarian statements ("AI struggled" vs "AI helped") rank higher
        3. Specific > Generic

        For now: simple truncation (Phase 1)
        Future: NLP-based ranking
        """
        # Phase 1: Simple truncation
        # Phase 2+: Analyze for impact/surprise level
        return surprises[:max_count]


# === Example Usage ===
if __name__ == "__main__":
    # Test the Reality Panel Agent
    agent = RealityPanelAgent()

    # Simulate negotiation
    available_data = {
        "reality": {
            "timeline": "5 days + 2 debug days",
            "timeline_note": "worth it!",
            "cost": 37,
            "surprises": [
                "AI struggled with edge cases",
                "Styling took 3x longer than coding",
                "Row Level Security was harder than expected"
            ],
            "challenges": ["Supabase RLS", "CSS responsiveness"]
        }
    }

    # Negotiation phase
    message = agent.negotiate(available_data)
    print(f"Agent: {message.agent_id}")
    print(f"Visual Weight: {message.visual_weight}")
    print(f"Data Requested: {message.data_requested}")

    # Render phase
    panel = agent.render(available_data)
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
    panel.save(output_dir / 'reality_panel_test.png')
    print(f"Test panel saved to: {output_dir / 'reality_panel_test.png'}")
