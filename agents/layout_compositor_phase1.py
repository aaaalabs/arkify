"""
Layout Compositor Agent - Phase 1
3x3 grid with Future Dust palette

Simple, Lovable, Complete
"""

from pathlib import Path
from typing import Dict, Any
from PIL import Image, ImageDraw, ImageFont
import io


class LayoutCompositorPhase1:
    """
    Compose 3x3 grid layout with Future Dust palette.

    Canvas: 900x1200px (3 columns x 3 rows)
    Panels: 300x400px each
    Header: 900x400px (spans 3 columns)
    """

    def __init__(self):
        """Initialize with Future Dust design system."""

        # Canvas settings
        self.canvas_size = (900, 1200)  # 3x3 grid, 4:5 ratio
        self.panel_size = (300, 400)    # Each panel

        # Future Dust Palette (2025 Color of the Year)
        self.colors = {
            'future_dust': '#4A4E69',      # Primary (dark blue-purple-grey)
            'electric_green': '#06FFA5',    # Accent (neon)
            'cosmic_white': '#F2F4F8',      # Off-white
            'deep_space': '#22223B',        # Darker bg
            'expected_grey': '#6B7280',     # Dimmed (for expected)
            'text': '#F2F4F8',              # Off-white text
            'text_dim': '#9A8C98',          # Dimmed text
        }

        # Gradients
        self.gradient_bg = self.colors['deep_space']  # For now, solid color

        # Typography
        self.fonts = self._load_fonts()

    def compose(self, layout_data: Dict[str, Any], panel_order: list = None) -> Path:
        """
        Compose 3x3 grid layout.

        Args:
            layout_data: Complete project data
            panel_order: List of panel IDs to render (from Story Arc Designer)

        Returns:
            Path to generated PNG
        """

        # Create canvas with dark background
        canvas = Image.new('RGB', self.canvas_size, self.gradient_bg)
        draw = ImageDraw.Draw(canvas)

        # Default panel order if not provided
        if panel_order is None:
            panel_order = ['header', 'results', 'tech_stack',
                          'expected', 'reality', 'learning']

        # Draw panels based on order
        # Row 1: Header (spanning)
        self._draw_header_panel(canvas, draw, layout_data)

        # Row 2 & 3: Data panels
        # Map panel names to draw functions
        panel_renderers = {
            'results': self._draw_results_panel,
            'tech_stack': self._draw_tech_stack_panel,
            'expected': self._draw_expected_panel,
            'reality': self._draw_reality_panel,
            'learning': self._draw_learning_panel,
        }

        # Grid positions (excluding header which is row 0)
        grid_positions = [
            (0, 1), (1, 1), (2, 1),  # Row 2
            (0, 2), (1, 2), (2, 2),  # Row 3
        ]

        # Draw panels (skip 'header' from panel_order)
        data_panels = [p for p in panel_order if p != 'header']
        for panel_id, (col, row) in zip(data_panels, grid_positions):
            if panel_id in panel_renderers:
                x = col * self.panel_size[0]
                y = row * self.panel_size[1]
                panel_renderers[panel_id](canvas, draw, layout_data, x, y)

        # Save output
        output_dir = Path('output')
        output_dir.mkdir(exist_ok=True)

        project_name = layout_data['name'].lower().replace(' ', '-')
        output_path = output_dir / f"{project_name}-phase1.png"

        canvas.save(output_path, 'PNG', quality=95, optimize=True, dpi=(300, 300))

        return output_path

    def _draw_header_panel(self, canvas: Image, draw: ImageDraw, data: Dict):
        """Draw spanning header (900x400px)."""
        x, y = 0, 0
        w, h = 900, 400

        # Background (slightly lighter than canvas)
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['future_dust'])

        # Project name
        name = data['name']
        name_y = y + 80
        self._draw_text(draw, name, (w//2, name_y), self.fonts['huge'],
                       self.colors['cosmic_white'], align='center')

        # Tagline (if available)
        tagline = data.get('tagline', '')
        if tagline:
            tagline_y = name_y + 70
            self._draw_text(draw, tagline, (w//2, tagline_y), self.fonts['medium'],
                           self.colors['text_dim'], align='center')

        # Key stats (hours • cost • users)
        kpis = data.get('kpis', {})
        stats_y = y + h - 80

        hours = kpis.get('hours_display', f"{data.get('hours', 0)}h")
        cost = kpis.get('cost_display', f"€{data.get('cost', 0)}")

        # Get users from results if available
        users = ""
        if 'results' in data and 'users' in data['results']:
            users = f"{data['results']['users']} users"

        stats = [hours, cost]
        if users:
            stats.append(users)

        stats_text = " • ".join(stats)
        self._draw_text(draw, stats_text, (w//2, stats_y), self.fonts['medium'],
                       self.colors['electric_green'], align='center')

    def _draw_results_panel(self, canvas: Image, draw: ImageDraw, data: Dict, x: int, y: int):
        """Draw results panel."""
        w, h = self.panel_size

        # Background
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['deep_space'])

        # Title
        title_y = y + 40
        self._draw_text(draw, "RESULTS", (x + w//2, title_y), self.fonts['small_bold'],
                       self.colors['text_dim'], align='center')

        results = data.get('results', {})

        # Users (big number)
        users = results.get('users', 0)
        users_y = y + 120
        self._draw_text(draw, str(users), (x + w//2, users_y), self.fonts['huge'],
                       self.colors['electric_green'], align='center')
        self._draw_text(draw, "users", (x + w//2, users_y + 65), self.fonts['small'],
                       self.colors['text_dim'], align='center')

        # Revenue
        revenue = results.get('revenue', 0)
        rev_y = y + 260
        self._draw_text(draw, f"€{revenue}", (x + w//2, rev_y), self.fonts['large'],
                       self.colors['cosmic_white'], align='center')
        self._draw_text(draw, "revenue", (x + w//2, rev_y + 40), self.fonts['tiny'],
                       self.colors['text_dim'], align='center')

    def _draw_tech_stack_panel(self, canvas: Image, draw: ImageDraw, data: Dict, x: int, y: int):
        """Draw tech stack panel."""
        w, h = self.panel_size

        # Background
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['deep_space'])

        # Title
        title_y = y + 40
        self._draw_text(draw, "TECH STACK", (x + w//2, title_y), self.fonts['small_bold'],
                       self.colors['text_dim'], align='center')

        # Tech stack (max 4)
        tech_stack = data.get('tech_stack', [])[:4]

        # Draw as simple list
        start_y = y + 110
        spacing = 70

        for i, tech in enumerate(tech_stack):
            tech_y = start_y + i * spacing

            # Colored box
            box_size = 50
            box_x = x + (w - box_size) // 2
            draw.rectangle([box_x, tech_y, box_x + box_size, tech_y + box_size],
                          fill=self.colors['future_dust'])

            # Tech name
            name_y = tech_y + box_size + 10
            self._draw_text(draw, tech, (x + w//2, name_y), self.fonts['small'],
                           self.colors['cosmic_white'], align='center')

    def _draw_expected_panel(self, canvas: Image, draw: ImageDraw, data: Dict, x: int, y: int):
        """Draw expected panel (dimmed)."""
        w, h = self.panel_size

        # Background
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['deep_space'])

        # Title
        title_y = y + 40
        self._draw_text(draw, "EXPECTED", (x + w//2, title_y), self.fonts['small_bold'],
                       self.colors['expected_grey'], align='center')

        expectations = data.get('expectations', {})

        # Timeline
        timeline = expectations.get('timeline', 'N/A')
        timeline_y = y + 120
        self._draw_text(draw, timeline, (x + w//2, timeline_y), self.fonts['large'],
                       self.colors['expected_grey'], align='center')

        # Cost
        cost = expectations.get('cost', 0)
        cost_y = y + 220
        self._draw_text(draw, f"€{cost}", (x + w//2, cost_y), self.fonts['medium'],
                       self.colors['expected_grey'], align='center')

        # Bar (visual indicator)
        bar_y = y + 300
        bar_width = 100
        bar_x = x + (w - bar_width) // 2
        draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + 20],
                      fill=self.colors['expected_grey'])

    def _draw_reality_panel(self, canvas: Image, draw: ImageDraw, data: Dict, x: int, y: int):
        """Draw reality panel (vivid)."""
        w, h = self.panel_size

        # Background
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['deep_space'])

        # Title
        title_y = y + 40
        self._draw_text(draw, "REALITY", (x + w//2, title_y), self.fonts['small_bold'],
                       self.colors['electric_green'], align='center')

        reality = data.get('reality', {})

        # Timeline
        timeline = reality.get('timeline', 'N/A')
        timeline_y = y + 120
        self._draw_text(draw, timeline, (x + w//2, timeline_y), self.fonts['large'],
                       self.colors['electric_green'], align='center')

        # Cost
        cost = reality.get('cost', 0)
        cost_y = y + 220
        self._draw_text(draw, f"€{cost}", (x + w//2, cost_y), self.fonts['medium'],
                       self.colors['cosmic_white'], align='center')

        # Bar (longer than expected)
        bar_y = y + 300
        bar_width = 180  # Longer than expected
        bar_x = x + (w - bar_width) // 2
        draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + 20],
                      fill=self.colors['electric_green'])

    def _draw_learning_panel(self, canvas: Image, draw: ImageDraw, data: Dict, x: int, y: int):
        """Draw learning panel."""
        w, h = self.panel_size

        # Background (slightly lighter)
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['future_dust'])

        # Title
        title_y = y + 40
        self._draw_text(draw, "💡 LEARNED", (x + w//2, title_y), self.fonts['small_bold'],
                       self.colors['cosmic_white'], align='center')

        # Learning text (wrapped)
        learning = data.get('learning', '')
        learning_y = y + 120
        self._draw_wrapped_text(draw, learning, x + 30, learning_y, w - 60,
                               self.fonts['medium'], self.colors['cosmic_white'])

    # === Helper Methods ===

    def _draw_text(self, draw: ImageDraw, text: str, pos: tuple, font, color: str, align='left'):
        """Draw text with alignment."""
        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]

            x, y = pos
            if align == 'center':
                x -= text_width // 2
            elif align == 'right':
                x -= text_width

            draw.text((x, y), text, font=font, fill=color)
        except:
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
                line_width = len(line_text) * 8

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
        line_height = 30
        for i, line in enumerate(lines):
            draw.text((x, y + i * line_height), line, font=font, fill=color)

    def _load_fonts(self) -> Dict[str, ImageFont.FreeTypeFont]:
        """Load fonts."""
        font_sizes = {
            'tiny': 14,
            'small': 16,
            'small_bold': 16,
            'medium': 22,
            'large': 36,
            'huge': 56
        }

        fonts = {}
        for name, size in font_sizes.items():
            try:
                # Try system fonts
                fonts[name] = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
            except:
                fonts[name] = ImageFont.load_default()

        return fonts
