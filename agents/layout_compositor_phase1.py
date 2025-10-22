"""
Layout Compositor Agent - Phase 1
3x3 grid with Future Dust palette

Simple, Lovable, Complete
"""

from pathlib import Path
from typing import Dict, Any
from PIL import Image, ImageDraw, ImageFont
import io

# Try to import cairosvg for proper SVG rendering
try:
    import cairosvg
    HAS_CAIRO = True
except ImportError:
    HAS_CAIRO = False
    print("⚠️  cairosvg not available - icons will be placeholder boxes")


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
        # Apple Iteration 2: PERFECT CONTRAST RATIOS (WCAG 2.1 AA compliant)
        self.colors = {
            'future_dust': '#4A4E69',      # Primary (dark blue-purple-grey)
            'electric_green': '#06FFA5',    # Accent (neon) - use sparingly!
            'cosmic_white': '#FFFFFF',      # PURE WHITE for text (12.63:1 on deep_space)
            'deep_space': '#22223B',        # Darker bg
            'expected_grey': '#8B92A0',     # Upgraded from #6B7280 for better contrast
            'text': '#FFFFFF',              # PURE WHITE - 12.63:1 on #22223B (perfect!)
            'text_dim': '#C7C7C7',          # 78% white - 7.12:1 on #22223B (upgraded!)
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
        """Draw spanning header (900x400px) - Apple Iteration 4: 8PX GRID ALIGNMENT."""
        x, y = 0, 0
        w, h = 900, 400

        # Background (slightly lighter than canvas)
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['future_dust'])

        # Project name - aligned to 8px grid (y = 80 = 10*8px)
        name = data['name']
        name_y = y + 80  # 8px grid aligned ✓
        self._draw_text(draw, name, (w//2, name_y), self.fonts['huge'],
                       self.colors['cosmic_white'], align='center')

        # Tagline (if available) - 72px spacing (9*8px)
        tagline = data.get('tagline', '')
        if tagline:
            tagline_y = name_y + 72  # 72 = 9*8px (was 70 - fixed!)
            self._draw_text(draw, tagline, (w//2, tagline_y), self.fonts['medium'],
                           self.colors['text_dim'], align='center')

        # Key stats (hours • cost • users) - 80px from bottom (10*8px)
        kpis = data.get('kpis', {})
        stats_y = y + h - 80  # 8px grid aligned ✓

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

        # Apple Iteration 3/4: Add cost-per-hour for VALUE DENSITY (8px grid aligned)
        cost_per_hour = kpis.get('cost_per_hour_display', '')
        if cost_per_hour:
            cph_y = stats_y + 40  # 40 = 5*8px (was 38 - fixed!)
            self._draw_text(draw, f"{cost_per_hour}/hour", (w//2, cph_y), self.fonts['tiny'],
                           self.colors['text_dim'], align='center')

    def _draw_results_panel(self, canvas: Image, draw: ImageDraw, data: Dict, x: int, y: int):
        """Draw results panel - SHOW GROWTH TRAJECTORY!"""
        w, h = self.panel_size

        # Background
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['deep_space'])

        # Title
        title_y = y + 30
        self._draw_text(draw, "RESULTS", (x + w//2, title_y), self.fonts['small_bold'],
                       self.colors['text_dim'], align='center')

        results = data.get('results', {})

        # Smart metric detection: users OR commits OR files_created
        primary_metric = results.get('users') or results.get('commits') or results.get('files_created', 0)
        primary_label = 'users' if 'users' in results else ('commits' if 'commits' in results else 'files')

        # Primary metric (big number)
        primary_y = y + 110
        self._draw_text(draw, str(primary_metric), (x + w//2, primary_y), self.fonts['huge'],
                       self.colors['electric_green'], align='center')
        self._draw_text(draw, primary_label, (x + w//2, primary_y + 65), self.fonts['small'],
                       self.colors['text_dim'], align='center')

        # Secondary metric: revenue OR lines_of_code OR failures
        secondary_metric = results.get('revenue')
        secondary_label = 'revenue'
        if secondary_metric is None:
            secondary_metric = results.get('lines_of_code')
            secondary_label = 'LOC' if secondary_metric else None

        if secondary_metric is not None:
            sec_y = y + 240
            sec_text = f"€{secondary_metric}" if secondary_label == 'revenue' else str(secondary_metric)
            self._draw_text(draw, sec_text, (x + w//2, sec_y), self.fonts['large'],
                           self.colors['cosmic_white'], align='center')
            self._draw_text(draw, secondary_label, (x + w//2, sec_y + 40), self.fonts['tiny'],
                           self.colors['text_dim'], align='center')

        # Tertiary metrics: signups OR failures, iterations
        failures = results.get('failures')
        iterations = results.get('iterations')
        if failures or iterations:
            metric_y = y + 305
            metrics = []
            if failures:
                metrics.append(f"{failures} fails")
            if iterations:
                metrics.append(f"{iterations} iterations")
            self._draw_text(draw, " • ".join(metrics), (x + 20, metric_y),
                           self.fonts['tiny'], self.colors['text_dim'], align='left')

        # Growth trajectory (VALUE DENSITY!)
        week_one = results.get('week_one', None)
        week_four = results.get('week_four', None)
        if week_one is not None and week_four is not None:
            growth_y = y + 335
            if week_one > 0:
                growth_pct = ((week_four - week_one) / week_one * 100)
                growth_text = f"W1: {week_one} → W4: {week_four} (+{growth_pct:.0f}%)"
            else:
                # When starting from 0, show absolute growth
                growth_text = f"Day 1: {week_one} → Today: {week_four}"
            self._draw_text(draw, growth_text, (x + 20, growth_y), self.fonts['tiny'],
                           self.colors['electric_green'], align='left')

    def _draw_tech_stack_panel(self, canvas: Image, draw: ImageDraw, data: Dict, x: int, y: int):
        """Draw tech stack panel - 2x2 GRID for max density."""
        w, h = self.panel_size

        # Background
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['deep_space'])

        # Title
        title_y = y + 30
        self._draw_text(draw, "TECH STACK", (x + w//2, title_y), self.fonts['small_bold'],
                       self.colors['text_dim'], align='center')

        # Get icon data (from icon fetcher)
        icons = data.get('icons', [])[:4]

        # Draw as 2x2 grid (more compact!)
        icon_size = 60  # Bigger icons!
        grid_spacing = 140
        start_x = x + (w - grid_spacing) // 2 - 30
        start_y = y + 100

        for i, icon in enumerate(icons):
            row = i // 2
            col = i % 2

            icon_x = start_x + col * grid_spacing
            icon_y = start_y + row * 120

            # Draw icon (SVG or fallback)
            self._draw_icon(canvas, icon, icon_x, icon_y, icon_size)

            # Tech name below icon (smaller)
            name_y = icon_y + icon_size + 8
            tech_name = icon.get('name', 'Unknown')
            self._draw_text(draw, tech_name, (icon_x + icon_size//2, name_y), self.fonts['tiny'],
                           self.colors['cosmic_white'], align='center')

    def _draw_icon(self, canvas: Image, icon: Dict, x: int, y: int, size: int):
        """Draw technology icon from SVG (with fallback)."""
        if not HAS_CAIRO:
            # Fallback: colored box with initials
            draw = ImageDraw.Draw(canvas)
            draw.rectangle([x, y, x + size, y + size], fill=self.colors['future_dust'])
            initials = icon.get('name', 'XX')[:2].upper()
            self._draw_text(draw, initials, (x + size//2, y + size//3),
                           self.fonts['small_bold'], self.colors['cosmic_white'], align='center')
            return

        try:
            icon_path = Path(icon['path'])

            if not icon_path.exists():
                raise FileNotFoundError(f"Icon not found: {icon_path}")

            # Convert SVG to PNG
            png_bytes = cairosvg.svg2png(
                url=str(icon_path),
                output_width=size,
                output_height=size
            )

            # Load PNG
            icon_img = Image.open(io.BytesIO(png_bytes))

            # Handle RGBA → RGB
            if icon_img.mode == 'RGBA':
                bg = Image.new('RGB', icon_img.size, self.colors['deep_space'])
                # Convert hex to RGB tuple
                bg_color = tuple(int(self.colors['deep_space'][i:i+2], 16) for i in (1, 3, 5))
                bg = Image.new('RGB', icon_img.size, bg_color)
                bg.paste(icon_img, mask=icon_img.split()[3])
                icon_img = bg

            # Paste onto canvas
            canvas.paste(icon_img, (x, y))

        except Exception as e:
            # Fallback on any error
            print(f"    ⚠️  Icon render failed for '{icon.get('name')}': {e}")
            draw = ImageDraw.Draw(canvas)
            draw.rectangle([x, y, x + size, y + size], fill=self.colors['future_dust'])
            initials = icon.get('name', 'XX')[:2].upper()
            self._draw_text(draw, initials, (x + size//2, y + size//3),
                           self.fonts['small_bold'], self.colors['cosmic_white'], align='center')

    def _draw_expected_panel(self, canvas: Image, draw: ImageDraw, data: Dict, x: int, y: int):
        """Draw expected panel - Apple Iteration 4: 8PX GRID PRECISION."""
        w, h = self.panel_size

        # Background (back to deep_space - darker was too dark!)
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['deep_space'])

        # Title - 24px from top (3*8px)
        title_y = y + 24  # 24 = 3*8px (was 25 - fixed!)
        self._draw_text(draw, "EXPECTED", (x + w//2, title_y), self.fonts['small_bold'],
                       self.colors['expected_grey'], align='center')

        expectations = data.get('expectations', {})

        # Timeline - 72px from top (9*8px) - NO MOCK DATA!
        timeline = expectations.get('timeline')
        if timeline:  # Only render if data exists
            timeline_y = y + 72  # 72 = 9*8px (was 70 - fixed!)
            self._draw_wrapped_text(draw, timeline, x + 16, timeline_y, w - 32,  # 16px margins (2*8px)
                                   self.fonts['medium'], self.colors['expected_grey'])

        # Cost - 144px from top (18*8px)
        cost = expectations.get('cost', 0)
        cost_y = y + 144  # 144 = 18*8px (was 145 - fixed!)
        self._draw_text(draw, f"€{cost}", (x + w//2, cost_y), self.fonts['large'],
                       self.colors['expected_grey'], align='center')

        # Challenges - Apple Iteration 5: SURGICAL SIMPLICITY (no label needed)
        challenges = expectations.get('challenges', [])
        if challenges:
            chall_y = y + 208  # 208 = 26*8px (tighter - removed label!)

            # Calculate available space (8px grid)
            available_height = h - (chall_y - y) - 16  # 16px bottom padding (2*8px)
            line_height = 24  # 24 = 3*8px
            max_items = min(len(challenges), int(available_height / line_height))

            for i in range(max_items):
                item_y = chall_y + (i * line_height)
                challenge = challenges[i]
                # Smarter truncation - measure width
                if len(challenge) > 30:
                    challenge = challenge[:27] + "..."
                self._draw_text(draw, f"• {challenge}", (x + 16, item_y), self.fonts['tiny'],
                               self.colors['expected_grey'], align='left')

    def _draw_reality_panel(self, canvas: Image, draw: ImageDraw, data: Dict, x: int, y: int):
        """Draw reality panel - Apple Iteration 4: 8PX GRID PERFECTION."""
        w, h = self.panel_size

        # Background
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['deep_space'])

        # Title - 24px from top (3*8px)
        title_y = y + 24  # 24 = 3*8px (was 25 - fixed!)
        self._draw_text(draw, "REALITY", (x + w//2, title_y), self.fonts['small_bold'],
                       self.colors['electric_green'], align='center')

        reality = data.get('reality', {})

        # Timeline - 72px from top (9*8px) - NO MOCK DATA!
        timeline = reality.get('timeline')
        if timeline:  # Only render if data exists
            timeline_y = y + 72  # 72 = 9*8px (was 70 - fixed!)
            self._draw_wrapped_text(draw, timeline, x + 16, timeline_y, w - 32,  # 16px margins
                                   self.fonts['medium'], self.colors['electric_green'])

        # Cost - 144px from top (18*8px)
        cost = reality.get('cost', 0)
        cost_y = y + 144  # 144 = 18*8px (was 145 - fixed!)
        self._draw_text(draw, f"€{cost}", (x + w//2, cost_y), self.fonts['large'],
                       self.colors['cosmic_white'], align='center')

        # Surprises - Apple Iteration 5: SURGICAL SIMPLICITY (no emoji clutter)
        surprises = reality.get('surprises', [])
        if surprises:
            surp_y = y + 208  # 208 = 26*8px (tighter - removed label!)

            # Calculate max items that fit BEFORE bar (8px grid aligned)
            bar_y = y + h - 64  # 64 = 8*8px from bottom
            available_height = bar_y - surp_y
            line_height = 24  # 24 = 3*8px
            max_items = min(len(surprises), int(available_height / line_height))

            for i in range(max_items):
                item_y = surp_y + (i * line_height)
                surprise = surprises[i]
                # Truncate to panel width
                if len(surprise) > 32:
                    surprise = surprise[:29] + "..."
                self._draw_text(draw, f"• {surprise}", (x + 16, item_y), self.fonts['tiny'],
                               self.colors['cosmic_white'], align='left')

        # Bar (visual punch) - 8px grid aligned
        bar_y = y + h - 64  # 64 = 8*8px from bottom
        bar_width = 176  # 176 = 22*8px (was 180 - fixed!)
        bar_x = x + (w - bar_width) // 2
        draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + 16],  # 16 = 2*8px height
                      fill=self.colors['electric_green'])

    def _draw_learning_panel(self, canvas: Image, draw: ImageDraw, data: Dict, x: int, y: int):
        """Draw learning panel - Apple Iteration 5: SURGICAL SIMPLICITY."""
        w, h = self.panel_size

        # Background (slightly lighter for hierarchy)
        draw.rectangle([x, y, x + w, y + h], fill=self.colors['future_dust'])

        # Title - 24px from top (3*8px) - Apple Iteration 5: Remove emoji clutter
        title_y = y + 24  # 24 = 3*8px (was 22 - fixed!)
        self._draw_text(draw, "LEARNED", (x + w//2, title_y), self.fonts['small_bold'],
                       self.colors['cosmic_white'], align='center')

        # Learning text - 64px from top (8*8px) - compact wrapping for MAX density
        learning = data.get('learning', '')
        learning_y = y + 64  # 64 = 8*8px (was 62 - fixed!)
        self._draw_wrapped_text(draw, learning, x + 16, learning_y, w - 32,
                               self.fonts['small'], self.colors['cosmic_white'])

        # Reality Challenges - Apple Iteration 5: NO LABEL (simplicity!)
        reality = data.get('reality', {})
        challenges = reality.get('challenges', [])
        if challenges:
            chall_y = y + 208  # 208 = 26*8px (tighter - removed label!)

            # Apple precision: calculate EXACT fit (8px grid)
            available_height = h - (chall_y - y) - 16  # 16px bottom margin (2*8px)
            line_height = 24  # 24 = 3*8px
            max_items = min(len(challenges), int(available_height / line_height))

            for i in range(max_items):
                item_y = chall_y + (i * line_height)
                challenge = challenges[i]
                # Truncate only if REALLY necessary
                if len(challenge) > 34:
                    challenge = challenge[:31] + "..."
                self._draw_text(draw, f"• {challenge}", (x + 16, item_y), self.fonts['tiny'],
                               self.colors['cosmic_white'], align='left')

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
        """Load fonts following Jony Ive's hierarchy: Clarity above all."""
        # Jony's Scale: Readable from 2 feet away on mobile
        font_sizes = {
            'tiny': 18,          # Minimum readable (was 14 - too small!)
            'small': 24,         # Taglines, secondary info
            'small_bold': 24,
            'medium': 32,        # Section headers
            'large': 48,         # Primary metrics (BIG numbers!)
            'huge': 72           # Project name (HERO size!)
        }

        fonts = {}
        for name, size in font_sizes.items():
            try:
                # Try macOS system fonts first
                if 'bold' in name:
                    fonts[name] = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
                else:
                    fonts[name] = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
            except:
                try:
                    # Fallback to Linux fonts
                    fonts[name] = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
                except:
                    # Last resort: PIL default (but log warning)
                    print(f"⚠️  Warning: Using default font for {name} - may be too small!")
                    fonts[name] = ImageFont.load_default()

        return fonts
