#!/usr/bin/env python3
"""
Claude 4.7 Meta-Recursion Infographic Generator
Creates stunning PNG showcasing Arkify's self-documenting journey
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


class Claude47MetaInfographic:
    """Generates pixel-perfect infographic showcasing Claude 4.7 capabilities"""

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
                {'num': 1, 'approach': 'Colored boxes', 'result': 'fail'},
                {'num': 2, 'approach': 'Download PNGs', 'result': 'fail'},
                {'num': 3, 'approach': 'SimpleIcons', 'result': 'fail'},
                {'num': 4, 'approach': 'cairosvg', 'result': 'success'},
            ],
            'autonomy_range': {'min': 20, 'max': 80},
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
        """Panel 1: Header - Built with Claude 4.7"""
        img = Image.new('RGB', (1200, 300), self._hex_to_rgb(self.colors['panel_bg']))

        # Add subtle gradient
        gradient = self.gradient.create_linear_gradient(
            1200, 300,
            '#1a1a1a', '#0a0a0a',
            direction='vertical'
        )
        img.paste(gradient, (0, 0))

        draw = ImageDraw.Draw(img)

        # Load fonts
        font_huge = self._get_font(72)
        font_large = self._get_font(36)
        font_small = self._get_font(20)

        # Main title
        title = "Built with Claude 4.7"
        bbox = draw.textbbox((0, 0), title, font=font_huge)
        title_width = bbox[2] - bbox[0]
        draw.text(
            ((1200 - title_width) // 2, 60),
            title,
            fill=self._hex_to_rgb(self.colors['accent']),
            font=font_huge
        )

        # Subtitle with infinity symbol
        subtitle = "∞ Meta-Recursion Achieved"
        bbox = draw.textbbox((0, 0), subtitle, font=font_large)
        subtitle_width = bbox[2] - bbox[0]
        draw.text(
            ((1200 - subtitle_width) // 2, 155),
            subtitle,
            fill=self._hex_to_rgb(self.colors['text']),
            font=font_large
        )

        # Tagline
        tagline = "Arkify analyzed its own 59 commits to create this visualization"
        bbox = draw.textbbox((0, 0), tagline, font=font_small)
        tagline_width = bbox[2] - bbox[0]
        draw.text(
            ((1200 - tagline_width) // 2, 220),
            tagline,
            fill=self._hex_to_rgb(self.colors['grey']),
            font=font_small
        )

        return img

    def _create_vision_panel(self):
        """Panel 2: The Vision - Philosophy"""
        img = Image.new('RGB', (600, 433), self._hex_to_rgb(self.colors['panel_bg']))

        # Gradient background
        gradient = self.gradient.create_preset_gradient(600, 433, 'meta', 'diagonal-tl-br')
        img.paste(gradient, (0, 0))

        # Semi-transparent overlay
        overlay = Image.new('RGBA', (600, 433), (10, 10, 10, 180))
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

        draw = ImageDraw.Draw(img)

        font_title = self._get_font(24)
        font_quote = self._get_font(32)
        font_body = self._get_font(16)

        # Title
        draw.text((30, 30), "THE VISION", fill=self._hex_to_rgb(self.colors['accent']), font=font_title)

        # Philosophy quote (centered, multiline)
        lines = self.data['philosophy'].strip('"').split('\n')
        y = 120
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font_quote)
            line_width = bbox[2] - bbox[0]
            draw.text(
                ((600 - line_width) // 2, y),
                line,
                fill=self._hex_to_rgb(self.colors['text']),
                font=font_quote
            )
            y += 50

        # Bottom tagline
        tagline = "Arkify documents thinking, not just results"
        bbox = draw.textbbox((0, 0), tagline, font=font_body)
        tagline_width = bbox[2] - bbox[0]
        draw.text(
            ((600 - tagline_width) // 2, 370),
            tagline,
            fill=self._hex_to_rgb(self.colors['grey']),
            font=font_body
        )

        return img

    def _create_data_panel(self):
        """Panel 3: The Data - Real Stats"""
        img = Image.new('RGB', (600, 433), self._hex_to_rgb(self.colors['panel_bg']))
        draw = ImageDraw.Draw(img)

        font_title = self._get_font(24)
        font_huge = self._get_font(96)
        font_label = self._get_font(18)
        font_small = self._get_font(14)

        # Title
        draw.text((30, 30), "THE DATA", fill=self._hex_to_rgb(self.colors['accent']), font=font_title)

        # Stats (3 big numbers)
        stats = [
            (str(self.data['total_commits']), "Total Commits", 100),
            (str(self.data['fail_commits']), "Documented Fails", 220),
            ("100%", "Real Data", 340),
        ]

        for value, label, y in stats:
            # Big number
            bbox = draw.textbbox((0, 0), value, font=font_huge)
            num_width = bbox[2] - bbox[0]
            draw.text(
                ((600 - num_width) // 2, y),
                value,
                fill=self._hex_to_rgb(self.colors['accent']),
                font=font_huge
            )

            # Label
            bbox = draw.textbbox((0, 0), label, font=font_label)
            label_width = bbox[2] - bbox[0]
            draw.text(
                ((600 - label_width) // 2, y + 85),
                label,
                fill=self._hex_to_rgb(self.colors['text']),
                font=font_label
            )

        return img

    def _create_decision_panel(self):
        """Panel 4: Decision Path - Icon Rendering Journey"""
        img = Image.new('RGB', (600, 433), self._hex_to_rgb(self.colors['panel_bg']))
        draw = ImageDraw.Draw(img)

        font_title = self._get_font(24)
        font_label = self._get_font(16)
        font_icon = self._get_font(40)

        # Title
        draw.text((30, 30), "DECISION PATH", fill=self._hex_to_rgb(self.colors['accent']), font=font_title)
        draw.text((30, 60), "Icon Rendering: 4 Tries", fill=self._hex_to_rgb(self.colors['text']), font=font_label)

        # Draw 4 tries horizontally
        y = 130
        box_width = 120
        box_height = 150
        spacing = 15

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

            # Try number
            draw.text((x + 10, y + 10), f"TRY {attempt['num']}", fill='#000000', font=font_label)

            # Icon (centered)
            icon = '✅' if attempt['result'] == 'success' else '❌'
            bbox = draw.textbbox((0, 0), icon, font=font_icon)
            icon_width = bbox[2] - bbox[0]
            draw.text(
                (x + (box_width - icon_width) // 2, y + 50),
                icon,
                fill='#000000',
                font=font_icon
            )

            # Approach (bottom, wrapped)
            approach_lines = self._wrap_text(attempt['approach'], 12)
            approach_y = y + 110
            for line in approach_lines[:2]:  # Max 2 lines
                bbox = draw.textbbox((0, 0), line, font=font_label)
                line_width = bbox[2] - bbox[0]
                draw.text(
                    (x + (box_width - line_width) // 2, approach_y),
                    line,
                    fill='#000000',
                    font=font_label
                )
                approach_y += 18

        # Bottom learning
        learning = "Real commits: 2729f2e → 4049175 → SUCCESS"
        draw.text((30, 350), learning, fill=self._hex_to_rgb(self.colors['grey']), font=font_label)

        return img

    def _create_autonomy_panel(self):
        """Panel 5: Autonomy Spectrum"""
        img = Image.new('RGB', (600, 433), self._hex_to_rgb(self.colors['panel_bg']))
        draw = ImageDraw.Draw(img)

        font_title = self._get_font(24)
        font_label = self._get_font(16)
        font_small = self._get_font(14)

        # Title
        draw.text((30, 30), "AGENT AUTONOMY", fill=self._hex_to_rgb(self.colors['accent']), font=font_title)

        # Spectrum visualization
        y = 100
        bar_width = 540
        bar_height = 60

        # Background bar
        draw.rectangle(
            [(30, y), (30 + bar_width, y + bar_height)],
            fill=self._hex_to_rgb('#2a2a2a')
        )

        # 20% marker (left side)
        x_20 = 30 + int(0.2 * bar_width)
        draw.rectangle(
            [(30, y), (x_20, y + bar_height)],
            fill=self._hex_to_rgb(self.colors['fail'])
        )
        draw.text((40, y + 20), "20%", fill='#000000', font=font_label)
        draw.text((40, y + 40), "Fixed", fill='#000000', font=font_small)

        # 80% marker (right side)
        x_80 = 30 + int(0.8 * bar_width)
        draw.rectangle(
            [(x_80, y), (30 + bar_width, y + bar_height)],
            fill=self._hex_to_rgb(self.colors['success'])
        )
        draw.text((x_80 + 10, y + 20), "80%", fill='#000000', font=font_label)
        draw.text((x_80 + 10, y + 40), "Creative", fill='#000000', font=font_small)

        # Arrow showing range
        self.shapes.draw_arrow(
            draw,
            (x_20, y + bar_height + 30),
            (x_80, y + bar_height + 30),
            self._hex_to_rgb(self.colors['accent']),
            width=4,
            arrow_size=15
        )

        # Range label
        draw.text((220, y + bar_height + 20), "Agent Freedom Range", fill=self._hex_to_rgb(self.colors['text']), font=font_label)

        # Explanation
        y_exp = 230
        explanations = [
            "20% - Header Agent: Fixed structure",
            "50% - Timeline Agent: Data visualization",
            "80% - Learning Agent: Full creative control",
        ]
        for exp in explanations:
            draw.text((30, y_exp), exp, fill=self._hex_to_rgb(self.colors['text']), font=font_small)
            y_exp += 30

        # Bottom insight
        insight = "Different agents need different levels of autonomy"
        draw.text((30, 380), insight, fill=self._hex_to_rgb(self.colors['grey']), font=font_small)

        return img

    def _create_failures_panel(self):
        """Panel 6: Failures as Features"""
        img = Image.new('RGB', (600, 433), self._hex_to_rgb(self.colors['panel_bg']))
        draw = ImageDraw.Draw(img)

        font_title = self._get_font(24)
        font_huge = self._get_font(72)
        font_label = self._get_font(18)
        font_small = self._get_font(16)

        # Title
        draw.text((30, 30), "FAILURES = DATA", fill=self._hex_to_rgb(self.colors['accent']), font=font_title)

        # Big percentage
        pct = f"{self.data['fail_percentage']:.1f}%"
        bbox = draw.textbbox((0, 0), pct, font=font_huge)
        pct_width = bbox[2] - bbox[0]
        draw.text(
            ((600 - pct_width) // 2, 100),
            pct,
            fill=self._hex_to_rgb(self.colors['fail']),
            font=font_huge
        )

        # Label
        label = "of commits documented fails"
        bbox = draw.textbbox((0, 0), label, font=font_label)
        label_width = bbox[2] - bbox[0]
        draw.text(
            ((600 - label_width) // 2, 185),
            label,
            fill=self._hex_to_rgb(self.colors['text']),
            font=font_label
        )

        # Progress bar visualization
        y = 250
        bar_width = 540
        bar_height = 30
        filled_width = int((self.data['fail_percentage'] / 100) * bar_width)

        # Empty bar
        draw.rectangle(
            [(30, y), (30 + bar_width, y + bar_height)],
            fill=self._hex_to_rgb('#2a2a2a')
        )

        # Filled portion
        draw.rectangle(
            [(30, y), (30 + filled_width, y + bar_height)],
            fill=self._hex_to_rgb(self.colors['fail'])
        )

        # Bottom message
        messages = [
            "Every fail is a data point",
            "Mistakes = Research",
            "Git commits capture the truth",
        ]
        y_msg = 310
        for msg in messages:
            draw.text((30, y_msg), msg, fill=self._hex_to_rgb(self.colors['grey']), font=font_small)
            y_msg += 30

        return img

    def _create_meta_panel(self):
        """Panel 7: Meta Recursion"""
        img = Image.new('RGB', (600, 433), self._hex_to_rgb(self.colors['panel_bg']))

        # Gradient background (purple)
        gradient = self.gradient.create_preset_gradient(600, 433, 'meta', 'diagonal-tr-bl')
        img.paste(gradient, (0, 0))

        # Semi-transparent overlay
        overlay = Image.new('RGBA', (600, 433), (10, 10, 10, 180))
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

        draw = ImageDraw.Draw(img)

        font_title = self._get_font(24)
        font_huge = self._get_font(64)
        font_quote = self._get_font(24)
        font_small = self._get_font(14)

        # Title
        draw.text((30, 30), "META ∞ RECURSION", fill=self._hex_to_rgb(self.colors['accent']), font=font_title)

        # Infinity symbol (centered)
        bbox = draw.textbbox((0, 0), "∞", font=font_huge)
        symbol_width = bbox[2] - bbox[0]
        draw.text(
            ((600 - symbol_width) // 2, 100),
            "∞",
            fill=self._hex_to_rgb(self.colors['accent']),
            font=font_huge
        )

        # Meta message (centered, multiline)
        lines = self.data['meta_message'].split('\n')
        y = 220
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font_quote)
            line_width = bbox[2] - bbox[0]
            draw.text(
                ((600 - line_width) // 2, y),
                line,
                fill=self._hex_to_rgb(self.colors['text']),
                font=font_quote
            )
            y += 35

        # Bottom tagline
        tagline = "Claude 4.7 analyzed all 59 commits at once"
        bbox = draw.textbbox((0, 0), tagline, font=font_small)
        tagline_width = bbox[2] - bbox[0]
        draw.text(
            ((600 - tagline_width) // 2, 380),
            tagline,
            fill=self._hex_to_rgb(self.colors['grey']),
            font=font_small
        )

        return img

    def _get_font(self, size):
        """Load font with fallback"""
        try:
            return ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', size)
        except:
            return ImageFont.load_default()

    def _hex_to_rgb(self, hex_color):
        """Convert hex to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def _wrap_text(self, text, max_chars):
        """Simple text wrapping"""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + 1 <= max_chars:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)

        if current_line:
            lines.append(' '.join(current_line))

        return lines


def main():
    """Generate the infographic"""
    print("🎨 Generating Claude 4.7 Meta-Recursion Infographic...")
    print("   Canvas: 1200x1600px (Instagram 3:4 portrait)")
    print("   Design: Future Dust 2025")
    print("   Data: Real git history (59 commits, 17 fails)")
    print()

    generator = Claude47MetaInfographic()
    infographic = generator.create_infographic()

    # Save output
    output_path = 'output/arkify-claude4.7-meta.png'
    os.makedirs('output', exist_ok=True)
    infographic.save(output_path, optimize=True, quality=95)

    # File size
    file_size_kb = os.path.getsize(output_path) / 1024

    print(f"✅ Generated: {output_path}")
    print(f"   Size: {file_size_kb:.1f} KB")
    print(f"   Dimensions: 1200x1600px")
    print()
    print("🚀 Ready to share on:")
    print("   - LinkedIn (optimal format)")
    print("   - Twitter/X (portrait format)")
    print("   - Instagram (3:4 aspect ratio)")
    print()
    print("💡 Key Message:")
    print("   'Claude 4.7 analyzed all 59 commits at once to create")
    print("   this visualization of Arkify building itself.'")
    print("   Meta-recursion level: ∞")


if __name__ == '__main__':
    main()
