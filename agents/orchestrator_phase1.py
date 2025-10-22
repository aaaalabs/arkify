"""
Orchestrator Agent - Phase 1
Coordinates Story Arc Designer + Graph Generator + Layout Compositor Phase 1

Simple, Lovable, Complete
"""

from pathlib import Path
from typing import Dict, Any

from .kpi_calculator import KPICalculator
from .icon_fetcher import IconFetcher
from .story_arc_designer import design_story_arc
from .layout_compositor_phase1 import LayoutCompositorPhase1


class OrchestratorPhase1:
    """
    Phase 1 orchestrator with story arc and 3x3 layout.
    """

    def __init__(self):
        """Initialize all agents."""
        self.kpi_calculator = KPICalculator()
        self.icon_fetcher = IconFetcher()
        self.layout_compositor = LayoutCompositorPhase1()

    def generate(self, project_data: Dict[str, Any]) -> Path:
        """
        Generate Phase 1 project breakdown.

        Args:
            project_data: Parsed YAML data with Phase 1 fields

        Returns:
            Path to generated PNG file
        """
        project = project_data['project']

        # Step 1: Design story arc
        print("  📖 Designing story arc...")
        story_arc = design_story_arc(project)
        print(f"     Story type: {story_arc['story_type']}")
        print(f"     Panel order: {story_arc['panel_order']}")

        # Step 2: Calculate KPIs
        print("  📊 Calculating KPIs...")
        kpis = self.kpi_calculator.calculate(project)

        # Step 3: Fetch tech stack icons
        print("  🎨 Fetching tech stack icons...")
        tech_stack = project.get('tech_stack', [])
        icons = self.icon_fetcher.fetch(tech_stack) if tech_stack else []

        # Step 4: Prepare layout data
        layout_data = {
            'name': project['name'],
            'tagline': project.get('tagline', ''),
            'hours': project.get('hours', 0),
            'cost': project.get('cost', 0),
            'tech_stack': tech_stack,
            'kpis': kpis,
            'icons': icons,
            'learning': project.get('learning', ''),
            'results': project.get('results', {}),
            'expectations': project.get('expectations', {}),
            'reality': project.get('reality', {}),
        }

        # Step 5: Compose 3x3 layout
        print("  🖼️  Composing 3x3 layout with Future Dust palette...")
        output_path = self.layout_compositor.compose(layout_data, story_arc['panel_order'])

        return output_path
