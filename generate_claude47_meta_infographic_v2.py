#!/usr/bin/env python3
"""
Claude 4.7 Meta-Recursion Infographic Generator V2
MASSIVE typography improvements based on QA feedback
Canvas: 1200x1600px (Instagram 3:4 portrait ratio)
Real data only - no mock data
"""

from PIL import Image, ImageDraw, ImageFont
import os
import sys

# Add agents to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'agents'))

from gradient_renderer import GradientRenderer
from shape_decorator import ShapeDecorator


class Claude47MetaInfographicV2:
    """V2: Pixel-perfect with MASSIVE typography and visual hierarchy"""

    def __init__(self):
        # Design System: Future Dust 2025
        self.colors = {
            'bg_deep': '#0a0a0a',           # Deep black canvas
            'primary': '#4A4E69',           # Dark blue-purple-grey
            'accent': '#06FFA5',            # Electric neon green
            'text': '#F2F4F8',              # Cosmic white
            'fail': '#E63946',              # Fail red
            'success': '#06FFA5',           # Success green
            'grey': '#9A8C98',              # Neutral grey
            'panel_bg': '#1a1a1a',          # Panel background
        }

        # Real data from git analysis
        self.data = {
            'total_commits': 59,
            'fail_commits': 17,
            'fail_percentage': 28.8,        # 17/59 = 28.8%
            'icon_tries': [
                {'num': 1, 'approach': 'Colored\nboxes', 'result': 'fail'},
                {'num': 2, 'approach': 'Download\nPNGs', 'result': 'fail'},
                {'num': 3, 'approach': 'Simple\nIcons', 'result': 'fail'},
                {'num': 4, 'approach': 'cairo\nsvg', 'result': 'success'},
            ],
            'autonomy_levels': [
                {'name': 'Header', 'percent': 20, 'color': '#E63946'},
                {'name': 'Timeline', 'percent': 50, 'color': '#F4A261'},
                {'name': 'Learning', 'percent': 80, 'color': '#06FFA5'},
            ],
            'philosophy': '"You are a researcher\nof your own thoughts"',
            'meta_message': 'This image shows the\ndecisions that created\nthis image',
        }

        # Agents
        self.gradient = GradientRenderer()
        self.shapes = ShapeDecorator()

    def create_infographic(self):
        """Main generation method"""
        # Create canvas
        canvas = Image.new('RGB', (1200, 1600), self._hex_to_rgb(self.colors['bg_deep']))

        # Generate panels
        header = self._create_header_panel()
        vision = self._create_vision_panel()
        data = self._create_data_panel()
        decision = self._create_decision_panel()
        autonomy = self._create_autonomy_panel()
        failures = self._create_failures_panel()
        meta = self._create_meta_panel()

        # Composite panels onto canvas
        canvas.paste(header, (0, 0))                    # Full width header
        canvas.paste(vision, (0, 300))                  # Left column
        canvas.paste(data, (600, 300))                  # Right column
        canvas.paste(decision, (0, 733))                # Left middle
        canvas.paste(autonomy, (600, 733))              # Right middle
        canvas.paste(failures, (0, 1166))               # Left bottom
        canvas.paste(meta, (600, 1166))                 # Right bottom

        return canvas

    def _create_header_panel(self):
        """Panel 1: MASSIVE header with electric green title"""
        img = Image.new('RGB', (1200, 300), self._hex_to_rgb(self.colors['panel_bg']))

        # Add subtle gradient
        gradient = self.gradient.create_linear_gradient(
            1200, 300,
            '#1a1a1a', '#0a0a0a',
            direction='vertical'
        )
        img.paste(gradient, (0, 0))

        draw = ImageDraw.Draw(img)

        # Load fonts - MUCH BIGGER
        font_massive = self._get_font(96)   # 72 → 96
        font_large = self._get_font(48)     # 36 → 48
        font_small = self._get_font(24)     # 20 → 24

        # Main title - ELECTRIC GREEN, MASSIVE
        title = "Built with Claude 4.7"
        bbox = draw.textbbox((0, 0), title, font=font_massive)
        title_width = bbox[2] - bbox[0]
        x = (1200 - title_width) // 2
        # Text shadow for depth
        draw.text((x + 2, 52), title, fill='#000000', font=font_massive)
        draw.text((x, 50), title, fill=self._hex_to_rgb(self.colors['accent']), font=font_massive)

        # Subtitle with infinity symbol
        subtitle = "∞ Meta-Recursion Achieved"
        bbox = draw.textbbox((0, 0), subtitle, font=font_large)
        subtitle_width = bbox[2] - bbox[0]
        draw.text(
            ((1200 - subtitle_width) // 2, 165),
            subtitle,
            fill=self._hex_to_rgb(self.colors['text']),
            font=font_large
        )

        # Tagline - bigger and bolder
        tagline = "Arkify analyzed its own 59 commits to create this visualization"
        bbox = draw.textbbox((0, 0), tagline, font=font_small)
        tagline_width = bbox[2] - bbox[0]
        draw.text(
            ((1200 - tagline_width) // 2, 235),
            tagline,
            fill=self._hex_to_rgb(self.colors['grey']),
            font=font_small
        )

        return img

    def _create_vision_panel(self):
        """Panel 2: CENTERED quote with MASSIVE text"""
        img = Image.new('RGB', (600, 433), self._hex_to_rgb(self.colors['panel_bg']))

        # Gradient background
        gradient = self.gradient.create_preset_gradient(600, 433, 'meta', 'diagonal-tl-br')
        img.paste(gradient, (0, 0))

        # Semi-transparent overlay
        overlay = Image.new('RGBA', (600, 433), (10, 10, 10, 180))
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

        draw = ImageDraw.Draw(img)

        font_title = self._get_font(28)     # 24 → 28
        font_quote = self._get_font(40)     # 32 → 40 BIGGER
        font_body = self._get_font(22)      # 16 → 22

        # Title
        draw.text((60, 40), "THE VISION", fill=self._hex_to_rgb(self.colors['accent']), font=font_title)

        # Philosophy quote (centered, multiline) - BIGGER
        lines = self.data['philosophy'].strip('"').split('\n')
        y = 130
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font_quote)
            line_width = bbox[2] - bbox[0]
            x = (600 - line_width) // 2
            # Text shadow for readability
            draw.text((x + 1, y + 1), line, fill='#000000', font=font_quote)
            draw.text((x, y), line, fill=self._hex_to_rgb(self.colors['text']), font=font_quote)
            y += 55

        # Bottom tagline - bigger
        tagline = "Arkify documents thinking, not just results"
        bbox = draw.textbbox((0, 0), tagline, font=font_body)
        tagline_width = bbox[2] - bbox[0]
        draw.text(
            ((600 - tagline_width) // 2, 360),
            tagline,
            fill=self._hex_to_rgb(self.colors['grey']),
            font=font_body
        )

        return img

    def _create_data_panel(self):
        """Panel 3: HUGE numbers with clear hierarchy"""
        img = Image.new('RGB', (600, 433), self._hex_to_rgb(self.colors['panel_bg']))
        draw = ImageDraw.Draw(img)

        font_title = self._get_font(28)     # 24 → 28
        font_massive = self._get_font(120)  # 96 → 120 MASSIVE
        font_label = self._get_font(24)     # 18 → 24
        font_small = self._get_font(20)     # 14 → 20

        # Title
        draw.text((60, 40), "THE DATA", fill=self._hex_to_rgb(self.colors['accent']), font=font_title)

        # Stats (3 MASSIVE numbers)
        stats = [
            (str(self.data['total_commits']), "Total Commits", 90),
            (str(self.data['fail_commits']), "Documented Fails", 220),
            ("100%", "Real Data", 350),
        ]

        for value, label, y in stats:
            # MASSIVE number with shadow
            bbox = draw.textbbox((0, 0), value, font=font_massive)
            num_width = bbox[2] - bbox[0]
            x = (600 - num_width) // 2
            draw.text((x + 2, y + 2), value, fill='#000000', font=font_massive)
            draw.text((x, y), value, fill=self._hex_to_rgb(self.colors['accent']), font=font_massive)

            # Label - bigger
            bbox = draw.textbbox((0, 0), label, font=font_label)
            label_width = bbox[2] - bbox[0]
            draw.text(
                ((600 - label_width) // 2, y + 100),
                label,
                fill=self._hex_to_rgb(self.colors['text']),
                font=font_label
            )

        return img

    def _create_decision_panel(self):
        """Panel 4: BIGGER boxes with CLEAR labels"""
        img = Image.new('RGB', (600, 433), self._hex_to_rgb(self.colors['panel_bg']))
        draw = ImageDraw.Draw(img)

        font_title = self._get_font(28)     # 24 → 28
        font_label = self._get_font(20)     # 16 → 20
        font_try = self._get_font(18)       # New - for TRY labels
        font_icon = self._get_font(48)      # 40 → 48 BIGGER EMOJI
        font_small = self._get_font(16)

        # Title
        draw.text((60, 40), "DECISION PATH", fill=self._hex_to_rgb(self.colors['accent']), font=font_title)
        draw.text((60, 75), "Icon Rendering: 4 Tries", fill=self._hex_to_rgb(self.colors['text']), font=font_label)

        # Draw 4 tries horizontally - BIGGER BOXES
        y = 140
        box_width = 130     # 120 → 130
        box_height = 160    # 150 → 160
        spacing = 10

        for i, attempt in enumerate(self.data['icon_tries']):
            x = 30 + i * (box_width + spacing)

            # Box color
            color = self.colors['success'] if attempt['result'] == 'success' else self.colors['fail']

            # Draw rounded box
            self.shapes.draw_rounded_rectangle(
                draw,
                [(x, y), (x + box_width, y + box_height)],
                fill=self._hex_to_rgb(color),
                radius=12
            )

            # Try number - BOLD and CLEAR
            draw.text((x + 10, y + 10), f"TRY {attempt['num']}", fill='#000000', font=font_try)

            # Icon (centered) - BIGGER
            icon = '✅' if attempt['result'] == 'success' else '❌'
            bbox = draw.textbbox((0, 0), icon, font=font_icon)
            icon_width = bbox[2] - bbox[0]
            draw.text(
                (x + (box_width - icon_width) // 2, y + 50),
                icon,
                fill='#000000',
                font=font_icon
            )

            # Approach (bottom, wrapped) - BIGGER
            approach_lines = attempt['approach'].split('\n')
            approach_y = y + 115
            for line in approach_lines[:2]:  # Max 2 lines
                bbox = draw.textbbox((0, 0), line, font=font_small)
                line_width = bbox[2] - bbox[0]
                draw.text(
                    (x + (box_width - line_width) // 2, approach_y),
                    line,
                    fill='#000000',
                    font=font_small
                )
                approach_y += 20

        # Bottom learning - bigger
        learning = "Real commits: 2729f2e → 4049175 = SUCCESS"
        draw.text((60, 360), learning, fill=self._hex_to_rgb(self.colors['grey']), font=font_label)

        return img

    def _create_autonomy_panel(self):
        """Panel 5: SIMPLIFIED 3-level spectrum"""
        img = Image.new('RGB', (600, 433), self._hex_to_rgb(self.colors['panel_bg']))
        draw = ImageDraw.Draw(img)

        font_title = self._get_font(28)     # 24 → 28
        font_huge = self._get_font(56)      # For percentages
        font_label = self._get_font(22)     # 16 → 22
        font_small = self._get_font(18)     # 14 → 18

        # Title
        draw.text((60, 40), "AGENT AUTONOMY", fill=self._hex_to_rgb(self.colors['accent']), font=font_title)

        # Simplified 3-level visualization
        y_start = 110
        level_height = 80
        spacing = 15

        for i, level in enumerate(self.data['autonomy_levels']):
            y = y_start + i * (level_height + spacing)
            bar_width = int((level['percent'] / 100) * 480)

            # Background bar
            draw.rectangle(
                [(60, y), (540, y + level_height)],
                fill=self._hex_to_rgb('#2a2a2a')
            )

            # Filled portion
            draw.rectangle(
                [(60, y), (60 + bar_width, y + level_height)],
                fill=self._hex_to_rgb(level['color'])
            )

            # Percentage - HUGE
            pct_text = f"{level['percent']}%"
            draw.text((75, y + 15), pct_text, fill='#000000', font=font_huge)

            # Label - CLEAR
            draw.text((75, y + 55), level['name'], fill='#000000', font=font_label)

        # Bottom insight - bigger
        insight = "Different agents need different levels of autonomy"
        draw.text((60, 380), insight, fill=self._hex_to_rgb(self.colors['grey']), font=font_small)

        return img

    def _create_failures_panel(self):
        """Panel 6: HUGE percentage with THICK bar"""
        img = Image.new('RGB', (600, 433), self._hex_to_rgb(self.colors['panel_bg']))
        draw = ImageDraw.Draw(img)

        font_title = self._get_font(28)     # 24 → 28
        font_massive = self._get_font(96)   # 72 → 96 MASSIVE
        font_label = self._get_font(24)     # 18 → 24
        font_small = self._get_font(20)     # 16 → 20

        # Title
        draw.text((60, 40), "FAILURES = DATA", fill=self._hex_to_rgb(self.colors['accent']), font=font_title)

        # MASSIVE percentage with shadow
        pct = f"{self.data['fail_percentage']:.1f}%"
        bbox = draw.textbbox((0, 0), pct, font=font_massive)
        pct_width = bbox[2] - bbox[0]
        x = (600 - pct_width) // 2
        draw.text((x + 2, 92), pct, fill='#000000', font=font_massive)
        draw.text((x, 90), pct, fill=self._hex_to_rgb(self.colors['fail']), font=font_massive)

        # Label - bigger
        label = "of commits documented fails"
        bbox = draw.textbbox((0, 0), label, font=font_label)
        label_width = bbox[2] - bbox[0]
        draw.text(
            ((600 - label_width) // 2, 190),
            label,
            fill=self._hex_to_rgb(self.colors['text']),
            font=font_label
        )

        # Progress bar - THICKER
        y = 250
        bar_width = 480
        bar_height = 50     # 30 → 50 THICK
        filled_width = int((self.data['fail_percentage'] / 100) * bar_width)

        # Empty bar
        draw.rectangle(
            [(60, y), (60 + bar_width, y + bar_height)],
            fill=self._hex_to_rgb('#2a2a2a')
        )

        # Filled portion
        draw.rectangle(
            [(60, y), (60 + filled_width, y + bar_height)],
            fill=self._hex_to_rgb(self.colors['fail'])
        )

        # Bottom messages - bigger
        messages = [
            "Every fail is a data point",
            "Mistakes = Research",
            "Git commits capture the truth",
        ]
        y_msg = 325
        for msg in messages:
            draw.text((60, y_msg), msg, fill=self._hex_to_rgb(self.colors['grey']), font=font_small)
            y_msg += 28

        return img

    def _create_meta_panel(self):
        """Panel 7: BIGGER text for readability"""
        img = Image.new('RGB', (600, 433), self._hex_to_rgb(self.colors['panel_bg']))

        # Gradient background (purple)
        gradient = self.gradient.create_preset_gradient(600, 433, 'meta', 'diagonal-tr-bl')
        img.paste(gradient, (0, 0))

        # Semi-transparent overlay
        overlay = Image.new('RGBA', (600, 433), (10, 10, 10, 180))
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

        draw = ImageDraw.Draw(img)

        font_title = self._get_font(28)     # 24 → 28
        font_huge = self._get_font(80)      # 64 → 80
        font_quote = self._get_font(28)     # 24 → 28 BIGGER
        font_small = self._get_font(18)     # 14 → 18

        # Title
        draw.text((60, 40), "META ∞ RECURSION", fill=self._hex_to_rgb(self.colors['accent']), font=font_title)

        # Infinity symbol (centered) - BIGGER
        bbox = draw.textbbox((0, 0), "∞", font=font_huge)
        symbol_width = bbox[2] - bbox[0]
        x = (600 - symbol_width) // 2
        draw.text((x + 2, 102), "∞", fill='#000000', font=font_huge)
        draw.text((x, 100), "∞", fill=self._hex_to_rgb(self.colors['accent']), font=font_huge)

        # Meta message (centered, multiline) - BIGGER
        lines = self.data['meta_message'].split('\n')
        y = 220
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font_quote)
            line_width = bbox[2] - bbox[0]
            x = (600 - line_width) // 2
            # Text shadow
            draw.text((x + 1, y + 1), line, fill='#000000', font=font_quote)
            draw.text((x, y), line, fill=self._hex_to_rgb(self.colors['text']), font=font_quote)
            y += 38

        # Bottom tagline - bigger
        tagline = "Claude 4.7 analyzed all 59 commits at once"
        bbox = draw.textbbox((0, 0), tagline, font=font_small)
        tagline_width = bbox[2] - bbox[0]
        draw.text(
            ((600 - tagline_width) // 2, 370),
            tagline,
            fill=self._hex_to_rgb(self.colors['grey']),
            font=font_small
        )

        return img

    def _get_font(self, size):
        """Load font with fallback"""
        try:
            return ImageFont.truetype('/System/Library/Fonts/SFNS.ttf', size)
        except Exception as e:
            print(f"Warning: Could not load SFNS.ttf (size {size}): {e}")
            return ImageFont.load_default()

    def _hex_to_rgb(self, hex_color):
        """Convert hex to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def main():
    """Generate the V2 infographic"""
    print("🎨 Generating Claude 4.7 Meta-Recursion Infographic V2...")
    print("   Canvas: 1200x1600px (Instagram 3:4 portrait)")
    print("   Design: Future Dust 2025")
    print("   Updates: MASSIVE typography, clear hierarchy")
    print("   Data: Real git history (59 commits, 17 fails)")
    print()

    generator = Claude47MetaInfographicV2()
    infographic = generator.create_infographic()

    # Save output
    output_path = 'output/arkify-claude4.7-meta-v2.png'
    os.makedirs('output', exist_ok=True)
    infographic.save(output_path, optimize=True, quality=95)

    # File size
    file_size_kb = os.path.getsize(output_path) / 1024

    print(f"✅ Generated: {output_path}")
    print(f"   Size: {file_size_kb:.1f} KB")
    print(f"   Dimensions: 1200x1600px")
    print()
    print("📊 V2 Improvements:")
    print("   ✅ Header: 96px bold electric green")
    print("   ✅ Numbers: 120px MASSIVE")
    print("   ✅ Decision boxes: Bigger with clear labels")
    print("   ✅ Autonomy: Simplified 3-level view")
    print("   ✅ Failures: 50px thick progress bar")
    print("   ✅ Meta: Bigger text (28px) for readability")
    print()
    print("🚀 Ready to dominate on:")
    print("   - LinkedIn (optimal format)")
    print("   - Twitter/X (portrait format)")
    print("   - Instagram (3:4 aspect ratio)")


if __name__ == '__main__':
    main()
