"""
Layout Compositor Agent
Phase 0: 2x2 grid static PNG generator

Creates a simple but professional 2x2 grid layout:
┌────────────┬────────────┐
│ Panel 1:   │ Panel 2:   │
│ Header +   │ Tech Stack │
│ Stats      │ (4 logos)  │
├────────────┼────────────┤
│ Panel 3:   │ Panel 4:   │
│ Time/Cost  │ Key        │
│ Chart      │ Learning   │
└────────────┴────────────┘
"""

from pathlib import Path
from typing import Dict, Any
from PIL import Image, ImageDraw, ImageFont, ImageColor
import io


class LayoutCompositor:
    """
    Compose final 2x2 grid layout.

    Phase 0: Static PNG only
    Phase 3: Add animation support
    Phase 6: Multi-platform outputs
    """

    def __init__(self):
        """Initialize compositor with design system."""

        # Canvas settings
        self.canvas_size = (800, 800)  # Square for now
        self.panel_size = (400, 400)   # Each panel is 400x400

        # Design system (indie hacker purple gradient theme)
        self.colors = {
            'background': '#f8f9fa',      # Light gray background
            'panel_bg': '#ffffff',         # White panels
            'primary': '#667eea',          # Purple
            'secondary': '#764ba2',        # Darker purple
            'text': '#1a202c',             # Near black
            'text_light': '#718096',       # Gray
            'accent': '#43e97b',           # Green for positive metrics
            'border': '#e2e8f0',           # Light border
        }

        # Typography (using default fonts for now)
        self.fonts = self._load_fonts()

    def compose(self, layout_data: Dict[str, Any]) -> Path:
        """
        Compose 2x2 grid layout.

        Args:
            layout_data: Data for all 4 panels

        Returns:
            Path to generated PNG file
        """
        # Create canvas
        canvas = Image.new('RGB', self.canvas_size, self.colors['background'])
        draw = ImageDraw.Draw(canvas)

        # Draw 4 panels
        self._draw_panel_1(canvas, draw, layout_data)  # Top-left: Header + Stats
        self._draw_panel_2(canvas, draw, layout_data)  # Top-right: Tech Stack
        self._draw_panel_3(canvas, draw, layout_data)  # Bottom-left: Time/Cost
        self._draw_panel_4(canvas, draw, layout_data)  # Bottom-right: Learning

        # Save output
        output_dir = Path('output')
        output_dir.mkdir(exist_ok=True)

        # Sanitize filename
        project_name = layout_data['name'].lower().replace(' ', '-')
        output_path = output_dir / f"{project_name}.png"

        canvas.save(output_path, 'PNG', quality=95, optimize=True)

        return output_path

    def _draw_panel_1(self, canvas: Image, draw: ImageDraw, data: Dict):
        """Draw Panel 1: Project Header + Key Stats."""
        x, y = 0, 0
        w, h = self.panel_size

        # Panel background
        self._draw_panel_background(draw, x, y, w, h)

        # Project name (large, bold)
        name = data['name']
        name_y = y + 60
        self._draw_text(draw, name, (x + w//2, name_y), self.fonts['large_bold'],
                       self.colors['text'], align='center')

        # Tagline (if available)
        if data.get('tagline'):
            tagline_y = name_y + 50
            self._draw_text(draw, data['tagline'], (x + w//2, tagline_y),
                           self.fonts['small'], self.colors['text_light'], align='center')

        # Key stats (hours and cost)
        kpis = data['kpis']
        stats_y = y + 200

        hours_text = kpis['hours_display']
        cost_text = kpis['cost_display']

        self._draw_stat_box(draw, x + 50, stats_y, hours_text, "Time", w - 100)
        self._draw_stat_box(draw, x + 50, stats_y + 100, cost_text, "Cost", w - 100)

    def _draw_panel_2(self, canvas: Image, draw: ImageDraw, data: Dict):
        """Draw Panel 2: Tech Stack Icons."""
        x, y = self.panel_size[0], 0
        w, h = self.panel_size

        # Panel background
        self._draw_panel_background(draw, x, y, w, h)

        # Title
        title_y = y + 60
        self._draw_text(draw, "Tech Stack", (x + w//2, title_y), self.fonts['medium_bold'],
                       self.colors['text'], align='center')

        # Load and draw icons in 2x2 grid
        icons = data.get('icons', [])[:4]  # Max 4 icons

        icon_size = 80
        grid_spacing = 100
        grid_start_x = x + (w - 2 * grid_spacing) // 2
        grid_start_y = y + 150

        for i, icon in enumerate(icons):
            row = i // 2
            col = i % 2

            icon_x = grid_start_x + col * grid_spacing
            icon_y = grid_start_y + row * grid_spacing

            self._draw_icon(canvas, icon, icon_x, icon_y, icon_size)

            # Icon label
            label_y = icon_y + icon_size + 15
            self._draw_text(draw, icon['name'], (icon_x + icon_size//2, label_y),
                           self.fonts['tiny'], self.colors['text_light'], align='center')

    def _draw_panel_3(self, canvas: Image, draw: ImageDraw, data: Dict):
        """Draw Panel 3: Project Architecture Stats."""
        x, y = 0, self.panel_size[1]
        w, h = self.panel_size

        # Panel background
        self._draw_panel_background(draw, x, y, w, h)

        # Title
        title_y = y + 40
        self._draw_text(draw, "Project Structure", (x + w//2, title_y), self.fonts['medium_bold'],
                       self.colors['text'], align='center')

        # Architecture metrics (from extended.results and git_stats in YAML)
        kpis = data.get('kpis', {})

        # Get architecture stats with fallbacks
        agents = kpis.get('agents_created', '?')
        files = kpis.get('files_created', '?')
        loc = kpis.get('lines_of_code', '?')
        commits = kpis.get('total_commits', '?')
        gen_time = kpis.get('generation_time', '?')

        # Format lines of code with thousands separator
        if isinstance(loc, int):
            loc_display = f"{loc:,}"
        else:
            loc_display = str(loc)

        # Draw metrics in a clean list
        metrics_start_y = y + 120
        line_height = 45

        metrics = [
            f"🤖  {agents} Agents",
            f"📄  {files} Files",
            f"📝  {loc_display} Lines",
            f"📦  {commits} Commits",
            f"⚡  {gen_time} Gen Time"
        ]

        for i, metric in enumerate(metrics):
            metric_y = metrics_start_y + (i * line_height)
            self._draw_text(draw, metric, (x + 60, metric_y), self.fonts['medium'],
                           self.colors['text'], align='left')

    def _draw_panel_4(self, canvas: Image, draw: ImageDraw, data: Dict):
        """Draw Panel 4: Key Learning."""
        x, y = self.panel_size[0], self.panel_size[1]
        w, h = self.panel_size

        # Panel background
        self._draw_panel_background(draw, x, y, w, h)

        # Title
        title_y = y + 60
        self._draw_text(draw, "💡 Key Learning", (x + w//2, title_y), self.fonts['medium_bold'],
                       self.colors['text'], align='center')

        # Learning text (wrapped)
        learning = data['learning']
        learning_y = y + 150
        self._draw_wrapped_text(draw, learning, x + 40, learning_y, w - 80,
                               self.fonts['medium'], self.colors['text'])

    # === Helper Methods ===

    def _draw_panel_background(self, draw: ImageDraw, x: int, y: int, w: int, h: int):
        """Draw panel background with border."""
        # White background
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['panel_bg'])

        # Border
        border_width = 2
        draw.rectangle([x, y, x + w - border_width, y + h - border_width],
                      outline=self.colors['border'], width=border_width)

    def _draw_text(self, draw: ImageDraw, text: str, pos: tuple, font, color: str, align='left'):
        """Draw text with alignment."""
        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            x, y = pos
            if align == 'center':
                x -= text_width // 2
            elif align == 'right':
                x -= text_width

            draw.text((x, y), text, font=font, fill=color)
        except Exception as e:
            # Fallback to basic text if font rendering fails
            draw.text(pos, text, fill=color)

    def _draw_wrapped_text(self, draw: ImageDraw, text: str, x: int, y: int,
                          max_width: int, font, color: str):
        """Draw text with word wrapping."""
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            current_line.append(word)
            line_text = ' '.join(current_line)

            try:
                bbox = draw.textbbox((0, 0), line_text, font=font)
                line_width = bbox[2] - bbox[0]
            except:
                line_width = len(line_text) * 10  # Rough estimate

            if line_width > max_width:
                if len(current_line) > 1:
                    current_line.pop()
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(line_text)
                    current_line = []

        if current_line:
            lines.append(' '.join(current_line))

        # Draw lines
        line_height = 35
        for i, line in enumerate(lines):
            draw.text((x, y + i * line_height), line, font=font, fill=color)

    def _draw_stat_box(self, draw: ImageDraw, x: int, y: int, value: str, label: str, width: int):
        """Draw a stat box with value and label."""
        # Value (large)
        self._draw_text(draw, value, (x + width//2, y), self.fonts['large'],
                       self.colors['primary'], align='center')

        # Label (small, below)
        label_y = y + 40
        self._draw_text(draw, label, (x + width//2, label_y), self.fonts['small'],
                       self.colors['text_light'], align='center')

    def _draw_icon(self, canvas: Image, icon: Dict, x: int, y: int, size: int):
        """Draw technology icon."""
        try:
            # Load SVG as image (simplified - just use a colored box for MVP)
            # Phase 2 will add proper SVG rendering
            icon_img = Image.new('RGB', (size, size), self.colors['primary'])

            # Paste onto canvas
            canvas.paste(icon_img, (x, y))

        except Exception as e:
            # Fallback: draw colored box with initials
            draw = ImageDraw.Draw(canvas)
            draw.rectangle([x, y, x + size, y + size], fill=self.colors['primary'])

            initials = icon['name'][:2].upper()
            self._draw_text(draw, initials, (x + size//2, y + size//3),
                           self.fonts['medium_bold'], '#ffffff', align='center')

    def _load_fonts(self) -> Dict[str, ImageFont.FreeTypeFont]:
        """Load fonts for different sizes."""
        # Try to use system fonts, fallback to default
        font_sizes = {
            'tiny': 12,
            'small': 14,
            'medium': 18,
            'medium_bold': 18,
            'large': 28,
            'large_bold': 32,
            'huge': 48
        }

        fonts = {}
        for name, size in font_sizes.items():
            try:
                # Try to load system font
                if 'bold' in name:
                    fonts[name] = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
                else:
                    fonts[name] = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
            except:
                # Fallback to default font
                fonts[name] = ImageFont.load_default()

        return fonts
