"""
Results Panel Agent
Shows actual project outcomes and metrics

Autonomy Level: 50%
- Decides which metrics to emphasize (users vs commits vs LOC)
- Controls number formatting (K, M abbreviations)
- Chooses visual graph style
"""

from typing import Dict, Any
from PIL import Image, ImageDraw
from agents.panel_agent_base import PanelAgentBase, PanelAgentMessage


class ResultsPanelAgent(PanelAgentBase):
    """
    Autonomous agent for Results panel.

    Signature Style:
    - Electric green for success metrics
    - Large numbers (hero metrics)
    - Small supporting metrics below
    - Optional visual graph/bar
    """

    def __init__(self):
        super().__init__(agent_id="results_panel_agent")

    def negotiate(self, available_data: Dict[str, Any]) -> PanelAgentMessage:
        """
        Phase 1: Declare data needs.

        Results panel wants:
        - results.* (all metrics)
        - Adapts based on project type (SaaS vs Dev Tool)
        """
        return PanelAgentMessage(
            agent_id=self.agent_id,
            phase="negotiation",
            panel_position=(2, 2),  # Column 2, Row 2 (right of bottom row)
            data_requested=[
                "results"  # Entire results object
            ],
            visual_weight=0.5,  # MEDIUM (data-heavy but not the story climax)
            color_emphasis="electric_green",
            animation_intent="count_up"
        )

    def render(self, assigned_data: Dict[str, Any]) -> Image.Image:
        """
        Phase 2: Create Results panel (300x400px).

        Layout Strategy:
        1. Title at top (24px from top, 8px grid)
        2. PRIMARY metric (huge, center) - users OR commits OR files
        3. SECONDARY metrics (2-3 supporting stats)
        4. Optional growth indicator (week_one → week_four)

        Adaptive Decisions:
        - Detect project type (users/revenue = SaaS, commits/LOC = Dev Tool)
        - Format large numbers (1000 → 1K, 1000000 → 1M)
        - Show failures honestly (if present)
        - Prioritize metrics with most variance
        """
        # Create canvas
        canvas, draw = self.create_panel_canvas(
            bg_color=self.design_system.colors['deep_space']
        )

        # Extract data
        results = assigned_data.get('results', {})

        # === TITLE (grid-aligned) ===
        title_y = self.align_to_grid(24)  # 24 = 3*8px
        self.draw_text(
            draw, "RESULTS", (150, title_y),  # Center of 300px panel
            font_key='small_bold',
            color='electric_green',
            align='center'
        )

        # === DETECT PRIMARY METRIC ===
        primary_metric, primary_label = self._detect_primary_metric(results)

        # === PRIMARY METRIC (hero number) ===
        if primary_metric is not None:
            metric_y = self.align_to_grid(96)  # 96 = 12*8px

            # Format large numbers
            formatted_metric = self._format_number(primary_metric)

            self.draw_text(
                draw, str(formatted_metric),
                (150, metric_y),
                font_key='huge',
                color='electric_green',
                align='center'
            )

            # Label below primary metric
            label_y = metric_y + 72 + 8  # 72px (huge font) + 8px gap
            self.draw_text(
                draw, primary_label,
                (150, label_y),
                font_key='small',
                color='text_dim',
                align='center'
            )

        # === SECONDARY METRICS (2-3 supporting stats) ===
        secondary_y = self.align_to_grid(232)  # 232 = 29*8px
        secondary_metrics = self._select_secondary_metrics(results, primary_label)

        for i, (label, value) in enumerate(secondary_metrics):
            item_y = secondary_y + (i * self.design_system.line_height)

            text = f"{label}: {self._format_number(value)}"
            self.draw_text(
                draw, text,
                (150, item_y),
                font_key='tiny',
                color='cosmic_white',
                align='center'
            )

        return canvas

    def _detect_primary_metric(self, results: Dict[str, Any]) -> tuple:
        """
        AUTONOMY ZONE: Decide which metric is most important.

        Priority order:
        1. users (SaaS projects)
        2. commits (Dev projects)
        3. files_created (Dev projects)
        4. lines_of_code (Dev projects)
        """
        if 'users' in results and results['users'] is not None:
            return results['users'], 'users'
        elif 'commits' in results and results['commits'] is not None:
            return results['commits'], 'commits'
        elif 'files_created' in results and results['files_created'] is not None:
            return results['files_created'], 'files'
        elif 'lines_of_code' in results and results['lines_of_code'] is not None:
            return results['lines_of_code'], 'LOC'
        else:
            return 0, 'projects'

    def _select_secondary_metrics(self, results: Dict[str, Any], primary_label: str) -> list:
        """
        AUTONOMY ZONE: Choose 2-3 supporting metrics.

        Strategy:
        - Show failures honestly (dev authenticity)
        - Show iterations (effort transparency)
        - Show growth if present (week_one → week_four)
        - Exclude primary metric from secondary list
        """
        secondary = []

        # Always show failures if present (honesty)
        if 'failures' in results and results['failures']:
            secondary.append(('fails', results['failures']))

        # Show iterations if present (effort)
        if 'iterations' in results and results['iterations']:
            secondary.append(('iterations', results['iterations']))

        # Show LOC if not primary
        if primary_label != 'LOC' and 'lines_of_code' in results:
            secondary.append(('LOC', results['lines_of_code']))

        # Show commits if not primary
        if primary_label != 'commits' and 'commits' in results:
            secondary.append(('commits', results['commits']))

        # Limit to 3 items
        return secondary[:3]

    def _format_number(self, num: int) -> str:
        """
        Format large numbers with K/M abbreviations.

        Examples:
        - 23 → "23"
        - 1609 → "1609" (< 10K, show full)
        - 15000 → "15K"
        - 1200000 → "1.2M"
        """
        if num >= 1000000:
            return f"{num / 1000000:.1f}M"
        elif num >= 10000:
            return f"{num // 1000}K"
        else:
            return str(num)


# === Example Usage ===
if __name__ == "__main__":
    # Test the Results Panel Agent
    agent = ResultsPanelAgent()

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
    panel.save(output_dir / 'results_panel_arkify.png')
    print(f"✅ Results panel saved to: {output_dir / 'results_panel_arkify.png'}")
