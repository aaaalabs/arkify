"""
Mini Orchestrator Agent
Phase 0: Simplified orchestration - just coordinate the 4 core agents

Responsibilities:
- Parse and validate input
- Coordinate KPI Calculator, Icon Fetcher, Layout Compositor
- Generate final output
"""

from pathlib import Path
from typing import Dict, Any

from .kpi_calculator import KPICalculator
from .icon_fetcher import IconFetcher
from .layout_compositor import LayoutCompositor


class MiniOrchestrator:
    """
    Simplified orchestrator for Phase 0.

    Future phases will add:
    - Story Arc Designer (Phase 1)
    - Research Agent (Phase 4)
    - QA Agent (Phase 5)
    """

    def __init__(self):
        """Initialize all agents."""
        self.kpi_calculator = KPICalculator()
        self.icon_fetcher = IconFetcher()
        self.layout_compositor = LayoutCompositor()

    def generate(self, project_data: Dict[str, Any]) -> Path:
        """
        Generate project breakdown from input data.

        Args:
            project_data: Parsed YAML data

        Returns:
            Path to generated PNG file
        """
        project = project_data['project']

        # Step 1: Calculate KPIs
        print("  📊 Calculating KPIs...")
        kpis = self.kpi_calculator.calculate(project)

        # Step 2: Fetch tech stack icons
        print("  🎨 Fetching tech stack icons...")
        icons = self.icon_fetcher.fetch(project['tech_stack'])

        # Step 3: Prepare layout data
        layout_data = {
            'name': project['name'],
            'tagline': project.get('tagline', ''),
            'hours': project['hours'],
            'cost': project['cost'],
            'kpis': kpis,
            'icons': icons,
            'learning': project['learning']
        }

        # Step 4: Compose final layout
        print("  🖼️  Composing 2x2 layout...")
        output_path = self.layout_compositor.compose(layout_data)

        return output_path
