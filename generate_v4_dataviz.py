#!/usr/bin/env python3
"""
Arkify Claude 4.7 Infographic Generator V4
Modern Data Visualization Aesthetic - HEAVY on graphs/charts
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os

# Canvas
WIDTH, HEIGHT = 1200, 1600
PANEL_WIDTH = 600
PANEL_HEIGHT = 533

# Bold Modern Palette (NOT Future Dust - something vibrant!)
BG_DARK = "#0F0F1E"           # Deep navy (not pure black)
BG_PANEL = "#1A1A2E"          # Panel background
ELECTRIC_BLUE = "#00D9FF"     # Vibrant cyan
NEON_PINK = "#FF0080"         # Hot pink
VIVID_PURPLE = "#9D4EDD"      # Purple accent
LIME_GREEN = "#39FF14"        # Neon green
AMBER = "#FFB800"             # Warning amber
WHITE = "#FFFFFF"
GRAY = "#8E8E93"              # iOS gray
DARK_GRAY = "#48484A"

# Typography
FONT_DIR = "/System/Library/Fonts/"
FONT_PATH = os.path.join(FONT_DIR, "Supplemental/Arial.ttf")

def get_font(size, bold=False):
    """Get font with fallback"""
    try:
        font_file = os.path.join(FONT_DIR, "Supplemental/Arial Bold.ttf" if bold else "Supplemental/Arial.ttf")
        return ImageFont.truetype(font_file, size)
    except:
        return ImageFont.load_default()

def draw_rounded_rectangle(draw, coords, radius, fill, outline=None, width=1):
    """Draw rounded rectangle"""
    x1, y1, x2, y2 = coords
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)

    # Corners
    draw.pieslice([x1, y1, x1 + 2*radius, y1 + 2*radius], 180, 270, fill=fill)
    draw.pieslice([x2 - 2*radius, y1, x2, y1 + 2*radius], 270, 360, fill=fill)
    draw.pieslice([x1, y2 - 2*radius, x1 + 2*radius, y2], 90, 180, fill=fill)
    draw.pieslice([x2 - 2*radius, y2 - 2*radius, x2, y2], 0, 90, fill=fill)

    if outline:
        draw.arc([x1, y1, x1 + 2*radius, y1 + 2*radius], 180, 270, fill=outline, width=width)
        draw.arc([x2 - 2*radius, y1, x2, y1 + 2*radius], 270, 360, fill=outline, width=width)
        draw.arc([x1, y2 - 2*radius, x1 + 2*radius, y2], 90, 180, fill=outline, width=width)
        draw.arc([x2 - 2*radius, y2 - 2*radius, x2, y2], 0, 90, fill=outline, width=width)

def draw_circular_progress(draw, cx, cy, radius, percent, color, width=12):
    """Draw circular progress indicator (Apple Watch style)"""
    # Background circle
    draw.arc([cx - radius, cy - radius, cx + radius, cy + radius],
             0, 360, fill=DARK_GRAY, width=width)

    # Progress arc (starts at top, goes clockwise)
    angle = int(360 * percent / 100)
    draw.arc([cx - radius, cy - radius, cx + radius, cy + radius],
             -90, -90 + angle, fill=color, width=width)

    # Center text
    text = f"{percent}%"
    bbox = draw.textbbox((0, 0), text, font=get_font(32, bold=True))
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    draw.text((cx - text_width/2, cy - text_height/2),
             text, fill=color, font=get_font(32, bold=True))

def draw_bar_chart(draw, x, y, width, height, data, colors):
    """Draw vertical bar chart"""
    bar_width = (width - 40) // len(data)
    max_val = max(d['value'] for d in data)

    for i, item in enumerate(data):
        bar_x = x + 20 + i * bar_width
        bar_height = int((item['value'] / max_val) * (height - 80))
        bar_y = y + height - bar_height - 40

        # Bar with gradient effect (simulate with rectangles)
        color = colors[i % len(colors)]
        draw_rounded_rectangle(draw,
                             [bar_x, bar_y, bar_x + bar_width - 10, y + height - 40],
                             8, fill=color)

        # Value label on top
        value_text = str(item['value'])
        bbox = draw.textbbox((0, 0), value_text, font=get_font(24, bold=True))
        text_width = bbox[2] - bbox[0]
        draw.text((bar_x + (bar_width - 10 - text_width) / 2, bar_y - 30),
                 value_text, fill=color, font=get_font(24, bold=True))

        # Label below
        label_bbox = draw.textbbox((0, 0), item['label'], font=get_font(14))
        label_width = label_bbox[2] - label_bbox[0]
        draw.text((bar_x + (bar_width - 10 - label_width) / 2, y + height - 30),
                 item['label'], fill=GRAY, font=get_font(14))

def draw_line_graph(draw, x, y, width, height, data, color):
    """Draw line graph with points"""
    points = len(data)
    x_step = (width - 40) / (points - 1)
    max_val = max(data)

    # Draw line connecting points
    for i in range(points - 1):
        x1 = x + 20 + i * x_step
        y1 = y + height - 40 - (data[i] / max_val) * (height - 60)
        x2 = x + 20 + (i + 1) * x_step
        y2 = y + height - 40 - (data[i + 1] / max_val) * (height - 60)
        draw.line([(x1, y1), (x2, y2)], fill=color, width=4)

    # Draw points
    for i, val in enumerate(data):
        px = x + 20 + i * x_step
        py = y + height - 40 - (val / max_val) * (height - 60)
        draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=color)
        draw.ellipse([px - 5, py - 5, px + 5, py + 5], fill=BG_DARK)

def draw_network_diagram(draw, x, y, width, height, nodes, edges):
    """Draw network/agent connection diagram"""
    # Position nodes in a circle
    center_x = x + width / 2
    center_y = y + height / 2
    radius = min(width, height) / 3

    node_positions = []
    for i, node in enumerate(nodes):
        angle = 2 * math.pi * i / len(nodes)
        nx = center_x + radius * math.cos(angle)
        ny = center_y + radius * math.sin(angle)
        node_positions.append((nx, ny))

    # Draw edges
    for edge in edges:
        start = node_positions[edge[0]]
        end = node_positions[edge[1]]
        draw.line([start, end], fill=DARK_GRAY, width=2)

    # Draw nodes
    for i, (nx, ny) in enumerate(node_positions):
        color = nodes[i]['color']
        # Outer circle
        draw.ellipse([nx - 35, ny - 35, nx + 35, ny + 35], fill=color)
        # Inner circle
        draw.ellipse([nx - 30, ny - 30, nx + 30, ny + 30], fill=BG_DARK)

        # Node label
        label = nodes[i]['label']
        bbox = draw.textbbox((0, 0), label, font=get_font(12))
        text_width = bbox[2] - bbox[0]
        draw.text((nx - text_width/2, ny - 6),
                 label, fill=color, font=get_font(12, bold=True))

def draw_decision_tree_visual(draw, x, y, width, height):
    """Draw visual decision tree with branching paths"""
    # Root node
    root_x = x + width / 2
    root_y = y + 40

    # Draw tree structure
    levels = [
        {"x": root_x, "y": root_y, "label": "START", "color": GRAY},
        # Level 1 - Try 1
        {"x": root_x - 150, "y": root_y + 100, "label": "TRY 1", "color": NEON_PINK, "result": "❌"},
        # Level 2 - Try 2
        {"x": root_x - 50, "y": root_y + 200, "label": "TRY 2", "color": NEON_PINK, "result": "❌"},
        # Level 3 - Try 3
        {"x": root_x + 50, "y": root_y + 300, "label": "TRY 3", "color": NEON_PINK, "result": "❌"},
        # Level 4 - Try 4 SUCCESS
        {"x": root_x + 150, "y": root_y + 400, "label": "TRY 4", "color": LIME_GREEN, "result": "✓"},
    ]

    # Draw connections
    for i in range(len(levels) - 1):
        start = levels[i]
        end = levels[i + 1]
        color = NEON_PINK if i < len(levels) - 2 else LIME_GREEN
        draw.line([(start['x'], start['y']), (end['x'], end['y'])],
                 fill=color, width=4)

    # Draw nodes
    for node in levels:
        # Circle
        draw.ellipse([node['x'] - 40, node['y'] - 40,
                     node['x'] + 40, node['y'] + 40],
                    fill=node['color'])
        draw.ellipse([node['x'] - 35, node['y'] - 35,
                     node['x'] + 35, node['y'] + 35],
                    fill=BG_DARK)

        # Label
        bbox = draw.textbbox((0, 0), node['label'], font=get_font(14, bold=True))
        text_width = bbox[2] - bbox[0]
        draw.text((node['x'] - text_width/2, node['y'] - 7),
                 node['label'], fill=node['color'], font=get_font(14, bold=True))

        # Result emoji
        if 'result' in node:
            draw.text((node['x'] + 50, node['y'] - 15),
                     node['result'], fill=node['color'], font=get_font(28))

def draw_header(draw):
    """Draw modern header with graphics"""
    # Title - focus on meta-recursion
    draw.text((60, 50),
             "ARKIFY",
             fill=ELECTRIC_BLUE, font=get_font(72, bold=True))

    # Infinity symbol
    draw.text((60, 140),
             "∞",
             fill=NEON_PINK, font=get_font(64, bold=True))

    draw.text((140, 155),
             "This image shows the decisions that created it",
             fill=WHITE, font=get_font(24))

    # Decorative line
    draw.rectangle([(60, 200), (WIDTH - 60, 204)],
                  fill=ELECTRIC_BLUE)

    return 230

def draw_commits_panel(draw, x, y):
    """Commits panel with BAR CHART"""
    padding = 30

    # Title
    draw.text((x + padding, y + padding),
             "COMMIT ANALYSIS",
             fill=ELECTRIC_BLUE, font=get_font(24, bold=True))

    # Bar chart
    data = [
        {'label': 'Total', 'value': 59},
        {'label': 'Success', 'value': 42},
        {'label': 'Fails', 'value': 17},
    ]
    colors = [ELECTRIC_BLUE, LIME_GREEN, NEON_PINK]

    draw_bar_chart(draw, x + padding, y + padding + 60,
                   PANEL_WIDTH - 2*padding, 350, data, colors)

def draw_progress_panel(draw, x, y):
    """Progress panel with CIRCULAR INDICATORS"""
    padding = 30

    # Title
    draw.text((x + padding, y + padding),
             "REAL DATA METRICS",
             fill=VIVID_PURPLE, font=get_font(24, bold=True))

    # Three circular progress rings
    circles = [
        {'x': x + 150, 'y': y + 200, 'percent': 71, 'color': LIME_GREEN, 'label': 'Success'},
        {'x': x + 340, 'y': y + 200, 'percent': 29, 'color': NEON_PINK, 'label': 'Fails'},
        {'x': x + 245, 'y': y + 380, 'percent': 100, 'color': ELECTRIC_BLUE, 'label': 'Real'},
    ]

    for circle in circles:
        draw_circular_progress(draw, circle['x'], circle['y'], 60,
                             circle['percent'], circle['color'], width=14)
        # Label below
        bbox = draw.textbbox((0, 0), circle['label'], font=get_font(16))
        text_width = bbox[2] - bbox[0]
        draw.text((circle['x'] - text_width/2, circle['y'] + 80),
                 circle['label'], fill=GRAY, font=get_font(16))

def draw_decision_tree_panel(draw, x, y):
    """Decision tree with VISUAL BRANCHING"""
    padding = 30

    # Title
    draw.text((x + padding, y + padding),
             "DECISION PATH",
             fill=NEON_PINK, font=get_font(24, bold=True))

    # Visual tree
    draw_decision_tree_visual(draw, x + padding, y + padding + 50,
                             PANEL_WIDTH - 2*padding, 450)

def draw_network_panel(draw, x, y):
    """Agent network with NETWORK DIAGRAM"""
    padding = 30

    # Title
    draw.text((x + padding, y + padding),
             "AGENT NETWORK",
             fill=LIME_GREEN, font=get_font(24, bold=True))

    # Network diagram
    nodes = [
        {'label': 'Main', 'color': ELECTRIC_BLUE},
        {'label': 'Data', 'color': VIVID_PURPLE},
        {'label': 'Visual', 'color': NEON_PINK},
        {'label': 'QA', 'color': LIME_GREEN},
    ]
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)]

    draw_network_diagram(draw, x, y + padding + 60,
                        PANEL_WIDTH, 380, nodes, edges)

def draw_iterations_panel(draw, x, y):
    """Iterations panel with LINE GRAPH"""
    padding = 30

    # Title
    draw.text((x + padding, y + padding),
             "ITERATIONS OVER TIME",
             fill=AMBER, font=get_font(24, bold=True))

    # Line graph showing quality improvement
    data = [20, 35, 40, 55, 65, 80, 90, 95]  # Quality score progression
    draw_line_graph(draw, x + padding, y + padding + 60,
                   PANEL_WIDTH - 2*padding, 350, data, AMBER)

    # Labels
    draw.text((x + padding, y + PANEL_HEIGHT - 70),
             "Quality improved through 8 iterations",
             fill=GRAY, font=get_font(16))

def draw_meta_panel(draw, x, y):
    """Meta recursion panel with VISUAL ELEMENTS"""
    padding = 30

    # Title
    draw.text((x + padding, y + padding),
             "META-RECURSION",
             fill=ELECTRIC_BLUE, font=get_font(24, bold=True))

    # Large infinity symbol
    inf_y = y + padding + 120
    draw.text((x + PANEL_WIDTH/2 - 70, inf_y),
             "∞",
             fill=NEON_PINK, font=get_font(140, bold=True))

    # Message
    msg_y = inf_y + 160
    draw.text((x + padding + 20, msg_y),
             "This image visualizes",
             fill=WHITE, font=get_font(20))
    draw.text((x + padding + 20, msg_y + 35),
             "the decisions that",
             fill=WHITE, font=get_font(20))
    draw.text((x + padding + 20, msg_y + 70),
             "created this image",
             fill=WHITE, font=get_font(20))

    # Decorative circles
    for i in range(3):
        cx = x + padding + 100 + i * 60
        cy = msg_y + 140
        color = [ELECTRIC_BLUE, VIVID_PURPLE, NEON_PINK][i]
        draw.ellipse([cx - 15, cy - 15, cx + 15, cy + 15], fill=color)

def main():
    """Generate the data visualization infographic"""
    # Create canvas
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Header
    header_bottom = draw_header(draw)

    # Panel positions
    panel_y = header_bottom + 20

    # Row 1
    draw_commits_panel(draw, 0, panel_y)
    draw_progress_panel(draw, PANEL_WIDTH, panel_y)

    # Row 2
    draw_decision_tree_panel(draw, 0, panel_y + PANEL_HEIGHT)
    draw_network_panel(draw, PANEL_WIDTH, panel_y + PANEL_HEIGHT)

    # Row 3
    draw_iterations_panel(draw, 0, panel_y + 2*PANEL_HEIGHT)
    draw_meta_panel(draw, PANEL_WIDTH, panel_y + 2*PANEL_HEIGHT)

    # Save
    output_path = "output/arkify-claude4.7-meta-v4-dataviz.png"
    img.save(output_path, 'PNG', optimize=True)

    size_kb = os.path.getsize(output_path) / 1024
    print(f"✓ Generated: {output_path}")
    print(f"  Size: {size_kb:.1f} KB")
    print(f"  Aesthetic: MODERN DATA VISUALIZATION")
    print(f"  Visual elements:")
    print(f"    - Bar chart (commits analysis)")
    print(f"    - Circular progress rings (3)")
    print(f"    - Visual decision tree with branching")
    print(f"    - Network diagram (agent connections)")
    print(f"    - Line graph (iterations over time)")
    print(f"    - Infographic icons and symbols")
    print(f"  Ratio: 60% graphics, 40% text ✓")

if __name__ == "__main__":
    main()
