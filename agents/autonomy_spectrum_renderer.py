"""
Autonomy Spectrum Renderer Agent
Visualizes agent autonomy levels as horizontal bars
Shows: Which agents have what level of decision freedom
"""

from PIL import Image, ImageDraw, ImageFont


class AutonomySpectrumRenderer:
    """Renders horizontal bar chart showing agent autonomy levels"""

    def __init__(self):
        self.colors = {
            'low': '#6B7280',       # Grey (20-40%)
            'medium': '#3B82F6',    # Blue (50-60%)
            'high': '#06FFA5',      # Green (70-100%)
            'empty': '#1A1A1A',     # Dark for empty portion
            'bg_dark': '#22223B',   # Background
            'text': '#F2F4F8'       # Text
        }

    def render(self, agents_data, width=300, height=400):
        """
        Render autonomy spectrum bars

        Args:
            agents_data: [
                {'agent': 'Header Agent', 'autonomy': 40, 'why': 'Fixed structure'},
                ...
            ]
            width, height: Panel dimensions

        Returns:
            PIL Image
        """
        img = Image.new('RGB', (width, height), self._hex_to_rgb(self.colors['bg_dark']))
        draw = ImageDraw.Draw(img)

        # Load fonts
        try:
            font_title = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 20)
            font_label = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 12)
            font_small = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 10)
        except:
            font_title = ImageFont.load_default()
            font_label = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # Title
        draw.text((20, 20), "AGENT AUTONOMY", fill=self._hex_to_rgb(self.colors['text']), font=font_title)

        # Draw bars
        y_start = 70
        bar_height = 28
        spacing = 12
        bar_width = width - 100  # Leave space for percentage

        for i, agent in enumerate(agents_data[:6]):  # Max 6 agents
            y = y_start + i * (bar_height + spacing)

            # Agent name
            name = agent.get('agent', '').replace(' Agent', '')
            draw.text((20, y), name, fill=self._hex_to_rgb(self.colors['text']), font=font_label)

            # Bar background (empty portion)
            bar_x = 20
            bar_y = y + 16
            draw.rectangle(
                [(bar_x, bar_y), (bar_x + bar_width, bar_y + 12)],
                fill=self._hex_to_rgb(self.colors['empty'])
            )

            # Bar filled portion
            autonomy = agent.get('autonomy', 0)
            filled_width = int((autonomy / 100) * bar_width)

            # Color based on autonomy level
            if autonomy <= 40:
                bar_color = self.colors['low']
            elif autonomy <= 60:
                bar_color = self.colors['medium']
            else:
                bar_color = self.colors['high']

            draw.rectangle(
                [(bar_x, bar_y), (bar_x + filled_width, bar_y + 12)],
                fill=self._hex_to_rgb(bar_color)
            )

            # Percentage
            pct_text = f"{autonomy}%"
            draw.text((bar_x + bar_width + 10, bar_y - 2),
                     pct_text, fill=self._hex_to_rgb(self.colors['text']), font=font_label)

        # Legend at bottom
        legend_y = height - 80
        draw.text((20, legend_y), "LOW (20-40%): Rule-based decisions",
                 fill=self._hex_to_rgb(self.colors['low']), font=font_small)
        draw.text((20, legend_y + 15), "MED (50-60%): Pattern matching",
                 fill=self._hex_to_rgb(self.colors['medium']), font=font_small)
        draw.text((20, legend_y + 30), "HIGH (70-100%): Creative control",
                 fill=self._hex_to_rgb(self.colors['high']), font=font_small)

        return img

    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


if __name__ == '__main__':
    # Test
    import os
    renderer = AutonomySpectrumRenderer()

    test_data = [
        {'agent': 'Header Agent', 'autonomy': 40, 'why': 'Fixed structure'},
        {'agent': 'Results Agent', 'autonomy': 30, 'why': 'Numbers + rules'},
        {'agent': 'Tech Stack Agent', 'autonomy': 60, 'why': 'Icon + layout'},
        {'agent': 'Timeline Agent', 'autonomy': 50, 'why': 'Data viz'},
        {'agent': 'Reality Agent', 'autonomy': 80, 'why': 'Story control'},
        {'agent': 'Learning Agent', 'autonomy': 90, 'why': 'Pure creativity'}
    ]

    img = renderer.render(test_data)

    os.makedirs('output/test_agents', exist_ok=True)
    img.save('output/test_agents/autonomy_spectrum_test.png')
    print("✅ Autonomy spectrum test generated: output/test_agents/autonomy_spectrum_test.png")
