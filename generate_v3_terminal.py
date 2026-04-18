#!/usr/bin/env python3
"""
Arkify Claude 4.7 Infographic Generator V3
Retro-Futuristic Terminal Archaeology Aesthetic
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Canvas
WIDTH, HEIGHT = 1200, 1600
PANEL_WIDTH = 600
PANEL_HEIGHT = 533

# Retro Terminal Palette
BG_DEEP = "#000000"          # Pure black CRT background
BG_DARK = "#0a0a0a"          # Slightly lighter black
PHOSPHOR_GREEN = "#00FF41"   # Classic terminal green (not the muted #06FFA5)
PHOSPHOR_DIM = "#00AA2A"     # Dimmed phosphor
AMBER = "#FFB000"            # Amber for warnings/failures
TEXT_WHITE = "#FFFFFF"       # Pure white for high contrast
TEXT_GRAY = "#666666"        # Dim gray for secondary text
FAIL_RED = "#FF0040"         # Bright error red
SUCCESS_GREEN = "#00FF41"    # Phosphor green for success

# Typography - Retro Terminal Fonts
# Using system monospace for terminal aesthetic
FONT_DIR = "/System/Library/Fonts/"
FONT_MONO = os.path.join(FONT_DIR, "Monaco.dfont")  # Classic Mac terminal font
FONT_SYSTEM = os.path.join(FONT_DIR, "Supplemental/Arial.ttf")

def add_scanlines(img, intensity=0.3):
    """Add CRT scanline effect"""
    draw = ImageDraw.Draw(img, 'RGBA')
    for y in range(0, HEIGHT, 2):
        draw.rectangle([(0, y), (WIDTH, y+1)],
                      fill=(0, 0, 0, int(255 * intensity)))
    return img

def add_glow(img):
    """Add phosphor glow effect"""
    # Create a blurred copy
    glow = img.copy()
    glow = glow.filter(ImageFilter.GaussianBlur(radius=3))
    # Blend with original
    return Image.blend(img, glow, alpha=0.3)

def draw_ascii_border(draw, x, y, w, h, color):
    """Draw retro ASCII-style border"""
    # Top
    draw.text((x, y), "┌" + "─" * int(w/12) + "┐", fill=color, font=get_font(16))
    # Bottom
    draw.text((x, y + h - 20), "└" + "─" * int(w/12) + "┘", fill=color, font=get_font(16))

def get_font(size, mono=False):
    """Get font with fallback"""
    try:
        if mono:
            return ImageFont.truetype(FONT_MONO, size)
        return ImageFont.truetype(FONT_SYSTEM, size)
    except:
        return ImageFont.load_default()

def draw_header(draw):
    """Draw retro terminal header"""
    y = 40

    # Terminal prompt style
    draw.text((60, y), ">_", fill=PHOSPHOR_GREEN, font=get_font(48, mono=True))
    draw.text((130, y), "ARKIFY.ANALYZE", fill=PHOSPHOR_GREEN, font=get_font(48, mono=True))

    # Subtitle
    y += 70
    draw.text((60, y), "THOUGHT ARCHAEOLOGY SYSTEM v4.7",
             fill=PHOSPHOR_DIM, font=get_font(24, mono=True))

    # Infinity symbol with terminal aesthetic
    y += 50
    draw.text((60, y), "∞ META-RECURSION ACHIEVED",
             fill=AMBER, font=get_font(32))

    # Terminal status bar
    y += 50
    draw.rectangle([(60, y), (WIDTH-60, y+2)], fill=PHOSPHOR_DIM)

    return y + 20

def draw_vision_panel(draw, x, y):
    """THE VISION - Terminal output style"""
    padding = 40

    # Panel label (terminal style)
    draw.text((x + padding, y + padding),
             "> CORE_PHILOSOPHY.txt",
             fill=PHOSPHOR_GREEN, font=get_font(20, mono=True))

    # Quote in retro terminal style
    quote_y = y + padding + 60
    draw.text((x + padding, quote_y),
             "YOU ARE A",
             fill=TEXT_WHITE, font=get_font(40))

    quote_y += 50
    draw.text((x + padding, quote_y),
             "RESEARCHER",
             fill=PHOSPHOR_GREEN, font=get_font(48))

    quote_y += 60
    draw.text((x + padding, quote_y),
             "of your own",
             fill=TEXT_GRAY, font=get_font(28))

    quote_y += 40
    draw.text((x + padding, quote_y),
             "THOUGHTS",
             fill=PHOSPHOR_GREEN, font=get_font(48))

    # Terminal cursor
    draw.text((x + padding + 220, quote_y + 10),
             "█", fill=PHOSPHOR_GREEN, font=get_font(40))

    # Bottom text
    quote_y += 100
    draw.text((x + padding, quote_y),
             "Arkify documents thinking,",
             fill=TEXT_GRAY, font=get_font(18, mono=True))
    draw.text((x + padding, quote_y + 25),
             "not just results",
             fill=TEXT_GRAY, font=get_font(18, mono=True))

def draw_data_panel(draw, x, y):
    """THE DATA - Terminal statistics readout"""
    padding = 40

    # Panel label
    draw.text((x + padding, y + padding),
             "> SYSTEM_STATS.log",
             fill=PHOSPHOR_GREEN, font=get_font(20, mono=True))

    stat_y = y + padding + 80

    # Big number display (terminal LED style)
    draw.text((x + padding, stat_y),
             "59",
             fill=PHOSPHOR_GREEN, font=get_font(120, mono=True))
    draw.text((x + padding + 180, stat_y + 80),
             "COMMITS",
             fill=TEXT_GRAY, font=get_font(24, mono=True))

    stat_y += 150
    draw.text((x + padding, stat_y),
             "17",
             fill=FAIL_RED, font=get_font(100, mono=True))
    draw.text((x + padding + 150, stat_y + 70),
             "FAILS",
             fill=TEXT_GRAY, font=get_font(24, mono=True))

    stat_y += 130
    draw.text((x + padding, stat_y),
             "100%",
             fill=SUCCESS_GREEN, font=get_font(80, mono=True))
    draw.text((x + padding + 220, stat_y + 60),
             "REAL",
             fill=TEXT_GRAY, font=get_font(24, mono=True))

def draw_decision_panel(draw, x, y):
    """DECISION PATH - Terminal command history"""
    padding = 30

    # Panel label
    draw.text((x + padding, y + padding),
             "> git log --oneline icons/",
             fill=PHOSPHOR_GREEN, font=get_font(18, mono=True))

    # Decision tree as terminal output
    cmd_y = y + padding + 60
    tries = [
        ("TRY 1", "Colored boxes", "❌", FAIL_RED),
        ("TRY 2", "Download PNGs", "❌", FAIL_RED),
        ("TRY 3", "SimpleIcons CDN", "❌", FAIL_RED),
        ("TRY 4", "cairosvg", "✓", SUCCESS_GREEN),
    ]

    for i, (label, method, result, color) in enumerate(tries):
        # Terminal-style commit hash
        draw.text((x + padding, cmd_y),
                 f"{label}",
                 fill=PHOSPHOR_DIM, font=get_font(16, mono=True))

        draw.text((x + padding + 100, cmd_y),
                 method,
                 fill=TEXT_WHITE, font=get_font(16, mono=True))

        draw.text((x + PANEL_WIDTH - 100, cmd_y),
                 result,
                 fill=color, font=get_font(32))

        cmd_y += 55

    # Success message
    cmd_y += 20
    draw.text((x + padding, cmd_y),
             "> SUCCESS: 4 iterations",
             fill=SUCCESS_GREEN, font=get_font(18, mono=True))

def draw_autonomy_panel(draw, x, y):
    """AGENT AUTONOMY - Terminal process monitor"""
    padding = 30

    # Panel label
    draw.text((x + padding, y + padding),
             "> ps aux | grep agents",
             fill=PHOSPHOR_GREEN, font=get_font(18, mono=True))

    # Process list style
    proc_y = y + padding + 60
    agents = [
        ("HeaderAgent", 20, FAIL_RED),
        ("TimelineAgent", 50, AMBER),
        ("LearningAgent", 80, SUCCESS_GREEN),
    ]

    for name, percent, color in agents:
        # Process name
        draw.text((x + padding, proc_y),
                 name,
                 fill=TEXT_WHITE, font=get_font(20, mono=True))

        # CPU bar (autonomy level)
        bar_x = x + padding + 220
        bar_width = 200
        bar_fill = int(bar_width * percent / 100)

        # Background bar
        draw.rectangle([(bar_x, proc_y + 8), (bar_x + bar_width, proc_y + 28)],
                      outline=PHOSPHOR_DIM, width=1)

        # Filled portion
        draw.rectangle([(bar_x, proc_y + 8), (bar_x + bar_fill, proc_y + 28)],
                      fill=color)

        # Percentage
        draw.text((bar_x + bar_width + 20, proc_y),
                 f"{percent}%",
                 fill=color, font=get_font(20, mono=True))

        proc_y += 70

    # Footer
    proc_y += 30
    draw.text((x + padding, proc_y),
             "↑ Creative Freedom Range",
             fill=TEXT_GRAY, font=get_font(16, mono=True))

def draw_failures_panel(draw, x, y):
    """FAILURES = DATA - Terminal error log"""
    padding = 40

    # Panel label
    draw.text((x + padding, y + padding),
             "> ERROR_ANALYSIS.txt",
             fill=FAIL_RED, font=get_font(20, mono=True))

    # Big percentage
    fail_y = y + padding + 100
    draw.text((x + padding, fail_y),
             "28.8%",
             fill=FAIL_RED, font=get_font(110, mono=True))

    # Progress bar (terminal style)
    bar_y = fail_y + 140
    bar_width = PANEL_WIDTH - 2*padding
    bar_fill = int(bar_width * 0.288)

    # Background
    draw.rectangle([(x + padding, bar_y), (x + padding + bar_width, bar_y + 40)],
                  outline=PHOSPHOR_DIM, width=2)

    # Filled portion
    draw.rectangle([(x + padding, bar_y), (x + padding + bar_fill, bar_y + 40)],
                  fill=FAIL_RED)

    # Text below
    text_y = bar_y + 70
    draw.text((x + padding, text_y),
             "17/59 commits = fails",
             fill=TEXT_GRAY, font=get_font(18, mono=True))

    text_y += 35
    draw.text((x + padding, text_y),
             "Every fail is data",
             fill=PHOSPHOR_GREEN, font=get_font(20, mono=True))

    text_y += 35
    draw.text((x + padding, text_y),
             "Mistakes = Research",
             fill=PHOSPHOR_GREEN, font=get_font(20, mono=True))

def draw_meta_panel(draw, x, y):
    """META RECURSION - Self-referential terminal"""
    padding = 40

    # Panel label
    draw.text((x + padding, y + padding),
             "> RECURSION_LEVEL.sh",
             fill=PHOSPHOR_GREEN, font=get_font(20, mono=True))

    # Infinity symbol (big)
    meta_y = y + padding + 100
    draw.text((x + PANEL_WIDTH//2 - 60, meta_y),
             "∞",
             fill=PHOSPHOR_GREEN, font=get_font(140))

    # Meta message
    msg_y = meta_y + 170
    draw.text((x + padding, msg_y),
             "This image shows",
             fill=TEXT_WHITE, font=get_font(22, mono=True))

    msg_y += 35
    draw.text((x + padding, msg_y),
             "the decisions that",
             fill=TEXT_WHITE, font=get_font(22, mono=True))

    msg_y += 35
    draw.text((x + padding, msg_y),
             "created this image",
             fill=TEXT_WHITE, font=get_font(22, mono=True))

    # Terminal prompt
    msg_y += 60
    draw.text((x + padding, msg_y),
             "> _",
             fill=PHOSPHOR_GREEN, font=get_font(24, mono=True))

def main():
    """Generate the retro terminal aesthetic infographic"""
    # Create canvas
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DEEP)
    draw = ImageDraw.Draw(img)

    # Draw header
    header_bottom = draw_header(draw)

    # Panel positions (2x3 grid)
    panel_y_start = header_bottom + 40

    # Row 1
    draw_vision_panel(draw, 0, panel_y_start)
    draw_data_panel(draw, PANEL_WIDTH, panel_y_start)

    # Row 2
    draw_decision_panel(draw, 0, panel_y_start + PANEL_HEIGHT)
    draw_autonomy_panel(draw, PANEL_WIDTH, panel_y_start + PANEL_HEIGHT)

    # Row 3
    draw_failures_panel(draw, 0, panel_y_start + 2*PANEL_HEIGHT)
    draw_meta_panel(draw, PANEL_WIDTH, panel_y_start + 2*PANEL_HEIGHT)

    # Add CRT effects
    img = add_scanlines(img, intensity=0.15)
    img = add_glow(img)

    # Save
    output_path = "output/arkify-claude4.7-meta-v3-terminal.png"
    img.save(output_path, 'PNG', optimize=True)
    print(f"✓ Generated: {output_path}")
    print(f"  Size: {os.path.getsize(output_path) / 1024:.1f} KB")
    print(f"  Aesthetic: RETRO-FUTURISTIC TERMINAL ARCHAEOLOGY")
    print(f"  Distinctive features: Phosphor green CRT, scanlines, monospace, ASCII borders")

if __name__ == "__main__":
    main()
