"""
Decision Path Renderer Agent
Visualizes decision journeys with multiple attempts (fails → success)
Shows: TRY 1 ❌ → TRY 2 ❌ → TRY 3 ❌ → TRY 4 ✅
"""

from PIL import Image, ImageDraw, ImageFont
import os


class DecisionPathRenderer:
    """Renders decision paths with visual progress showing fails and success"""

    def __init__(self):
        self.colors = {
            'fail': '#FF006E',      # Neon magenta
            'success': '#06FFA5',   # Neon green
            'bg_dark': '#22223B',   # Dark navy
            'text': '#F2F4F8',      # Off-white
            'arrow': '#9A8C98'      # Grey
        }

    def render(self, decision_data, width=300, height=400):
        """
        Render decision path visualization

        Args:
            decision_data: {
                'name': str,
                'attempts': [
                    {'approach': str, 'result': str, 'time': str},
                    ...
                ]
            }
            width, height: Panel dimensions

        Returns:
            PIL Image
        """
        img = Image.new('RGB', (width, height), self._hex_to_rgb(self.colors['bg_dark']))
        draw = ImageDraw.Draw(img)

        # Load fonts
        try:
            font_title = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 20)
            font_label = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 14)
            font_small = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 11)
        except:
            font_title = ImageFont.load_default()
            font_label = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # Title
        title = decision_data.get('name', 'DECISION PATH').upper()
        draw.text((20, 20), title, fill=self._hex_to_rgb(self.colors['text']), font=font_title)

        # Draw attempts (max 4)
        attempts = decision_data.get('attempts', [])[:4]
        y_start = 80
        box_height = 60
        spacing = 15

        for i, attempt in enumerate(attempts):
            y = y_start + i * (box_height + spacing)

            # Determine if success or fail
            is_success = 'SUCCESS' in attempt.get('result', '').upper() or '✅' in attempt.get('result', '')
            bg_color = self.colors['success'] if is_success else self.colors['fail']

            # Draw attempt box
            draw.rectangle(
                [(20, y), (width - 20, y + box_height)],
                fill=self._hex_to_rgb(bg_color),
                outline=None
            )

            # Try number
            try_text = f"TRY {i+1}"
            draw.text((30, y + 8), try_text, fill='#000000', font=font_label)

            # Approach
            approach = attempt.get('approach', '')[:25]  # Truncate
            draw.text((30, y + 25), approach, fill='#000000', font=font_small)

            # Result icon
            icon = '✅' if is_success else '❌'
            draw.text((width - 50, y + 15), icon, fill='#000000', font=font_title)

            # Time
            time = attempt.get('time', '')
            draw.text((30, y + 42), time, fill='#00000088', font=font_small)

            # Arrow to next (if not last)
            if i < len(attempts) - 1:
                arrow_y = y + box_height + spacing // 2
                draw.text((width // 2 - 10, arrow_y - 8), '→',
                         fill=self._hex_to_rgb(self.colors['arrow']), font=font_title)

        # Bottom summary
        total_time = decision_data.get('learning', 'See decision journey')
        draw.text((20, height - 40), total_time,
                 fill=self._hex_to_rgb(self.colors['text']), font=font_small)

        return img

    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


if __name__ == '__main__':
    # Test
    renderer = DecisionPathRenderer()

    test_data = {
        'name': 'Real Icons: 4 Tries',
        'attempts': [
            {'approach': 'Colored PIL boxes', 'result': 'FAIL - Too ugly', 'time': '30min'},
            {'approach': 'Download PNGs', 'result': 'FAIL - Not scalable', 'time': '1h'},
            {'approach': 'SimpleIcons CDN', 'result': 'FAIL - No SVG', 'time': '2h'},
            {'approach': 'cairosvg', 'result': 'SUCCESS ✅', 'time': '1h'}
        ],
        'learning': '4.5h to solve icon rendering'
    }

    img = renderer.render(test_data)

    # Save test output
    os.makedirs('output/test_agents', exist_ok=True)
    img.save('output/test_agents/decision_path_test.png')
    print("✅ Decision path test generated: output/test_agents/decision_path_test.png")
