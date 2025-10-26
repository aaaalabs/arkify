"""
Timeline Panel Agent
Shows project timeline, milestones, and quality evolution

Autonomy Level: 60%
- Decides which milestones to highlight
- Controls timeline visualization style
- Chooses metric evolution display
"""

from typing import Dict, Any, List, Tuple
from PIL import Image, ImageDraw
from agents.panel_agent_base import PanelAgentBase, PanelAgentMessage


class TimelinePanelAgent(PanelAgentBase):
    """
    Autonomous agent for Timeline panel.

    Signature Style:
    - Horizontal timeline bar (electric green)
    - Milestone markers with context
    - Quality evolution metrics
    - Visual progress indicators
    """

    def __init__(self):
        super().__init__(agent_id="timeline_panel_agent")

    def negotiate(self, available_data: Dict[str, Any]) -> PanelAgentMessage:
        """
        Phase 1: Declare data needs.

        Timeline panel wants:
        - hours (duration)
        - results.iterations (quality improvement cycles)
        - results.failures (honest challenges)
        - reality.challenges (context for timeline events)
        """
        return PanelAgentMessage(
            agent_id=self.agent_id,
            phase="negotiation",
            panel_position=(2, 1),  # Column 2, Row 1 (right of middle row)
            data_requested=[
                "hours",
                "results.iterations",
                "results.failures",
                "results.commits"
            ],
            visual_weight=0.4,  # MEDIUM (supporting context)
            color_emphasis="electric_green",
            animation_intent="progress_fill"
        )

    def render(self, assigned_data: Dict[str, Any]) -> Image.Image:
        """
        Phase 2: Create Timeline panel (300x400px).

        Layout Strategy:
        1. Title at top (24px from top, 8px grid)
        2. Date + Duration line
        3. Horizontal timeline bar (visual anchor)
        4. Milestone markers on timeline
        5. Quality evolution metrics below

        Adaptive Decisions (60% AUTONOMY):
        - Which milestones to mark on timeline
        - How to visualize quality improvement
        - Which metrics to emphasize
        """
        # Create canvas
        canvas, draw = self.create_panel_canvas(
            bg_color=self.design_system.colors['deep_space']
        )

        # Extract data
        hours = assigned_data.get('hours', 0)
        results = assigned_data.get('results', {})
        iterations = results.get('iterations', 0)
        failures = results.get('failures', 0)
        commits = results.get('commits', 0)

        # === TITLE (grid-aligned) ===
        title_y = self.align_to_grid(24)  # 24 = 3*8px
        self.draw_text(
            draw, "TIMELINE", (150, title_y),  # Center of 300px panel
            font_key='small_bold',
            color='electric_green',
            align='center'
        )

        # === DATE + DURATION ===
        date_y = self.align_to_grid(72)  # 72 = 9*8px
        date_text = f"Oct 22, 2025 • {hours}h"
        self.draw_text(
            draw, date_text,
            (150, date_y),
            font_key='tiny',
            color='text_dim',
            align='center'
        )

        # === TIMELINE BAR (visual anchor) ===
        timeline_y = self.align_to_grid(128)  # 128 = 16*8px
        bar_width = 236  # 300 - 64 (margins)
        bar_x_start = 32  # 4 grid units margin
        bar_height = 8

        # Draw timeline background (dim)
        draw.rectangle(
            [bar_x_start, timeline_y, bar_x_start + bar_width, timeline_y + bar_height],
            fill=self.design_system.colors['expected_grey']
        )

        # AUTONOMY: Decide milestone positions based on available data
        milestones = self._calculate_milestones(hours, iterations, failures)

        # Draw milestone markers
        for milestone in milestones:
            marker_x = bar_x_start + int((milestone['position'] / hours) * bar_width)
            marker_y = timeline_y

            # Draw marker (small circle)
            marker_radius = 4
            draw.ellipse(
                [marker_x - marker_radius, marker_y - marker_radius,
                 marker_x + marker_radius, marker_y + marker_radius + bar_height],
                fill=self.design_system.colors['electric_green']
            )

        # Timeline labels (0h and end)
        label_y = timeline_y + bar_height + 8
        self.draw_text(draw, "0h", (bar_x_start, label_y),
                      font_key='tiny', color='text_dim', align='left')
        self.draw_text(draw, f"{hours}h", (bar_x_start + bar_width, label_y),
                      font_key='tiny', color='text_dim', align='right')

        # === QUALITY EVOLUTION METRICS ===
        metrics_y = self.align_to_grid(208)  # 208 = 26*8px

        # AUTONOMY: Choose which quality metrics to show
        quality_metrics = self._select_quality_metrics(iterations, failures, commits)

        for i, (label, before, after) in enumerate(quality_metrics):
            item_y = metrics_y + (i * self.design_system.line_height)

            # Format metric evolution
            if before and after:
                metric_text = f"{label}: {before} → {after}"
            else:
                metric_text = f"{label}: {after}"

            self.draw_text(
                draw, metric_text,
                (150, item_y),
                font_key='tiny',
                color='cosmic_white',
                align='center'
            )

        # === PROGRESS INDICATOR (visual punch) ===
        # Show iteration count as mini progress bars
        if iterations > 0:
            progress_y = 400 - self.align_to_grid(64)  # 64px from bottom
            progress_label_y = progress_y - 20

            self.draw_text(
                draw, f"{iterations} iterations",
                (150, progress_label_y),
                font_key='tiny',
                color='text_dim',
                align='center'
            )

            # Mini progress dots
            dot_spacing = 12
            total_width = iterations * dot_spacing
            start_x = 150 - (total_width // 2)

            for i in range(iterations):
                dot_x = start_x + (i * dot_spacing)
                draw.ellipse(
                    [dot_x - 3, progress_y - 3, dot_x + 3, progress_y + 3],
                    fill=self.design_system.colors['electric_green']
                )

        return canvas

    def _calculate_milestones(self, hours: int, iterations: int, failures: int) -> List[Dict[str, Any]]:
        """
        AUTONOMY ZONE: Decide which milestones to mark on timeline.

        Strategy:
        - Always mark start (0h) and end (hours)
        - Mark iteration checkpoints (evenly distributed)
        - Mark failure points (if significant)

        Returns:
            List of milestone dicts with 'position' (hour) and 'type'
        """
        milestones = []

        # Start
        milestones.append({'position': 0, 'type': 'start'})

        # Iteration checkpoints (evenly distributed)
        if iterations > 1:
            for i in range(1, iterations):
                milestone_hour = (hours / iterations) * i
                milestones.append({'position': milestone_hour, 'type': 'iteration'})

        # End
        milestones.append({'position': hours, 'type': 'complete'})

        return milestones

    def _select_quality_metrics(self, iterations: int, failures: int, commits: int) -> List[Tuple[str, Any, Any]]:
        """
        AUTONOMY ZONE: Choose which quality evolution metrics to display.

        Strategy:
        - Show contrast improvement (2:1 → 7.12:1) - most dramatic
        - Show iteration count
        - Show failure count (honesty)
        - Show commit velocity

        Returns:
            List of (label, before, after) tuples
        """
        metrics = []

        # Contrast evolution (hardcoded for Phase 1 since it's in reality.challenges)
        # Agent can infer from "poor contrast" challenge
        metrics.append(("Contrast", "2:1", "7.12:1"))

        # Iterations (show as evolution from 0 to final)
        if iterations:
            metrics.append(("Iterations", None, iterations))

        # Failures (honest reporting)
        if failures:
            metrics.append(("Failures", None, failures))

        # Limit to 3 metrics (space constraint)
        return metrics[:3]


# === Example Usage ===
if __name__ == "__main__":
    # Test the Timeline Panel Agent
    agent = TimelinePanelAgent()

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
    panel.save(output_dir / 'timeline_panel_arkify.png')
    print(f"✅ Timeline panel saved to: {output_dir / 'timeline_panel_arkify.png'}")
