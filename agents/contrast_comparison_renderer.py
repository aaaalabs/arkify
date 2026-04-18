"""
Contrast Comparison Renderer Agent
Visualizes before/after contrast improvements
Shows: Side-by-side comparison with actual visual difference
"""

from PIL import Image, ImageDraw, ImageFont


class ContrastComparisonRenderer:
    """Renders before/after contrast comparison with visual demonstration"""

    def __init__(self):
        # Before colors (low contrast)
        self.before = {
            'bg': '#4A4E69',        # Medium grey
            'text': '#6B7280',      # Light grey (low contrast)
            'ratio': '2:1'
        }

        # After colors (high contrast)
        self.after = {
            'bg': '#22223B',        # Dark navy
            'text': '#F2F4F8',      # Off-white (high contrast)
            'ratio': '7.12:1'
        }

        self.header_bg = '#1A1A1A'
        self.divider = '#9A8C98'

    def render(self, width=300, height=400):
        """
        Render contrast comparison

        Args:
            width, height: Panel dimensions

        Returns:
            PIL Image
        """
        img = Image.new('RGB', (width, height), self._hex_to_rgb(self.header_bg))
        draw = ImageDraw.Draw(img)

        # Load fonts
        try:
            font_title = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 20)
            font_large = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 32)
            font_label = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 14)
            font_small = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 12)
        except:
            font_title = ImageFont.load_default()
            font_large = ImageFont.load_default()
            font_label = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # Title
        draw.text((20, 20), "CONTRAST JOURNEY", fill='#FFFFFF', font=font_title)

        # Split into two halves
        split_y = 80
        half_width = width // 2
        content_height = height - split_y

        # BEFORE (left half)
        before_x = 0
        draw.rectangle(
            [(before_x, split_y), (half_width - 1, height)],
            fill=self._hex_to_rgb(self.before['bg'])
        )

        # Before label
        draw.text((before_x + 20, split_y + 20), "BEFORE",
                 fill=self._hex_to_rgb(self.before['text']), font=font_label)

        # Before demo text (hard to read)
        demo_y = split_y + 60
        draw.text((before_x + 20, demo_y), "Sample",
                 fill=self._hex_to_rgb(self.before['text']), font=font_large)
        draw.text((before_x + 20, demo_y + 40), "Text",
                 fill=self._hex_to_rgb(self.before['text']), font=font_large)

        # Contrast ratio
        draw.text((before_x + 20, height - 80), self.before['ratio'],
                 fill=self._hex_to_rgb(self.before['text']), font=font_large)
        draw.text((before_x + 20, height - 50), "FAIL",
                 fill='#FF006E', font=font_label)
        draw.text((before_x + 20, height - 30), "Barely visible",
                 fill=self._hex_to_rgb(self.before['text']), font=font_small)

        # AFTER (right half)
        after_x = half_width + 1
        draw.rectangle(
            [(after_x, split_y), (width, height)],
            fill=self._hex_to_rgb(self.after['bg'])
        )

        # After label
        draw.text((after_x + 20, split_y + 20), "AFTER",
                 fill=self._hex_to_rgb(self.after['text']), font=font_label)

        # After demo text (clear)
        draw.text((after_x + 20, demo_y), "Sample",
                 fill=self._hex_to_rgb(self.after['text']), font=font_large)
        draw.text((after_x + 20, demo_y + 40), "Text",
                 fill=self._hex_to_rgb(self.after['text']), font=font_large)

        # Contrast ratio
        draw.text((after_x + 20, height - 80), self.after['ratio'],
                 fill=self._hex_to_rgb(self.after['text']), font=font_large)
        draw.text((after_x + 20, height - 50), "WCAG AA",
                 fill='#06FFA5', font=font_label)
        draw.text((after_x + 20, height - 30), "Crystal clear",
                 fill=self._hex_to_rgb(self.after['text']), font=font_small)

        # Vertical divider
        draw.line([(half_width, split_y), (half_width, height)],
                 fill=self._hex_to_rgb(self.divider), width=2)

        return img

    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


if __name__ == '__main__':
    # Test
    import os
    renderer = ContrastComparisonRenderer()

    img = renderer.render()

    os.makedirs('output/test_agents', exist_ok=True)
    img.save('output/test_agents/contrast_comparison_test.png')
    print("✅ Contrast comparison test generated: output/test_agents/contrast_comparison_test.png")
