"""
Expected Panel Agent
Shows initial assumptions and expectations (to contrast with reality)

Autonomy Level: 60%
- Decides which expectations to emphasize
- Controls visual hierarchy
- Chooses metric formatting
"""

from typing import Dict, Any
from PIL import Image, ImageDraw
from agents.panel_agent_base import PanelAgentBase, PanelAgentMessage


class ExpectedPanelAgent(PanelAgentBase):
    """
    Autonomous agent for Expected panel.

    Signature Style:
    - Expected grey accent (muted, assumptions)
    - Clean typography
    - Understated (expectations often wrong)
    - Lists and bullet points
    """

    def __init__(self):
        super().__init__(agent_id="expected_panel_agent")

    def negotiate(self, available_data: Dict[str, Any]) -> PanelAgentMessage:
        """
        Phase 1: Declare data needs.

        Expected panel wants:
        - expectations.timeline (primary)
        - expectations.cost (secondary)
        - expectations.features (list)
        """
        return PanelAgentMessage(
            agent_id=self.agent_id,
            phase="negotiation",
            panel_position=(0, 2),  # Column 0, Row 2 (left of bottom row)
            data_requested=[
                "expectations.timeline",
                "expectations.cost",
                "expectations.features"
            ],
            visual_weight=0.4,  # MEDIUM-LOW (expectations are just the setup)
            color_emphasis="expected_grey",
            animation_intent="fade_in"
        )

    def render(self, assigned_data: Dict[str, Any]) -> Image.Image:
        """
        Phase 2: Create Expected panel (300x400px).

        Layout Strategy:
        1. Title at top (24px from top, 8px grid)
        2. Timeline (expected grey) - PRIMARY
        3. Cost below timeline (if different from €0)
        4. Features (bullets) - what was planned
        5. Subtle "before the storm" vibe

        Adaptive Decisions:
        - If timeline similar to reality → dim it (not interesting)
        - If features > 4 → prioritize core features
        - If cost is 0 → hide it (not informative)
        """
        # Create canvas
        canvas, draw = self.create_panel_canvas(
            bg_color=self.design_system.colors['deep_space']
        )

        # Extract data
        expectations = assigned_data.get('expectations', {})
        timeline = expectations.get('timeline', '')
        cost = expectations.get('cost')
        features = expectations.get('features', [])

        # === TITLE (grid-aligned) ===
        title_y = self.align_to_grid(24)  # 24 = 3*8px
        self.draw_text(
            draw, "ERWARTET", (150, title_y),  # Center of 300px panel
            font_key='small_bold',
            color='expected_grey',
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
                color='expected_grey'
            )

        # === COST (if present and non-zero) ===
        if cost is not None and cost > 0:
            cost_y = self.align_to_grid(144)  # 144 = 18*8px
            self.draw_text(
                draw, f"€{cost}",
                (150, cost_y),
                font_key='large',
                color='cosmic_white',
                align='center'
            )

        # === FEATURES (adaptive list) ===
        if features:
            features_y = self.align_to_grid(208)  # 208 = 26*8px

            # Calculate how many features fit
            available_height = 400 - features_y - self.align_to_grid(32)  # 32px margin bottom
            line_height = self.design_system.line_height  # 24px
            max_items = min(len(features), int(available_height / line_height))

            # AUTONOMY: Agent decides which features to show
            selected_features = self._select_core_features(features, max_items)

            for i, feature in enumerate(selected_features):
                item_y = features_y + (i * line_height)

                # Truncate intelligently
                if len(feature) > 32:
                    feature = feature[:29] + "..."

                self.draw_text(
                    draw, f"• {feature}",
                    (16, item_y),
                    font_key='tiny',
                    color='cosmic_white',
                    align='left'
                )

        return canvas

    def _select_core_features(self, features: list, max_count: int) -> list:
        """
        AUTONOMY ZONE: Agent decides which expected features to prioritize.

        Strategy:
        1. Core/fundamental features rank higher
        2. Simple features > complex (expectations usually simple)
        3. Technical features > UI polish (what was actually planned)

        For now: simple truncation (Phase 1)
        Future: Smart ranking based on feature type
        """
        # Phase 1: Simple truncation
        # Phase 2+: Analyze feature complexity, prioritize core functionality
        return features[:max_count]


# === Example Usage ===
if __name__ == "__main__":
    # Test the Expected Panel Agent
    agent = ExpectedPanelAgent()

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
    panel.save(output_dir / 'expected_panel_arkify.png')
    print(f"✅ Expected panel saved to: {output_dir / 'expected_panel_arkify.png'}")
