"""
Learning Panel Agent
Shows key insights, lessons learned, and challenges faced

Autonomy Level: 80% (HIGHEST)
- Decides which insights to emphasize
- Controls narrative tone and pacing
- Chooses challenge vs surprise framing
- Maximum creative freedom for storytelling
"""

from typing import Dict, Any, List
from PIL import Image, ImageDraw
from agents.panel_agent_base import PanelAgentBase, PanelAgentMessage


class LearningPanelAgent(PanelAgentBase):
    """
    Autonomous agent for Learning panel.

    Signature Style:
    - Story-driven (highest narrative control)
    - Main insight (hero message)
    - Supporting challenges/surprises
    - Wisdom-focused (the "why this matters")
    """

    def __init__(self):
        super().__init__(agent_id="learning_panel_agent")

    def negotiate(self, available_data: Dict[str, Any]) -> PanelAgentMessage:
        """
        Phase 1: Declare data needs.

        Learning panel wants:
        - learning (main insight)
        - reality.challenges (what was hard)
        - reality.surprises (what was unexpected)
        """
        return PanelAgentMessage(
            agent_id=self.agent_id,
            phase="negotiation",
            panel_position=(1, 1),  # Column 1, Row 1 (center of middle row)
            data_requested=[
                "learning",
                "reality.challenges",
                "reality.surprises"
            ],
            visual_weight=0.7,  # HIGH (this is the wisdom/payoff)
            color_emphasis="cosmic_white",
            animation_intent="reveal_text"
        )

    def render(self, assigned_data: Dict[str, Any]) -> Image.Image:
        """
        Phase 2: Create Learning panel (300x400px).

        Layout Strategy:
        1. Title at top (24px from top, 8px grid)
        2. Main learning (wrapped, medium font) - THE WISDOM
        3. Challenges OR surprises (bullets) - context
        4. Adaptive content based on what's more impactful

        Adaptive Decisions (80% AUTONOMY):
        - Choose challenges vs surprises based on impact
        - Truncate learning if too long (extract core message)
        - Decide bullet count (2-4 max)
        - Emphasize contrarian insights over obvious ones
        """
        # Create canvas
        canvas, draw = self.create_panel_canvas(
            bg_color=self.design_system.colors['deep_space']
        )

        # Extract data
        learning = assigned_data.get('learning', '')
        reality = assigned_data.get('reality', {})
        challenges = reality.get('challenges', [])
        surprises = reality.get('surprises', [])

        # === TITLE (grid-aligned) ===
        title_y = self.align_to_grid(24)  # 24 = 3*8px
        self.draw_text(
            draw, "LEARNED", (150, title_y),  # Center of 300px panel
            font_key='small_bold',
            color='electric_green',
            align='center'
        )

        # === MAIN LEARNING (hero insight) ===
        if learning:
            learning_y = self.align_to_grid(72)  # 72 = 9*8px

            # AUTONOMY: Extract core insight if too long
            core_learning = self._extract_core_insight(learning)

            learning_height = self.draw_wrapped_text(
                draw, core_learning,
                x=16,  # 2 grid units margin
                y=learning_y,
                max_width=268,  # 300 - 32 (margins)
                font_key='small',
                color='cosmic_white'
            )

        # === CHALLENGES OR SURPRISES (context bullets) ===
        # AUTONOMY: Decide which to show based on impact
        bullets, bullet_label = self._select_context_bullets(challenges, surprises)

        if bullets:
            bullets_y = learning_y + learning_height + self.align_to_grid(24)  # 24px gap

            # Show label
            self.draw_text(
                draw, bullet_label,
                (16, bullets_y),
                font_key='tiny',
                color='text_dim',
                align='left'
            )

            # Show bullets (max 4)
            bullet_start_y = bullets_y + 24
            available_height = 400 - bullet_start_y - self.align_to_grid(32)
            line_height = self.design_system.line_height
            max_bullets = min(len(bullets), int(available_height / line_height), 4)

            for i in range(max_bullets):
                item_y = bullet_start_y + (i * line_height)
                bullet_text = bullets[i]

                # Truncate intelligently
                if len(bullet_text) > 35:
                    bullet_text = bullet_text[:32] + "..."

                self.draw_text(
                    draw, f"• {bullet_text}",
                    (24, item_y),  # Indent bullets
                    font_key='tiny',
                    color='cosmic_white',
                    align='left'
                )

        return canvas

    def _extract_core_insight(self, learning: str) -> str:
        """
        AUTONOMY ZONE: Extract core message from long learning text.

        Strategy:
        - If learning has multiple sentences, take first 1-2
        - Look for contrarian insights (beat, not, actually, surprisingly)
        - Preserve action-oriented language
        - Max ~120 chars for readability

        For now: Simple truncation at sentence boundary
        Future: NLP-based insight extraction
        """
        # Phase 1: Keep full text if <= 150 chars
        if len(learning) <= 150:
            return learning

        # Phase 2: Truncate at sentence boundary
        sentences = learning.split('. ')
        if len(sentences) > 1:
            return sentences[0] + '.'

        # Fallback: Hard truncate
        return learning[:147] + "..."

    def _select_context_bullets(self, challenges: List[str], surprises: List[str]) -> tuple:
        """
        AUTONOMY ZONE: Choose whether to show challenges or surprises.

        Strategy:
        - Surprises > Challenges (more engaging, less obvious)
        - Contrarian surprises rank highest
        - Show challenges only if no surprises or very impactful
        - Mix both if space allows

        Returns:
            (bullets_to_show, label)
        """
        # AUTONOMY: Prefer surprises (more interesting)
        if surprises:
            # Rank surprises by impact
            ranked_surprises = self._rank_by_impact(surprises)
            return (ranked_surprises, "Surprises:")
        elif challenges:
            # Fallback to challenges
            ranked_challenges = self._rank_by_impact(challenges)
            return (ranked_challenges, "Challenges:")
        else:
            return ([], "")

    def _rank_by_impact(self, items: List[str]) -> List[str]:
        """
        AUTONOMY ZONE: Rank items by impact/interest.

        High-impact signals:
        - Quantitative data (numbers, percentages)
        - Contrarian language (but, actually, surprisingly, not)
        - Specificity (concrete > vague)

        For now: Simple heuristic scoring
        Future: NLP-based sentiment + surprise analysis
        """
        def score_item(item: str) -> int:
            score = 0

            # Numbers = concrete
            if any(char.isdigit() for char in item):
                score += 2

            # Contrarian signals
            contrarian_words = ['but', 'actually', 'surprisingly', 'not', 'instead', 'however']
            if any(word in item.lower() for word in contrarian_words):
                score += 3

            # Specificity (longer = more detail)
            if len(item) > 40:
                score += 1

            return score

        # Sort by score (descending)
        scored = [(item, score_item(item)) for item in items]
        scored.sort(key=lambda x: x[1], reverse=True)

        return [item for item, score in scored]


# === Example Usage ===
if __name__ == "__main__":
    # Test the Learning Panel Agent
    agent = LearningPanelAgent()

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
    panel.save(output_dir / 'learning_panel_arkify.png')
    print(f"✅ Learning panel saved to: {output_dir / 'learning_panel_arkify.png'}")
