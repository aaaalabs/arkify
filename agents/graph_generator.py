"""
Graph Generator Agent

Creates comparison charts for Expected vs Reality.
Simple, Lovable, Complete - Phase 1 implementation.
"""

import matplotlib
matplotlib.use('Agg')  # Non-GUI backend
import matplotlib.pyplot as plt
from PIL import Image
import io
import re


def generate_timeline_comparison(expected_timeline, reality_timeline, colors=None):
    """
    Generate Expected vs Reality timeline bar chart.

    Args:
        expected_timeline: String like "2 days" or "2-3 days"
        reality_timeline: String like "5 days"
        colors: Dict with 'expected' and 'reality' color codes

    Returns:
        PIL Image object
    """

    # Default colors (Future Dust palette)
    if colors is None:
        colors = {
            "expected": "#6B7280",  # Gray (dimmed)
            "reality": "#06FFA5",   # Electric green (vivid)
            "background": "#22223B", # Dark background
            "text": "#F2F4F8"       # Off-white text
        }

    # Parse days
    expected_days = _parse_days(expected_timeline)
    reality_days = _parse_days(reality_timeline)

    # Create figure
    fig, ax = plt.subplots(figsize=(6, 4), facecolor=colors["background"])
    ax.set_facecolor(colors["background"])

    # Data
    labels = ['Expected', 'Reality']
    values = [expected_days, reality_days]
    bar_colors = [colors["expected"], colors["reality"]]

    # Create horizontal bars
    bars = ax.barh(labels, values, color=bar_colors, height=0.6)

    # Add value labels on bars
    for i, (bar, value) in enumerate(zip(bars, values)):
        width = bar.get_width()
        label = expected_timeline if i == 0 else reality_timeline
        ax.text(width * 0.95, bar.get_y() + bar.get_height()/2,
                f'  {label}',
                ha='right', va='center',
                color='white',
                fontsize=14,
                fontweight='bold')

    # Style
    ax.set_xlabel('Days', color=colors["text"], fontsize=12)
    ax.tick_params(colors=colors["text"])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(colors["text"])
    ax.spines['left'].set_color(colors["text"])

    # Set y-axis labels
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, color=colors["text"], fontsize=12)

    # Tight layout
    plt.tight_layout()

    # Convert to PIL Image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150, facecolor=colors["background"])
    buf.seek(0)
    img = Image.open(buf)

    plt.close(fig)

    return img


def generate_cost_comparison(expected_cost, reality_cost, colors=None):
    """
    Generate Expected vs Reality cost bar chart.

    Args:
        expected_cost: Number (EUR)
        reality_cost: Number (EUR)
        colors: Dict with color codes

    Returns:
        PIL Image object
    """

    # Default colors
    if colors is None:
        colors = {
            "expected": "#6B7280",
            "reality": "#06FFA5",
            "background": "#22223B",
            "text": "#F2F4F8"
        }

    # Create figure
    fig, ax = plt.subplots(figsize=(6, 4), facecolor=colors["background"])
    ax.set_facecolor(colors["background"])

    # Data
    labels = ['Expected', 'Reality']
    values = [expected_cost, reality_cost]
    bar_colors = [colors["expected"], colors["reality"]]

    # Create horizontal bars
    bars = ax.barh(labels, values, color=bar_colors, height=0.6)

    # Add value labels on bars
    for bar, value in zip(bars, values):
        width = bar.get_width()
        ax.text(width * 0.95, bar.get_y() + bar.get_height()/2,
                f'  €{value}',
                ha='right', va='center',
                color='white',
                fontsize=14,
                fontweight='bold')

    # Style
    ax.set_xlabel('Cost (EUR)', color=colors["text"], fontsize=12)
    ax.tick_params(colors=colors["text"])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(colors["text"])
    ax.spines['left'].set_color(colors["text"])

    # Set y-axis labels
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, color=colors["text"], fontsize=12)

    # Tight layout
    plt.tight_layout()

    # Convert to PIL Image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150, facecolor=colors["background"])
    buf.seek(0)
    img = Image.open(buf)

    plt.close(fig)

    return img


def _parse_days(timeline_str):
    """
    Parse timeline string to extract number of days.

    Examples:
    - "2 days" -> 2
    - "2-3 days" -> 2.5
    - "5 days, multiple evenings" -> 5
    """

    if not timeline_str:
        return 0

    if isinstance(timeline_str, (int, float)):
        return float(timeline_str)

    timeline_lower = str(timeline_str).lower()

    # Try to extract number
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
    print("Testing Graph Generator...")

    # Test timeline comparison
    img1 = generate_timeline_comparison("2 days", "5 days")
    img1.save("test_timeline.png")
    print(f"✓ Timeline chart generated: {img1.size}")

    # Test cost comparison
    img2 = generate_cost_comparison(20, 37)
    img2.save("test_cost.png")
    print(f"✓ Cost chart generated: {img2.size}")

    print("Done! Check test_timeline.png and test_cost.png")
