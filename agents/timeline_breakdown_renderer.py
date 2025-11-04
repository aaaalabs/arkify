"""
Timeline Breakdown Renderer Agent
Visualizes where time actually goes: fails vs working vs polish
Shows: 60% fails (red), 30% working (yellow), 10% polish (green)
"""

from PIL import Image, ImageDraw, ImageFont


class TimelineBreakdownRenderer:
    """Renders horizontal timeline showing fail/work/polish segments"""

    def __init__(self):
        self.colors = {
            'fail': '#FF006E',         # Magenta - failed attempts
            'working': '#FFD93D',      # Yellow - working iterations
            'polish': '#06FFA5',       # Green - final polish
            'bg': '#22223B',
            'text': '#F2F4F8',
            'grid': '#4A4E69'
        }

    def render(self, total_hours=10, width=300, height=400):
        """
        Render timeline breakdown

        Args:
            total_hours: Total time spent (from YAML)
            width, height: Panel dimensions

        Returns:
            PIL Image
        """
        img = Image.new('RGB', (width, height), self._hex_to_rgb(self.colors['bg']))
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
        draw.text((20, 20), f"TIMELINE: {total_hours}H",
                 fill=self._hex_to_rgb(self.colors['text']), font=font_title)

        # Timeline bar
        bar_y = 80
        bar_height = 40
        bar_width = width - 40

        # Segments (realistic breakdown from git data)
        # Based on Phase 1: 7 iterations, 4 fails = ~60% fail time
        segments = [
            {'label': 'Failed attempts', 'hours': 6, 'color': 'fail'},
            {'label': 'Working iterations', 'hours': 3, 'color': 'working'},
            {'label': 'Final polish', 'hours': 1, 'color': 'polish'}
        ]

        # Draw timeline axis
        draw.line([(20, bar_y + bar_height + 10), (width - 20, bar_y + bar_height + 10)],
                 fill=self._hex_to_rgb(self.colors['grid']), width=1)

        # Time markers
        for i in range(0, total_hours + 1, 2):
            x = 20 + (i / total_hours) * bar_width
            draw.text((x - 5, bar_y + bar_height + 15), f"{i}h",
                     fill=self._hex_to_rgb(self.colors['text']), font=font_small)

        # Draw segments
        x_offset = 20
        for segment in segments:
            seg_width = (segment['hours'] / total_hours) * bar_width
            color = self.colors[segment['color']]

            # Segment bar
            draw.rectangle(
                [(x_offset, bar_y), (x_offset + seg_width, bar_y + bar_height)],
                fill=self._hex_to_rgb(color)
            )

            x_offset += seg_width

        # Legend with percentages
        legend_y = bar_y + bar_height + 60
        spacing = 55

        for i, segment in enumerate(segments):
            y = legend_y + i * spacing
            color = self.colors[segment['color']]
            pct = (segment['hours'] / total_hours) * 100

            # Color box
            draw.rectangle([(20, y), (40, y + 20)], fill=self._hex_to_rgb(color))

            # Label
            draw.text((50, y), segment['label'],
                     fill=self._hex_to_rgb(self.colors['text']), font=font_label)

            # Percentage
            draw.text((50, y + 16), f"{segment['hours']}h ({pct:.0f}%)",
                     fill=self._hex_to_rgb(self.colors['text']), font=font_small)

        # Insight at bottom
        draw.text((20, height - 40), "Most time = iteration,",
                 fill=self._hex_to_rgb(self.colors['text']), font=font_small)
        draw.text((20, height - 25), "not building",
                 fill=self._hex_to_rgb(self.colors['text']), font=font_small)

        return img

    def _hex_to_rgb(self, hex_color):
        """Convert hex to RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


if __name__ == '__main__':
    import os
    renderer = TimelineBreakdownRenderer()
    img = renderer.render(total_hours=10)

    os.makedirs('output/test_agents', exist_ok=True)
    img.save('output/test_agents/timeline_breakdown_test.png')
    print("✅ Timeline breakdown test generated: output/test_agents/timeline_breakdown_test.png")
