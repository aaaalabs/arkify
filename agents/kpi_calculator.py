"""
KPI Calculator Agent
Phase 0: Basic metrics calculation

Calculates:
- Cost per hour
- Project velocity (if baseline provided)
- Simple comparison metrics
"""

from typing import Dict, Any


class KPICalculator:
    """
    Calculate key performance indicators from project data.

    Phase 0: Simple math only
    Phase 4: Add AI-powered insight generation
    """

    def calculate(self, project: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate KPIs from project data.

        Args:
            project: Project data dictionary

        Returns:
            Dictionary of calculated KPIs
        """
        hours = project['hours']
        cost = project['cost']

        # Basic calculations
        cost_per_hour = cost / hours if hours > 0 else 0

        kpis = {
            'total_hours': hours,
            'total_cost': cost,
            'cost_per_hour': round(cost_per_hour, 2),

            # Visual formatting helpers
            'hours_display': self._format_hours(hours),
            'cost_display': self._format_cost(cost),
            'cost_per_hour_display': self._format_cost(cost_per_hour),
        }

        # Extended metrics (if available)
        if 'extended' in project:
            extended = project['extended']

            # Results metrics
            if 'results' in extended:
                results = extended['results']
                kpis['users'] = results.get('users', 0)
                kpis['signups'] = results.get('signups', 0)
                kpis['revenue'] = results.get('revenue', 0)

            # Reality check metrics
            if 'expectations' in extended and 'reality' in extended:
                expected_timeline = extended['expectations'].get('timeline', '')
                actual_timeline = extended['reality'].get('timeline', '')
                kpis['timeline_comparison'] = {
                    'expected': expected_timeline,
                    'actual': actual_timeline
                }

        return kpis

    def _format_hours(self, hours: float) -> str:
        """Format hours for display."""
        if hours < 1:
            return f"{int(hours * 60)}min"
        elif hours == 1:
            return "1 hour"
        elif hours < 24:
            return f"{int(hours)}h"
        else:
            days = hours / 24
            return f"{days:.1f} days"

    def _format_cost(self, cost: float) -> str:
        """Format cost for display (assumes EUR)."""
        if cost == 0:
            return "Free"
        elif cost < 1:
            return f"€{cost:.2f}"
        else:
            return f"€{int(cost)}"
