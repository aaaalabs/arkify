"""
Story Arc Designer Agent

Determines optimal panel ordering for narrative flow.
Simple, Lovable, Complete - Phase 1 implementation.
"""

def design_story_arc(project_data):
    """
    Design the story arc and panel ordering.

    Args:
        project_data: Dict containing project information

    Returns:
        Dict with panel_order and story_type
    """

    # Detect story type based on data patterns
    story_type = _detect_story_type(project_data)

    # Determine panel order based on story type
    panel_order = _get_panel_order(story_type, project_data)

    return {
        "story_type": story_type,
        "panel_order": panel_order,
        "narrative_flow": _get_narrative_flow(story_type)
    }


def _detect_story_type(project_data):
    """
    Detect the type of story to tell.

    Types:
    - struggle_story: Reality took longer/cost more than expected (relatable)
    - success_story: Good results, impressive numbers (aspirational)
    - learning_story: Focus on insights and lessons (educational)
    """

    # Check if we have expectations vs reality data
    has_expectations = "expectations" in project_data
    has_reality = "reality" in project_data
    has_results = "results" in project_data

    # Struggle story: Reality > Expectations
    if has_expectations and has_reality:
        expected_days = _parse_days(project_data["expectations"].get("timeline", ""))
        reality_days = _parse_days(project_data["reality"].get("timeline", ""))

        if reality_days > expected_days * 1.5:  # 50% longer than expected
            return "struggle_story"

    # Success story: Good results
    if has_results:
        results = project_data["results"]
        users = results.get("users", 0)
        revenue = results.get("revenue", 0)

        if users > 100 or revenue > 1000:
            return "success_story"

    # Default: Learning story
    return "learning_story"


def _get_panel_order(story_type, project_data):
    """
    Get panel order based on story type.

    Panel IDs:
    - header: Project name, tagline, key stats
    - results: Users, revenue, metrics
    - tech_stack: Technologies used
    - expected: Original plan
    - reality: What actually happened
    - learning: Key insight + CTA
    """

    # Check which panels we can create
    has_results = "results" in project_data
    has_expectations = "expectations" in project_data and "reality" in project_data

    if story_type == "struggle_story":
        # Lead with struggle, show perseverance
        # Hook: "I thought it would be easy..."
        order = ["header"]
        if has_expectations:
            order.extend(["expected", "reality"])
        if has_results:
            order.append("results")
        order.extend(["tech_stack", "learning"])
        return order

    elif story_type == "success_story":
        # Lead with results, show method
        # Hook: "From 0 to 127 users in 4 weeks"
        order = ["header"]
        if has_results:
            order.append("results")
        order.append("tech_stack")
        if has_expectations:
            order.extend(["expected", "reality"])
        order.append("learning")
        return order

    else:  # learning_story
        # Balanced flow: plan → reality → learning
        order = ["header"]
        if has_expectations:
            order.extend(["expected", "reality"])
        order.append("tech_stack")
        if has_results:
            order.append("results")
        order.append("learning")
        return order


def _get_narrative_flow(story_type):
    """Get narrative description for story type."""

    flows = {
        "struggle_story": "Problem → Struggle → Reality → Perseverance → Wisdom",
        "success_story": "Achievement → Method → Reality Check → Wisdom",
        "learning_story": "Plan → Reality → Tools → Outcome → Wisdom"
    }

    return flows.get(story_type, "Unknown")


def _parse_days(timeline_str):
    """
    Parse timeline string to extract number of days.

    Examples:
    - "2 days" -> 2
    - "2-3 days" -> 2.5
    - "5 days, multiple evenings" -> 5
    - "a weekend" -> 2
    """

    if not timeline_str:
        return 0

    timeline_lower = timeline_str.lower()

    # Try to extract number
    import re
    numbers = re.findall(r'\d+', timeline_lower)

    if numbers:
        # If range like "2-3", take average
        if len(numbers) >= 2 and '-' in timeline_lower:
            return (int(numbers[0]) + int(numbers[1])) / 2
        return int(numbers[0])

    # Handle words
    if "weekend" in timeline_lower:
        return 2
    if "week" in timeline_lower:
        return 7

    return 0


# Simple test
if __name__ == "__main__":
    # Test struggle story
    test_data = {
        "name": "AI Todo App",
        "expectations": {"timeline": "2 days"},
        "reality": {"timeline": "5 days"},
        "results": {"users": 127},
        "tech_stack": ["Cursor", "Claude", "Next.js", "Vercel"],
        "learning": "Ship fast, iterate later"
    }

    arc = design_story_arc(test_data)
    print("Story Type:", arc["story_type"])
    print("Panel Order:", arc["panel_order"])
    print("Narrative Flow:", arc["narrative_flow"])
