"""
Meta-Recursion Renderer Agent
Visualizes the moment of understanding what Arkify actually is.
This panel documents itself being created.

Real data from: This conversation, Oct 26 2025, 05:30-06:00
"""

from PIL import Image, ImageDraw, ImageFont


class MetaRecursionRenderer:
    """
    Renders the meta-moment:
    'Oh, Arkify isn't documentation. It's self-research.'

    This agent documents the realization that led to its own creation.
    Infinite recursion as a feature.
    """

    def __init__(self):
        self.colors = {
            'bg': '#0A0A0A',           # Pure black
            'iteration1': '#4A4E69',   # Grey (misunderstanding)
            'iteration2': '#3B82F6',   # Blue (getting closer)
            'iteration3': '#06FFA5',   # Green (realization)
            'iteration4': '#FFD93D',   # Gold (meta-realization)
            'text': '#F2F4F8',
            'dim': '#6B7280'
        }

    def render(self, width=300, height=400):
        """
        Render the meta-learning journey

        Timeline:
        05:30 - Build Phase 2 with mock data
        05:40 - User: "Never use mock data"
        05:45 - Fix: Extract real git data
        05:50 - User: "The mistake IS research"
        05:55 - Realize: "Oh. THAT'S what Arkify is."
        06:00 - Build THIS panel documenting the realization

        This is the panel.
        You're reading it.
        It documents itself.
        """
        img = Image.new('RGB', (width, height), self._hex_to_rgb(self.colors['bg']))
        draw = ImageDraw.Draw(img)

        try:
            font_title = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 22)
            font_big = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 48)  # For infinity symbol
            font_label = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 14)
            font_small = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 11)
        except:
            font_title = ImageFont.load_default()
            font_big = ImageFont.load_default()
            font_label = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # Title
        draw.text((20, 20), "META-LEARNING", fill=self._hex_to_rgb(self.colors['text']), font=font_title)

        # BIG INFINITY SYMBOL (visual anchor)
        draw.text((width // 2 - 30, 60), "∞", fill=self._hex_to_rgb(self.colors['iteration4']), font=font_big)

        # Simplified timeline - just 3 KEY moments
        y = 130
        line_h = 55

        # Moment 1: The Mistake
        draw.text((20, y), "1. Built with mock data",
                 fill=self._hex_to_rgb(self.colors['iteration1']), font=font_label)
        draw.text((20, y + 18), "User: ❌ Never use mock",
                 fill=self._hex_to_rgb(self.colors['text']), font=font_small)

        # Arrow
        draw.text((35, y + 38), "↓", fill=self._hex_to_rgb(self.colors['dim']), font=font_label)

        # Moment 2: The Realization
        y2 = y + line_h
        draw.text((20, y2), "2. Mistake IS research",
                 fill=self._hex_to_rgb(self.colors['iteration3']), font=font_label)
        draw.text((20, y2 + 18), "Failures = Features",
                 fill=self._hex_to_rgb(self.colors['text']), font=font_small)

        # Arrow
        draw.text((35, y2 + 38), "↓", fill=self._hex_to_rgb(self.colors['dim']), font=font_label)

        # Moment 3: The Meta-Insight (THIS PANEL)
        y3 = y2 + line_h
        draw.rectangle([(20, y3), (width - 20, y3 + 60)],
                      outline=self._hex_to_rgb(self.colors['iteration4']), width=2)

        draw.text((30, y3 + 10), "3. This panel →",
                 fill=self._hex_to_rgb(self.colors['iteration4']), font=font_label)
        draw.text((30, y3 + 28), "documents itself",
                 fill=self._hex_to_rgb(self.colors['text']), font=font_label)
        draw.text((30, y3 + 44), "being created",
                 fill=self._hex_to_rgb(self.colors['text']), font=font_small)

        return img

    def _hex_to_rgb(self, hex_color):
        """Convert hex to RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


if __name__ == '__main__':
    import os

    # Build panel about building panels about thinking
    renderer = MetaRecursionRenderer()
    img = renderer.render()

    os.makedirs('output/test_agents', exist_ok=True)
    img.save('output/test_agents/meta_recursion_test.png')

    print("✅ Meta-recursion panel generated")
    print("   This panel documents the realization that led to its creation")
    print("   Timestamp: Oct 26 2025, 05:30-06:00")
    print("   Meta-level: ∞")
    print("")
    print("   The panel shows:")
    print("   - 05:30: Built with mock data (mistake)")
    print("   - 05:40: Corrected with real data")
    print("   - 05:50: Realized mistakes ARE research")
    print("   - 05:55: Realized Arkify = self-research")
    print("   - 06:00: Building THIS panel about the realization")
    print("")
    print("   Every layer documents the layer below it.")
    print("   Infinite recursion as a feature, not a bug.")
