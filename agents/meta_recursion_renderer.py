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
            font_title = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 18)
            font_label = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 11)
            font_tiny = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 9)
        except:
            font_title = ImageFont.load_default()
            font_label = ImageFont.load_default()
            font_tiny = ImageFont.load_default()

        # Title
        draw.text((20, 20), "META-LEARNING", fill=self._hex_to_rgb(self.colors['text']), font=font_title)
        draw.text((20, 38), "Oct 26, 05:30-06:00", fill=self._hex_to_rgb(self.colors['dim']), font=font_tiny)

        # Timeline with realizations
        y = 70
        line_h = 52

        # Iteration 1: Misunderstanding
        self._draw_iteration(draw, 20, y,
            "05:30", "Thought: Arkify = Documentation",
            "Built Phase 2 with mock data",
            self.colors['iteration1'], font_label, font_tiny)

        # Iteration 2: Correction
        self._draw_iteration(draw, 20, y + line_h,
            "05:40", "User: 'Never use mock data'",
            "Realized: Need real git commits",
            self.colors['iteration2'], font_label, font_tiny)

        # Iteration 3: First meta-insight
        self._draw_iteration(draw, 20, y + line_h * 2,
            "05:50", "User: 'Mistake IS research'",
            "Realized: Failures are features",
            self.colors['iteration3'], font_label, font_tiny)

        # Iteration 4: Full recursion
        self._draw_iteration(draw, 20, y + line_h * 3,
            "05:55", "User: 'You research yourself'",
            "Realized: Arkify = Self-research journal",
            self.colors['iteration4'], font_label, font_tiny)

        # Current moment (THIS)
        y_current = y + line_h * 4
        draw.rectangle([(20, y_current), (width - 20, y_current + 48)],
                      outline=self._hex_to_rgb(self.colors['iteration4']), width=2)

        draw.text((30, y_current + 8), "06:00 NOW",
                 fill=self._hex_to_rgb(self.colors['iteration4']), font=font_label)
        draw.text((30, y_current + 22), "Building panel about",
                 fill=self._hex_to_rgb(self.colors['text']), font=font_tiny)
        draw.text((30, y_current + 32), "learning what Arkify is",
                 fill=self._hex_to_rgb(self.colors['text']), font=font_tiny)

        # The punchline
        draw.text((20, height - 40), "This panel documents",
                 fill=self._hex_to_rgb(self.colors['dim']), font=font_tiny)
        draw.text((20, height - 28), "its own creation.",
                 fill=self._hex_to_rgb(self.colors['iteration4']), font=font_label)
        draw.text((20, height - 14), "∞ Meta-recursion",
                 fill=self._hex_to_rgb(self.colors['dim']), font=font_tiny)

        return img

    def _draw_iteration(self, draw, x, y, time, thought, action, color, font_label, font_tiny):
        """Draw one iteration/realization"""
        # Time badge
        draw.rectangle([(x, y), (x + 45, y + 16)], fill=self._hex_to_rgb(color))
        draw.text((x + 4, y + 3), time, fill='#000000', font=font_tiny)

        # Thought
        draw.text((x + 50, y), thought,
                 fill=self._hex_to_rgb(self.colors['text']), font=font_tiny)

        # Action/Result
        draw.text((x + 50, y + 12), action,
                 fill=self._hex_to_rgb(self.colors['dim']), font=font_tiny)

        # Arrow to next
        draw.text((x + 8, y + 24), "↓", fill=self._hex_to_rgb(color), font=font_label)

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
