"""
Layout Compositor Phase 2.1 (Canva Style)
Assembles 6-panel story-driven layout with gradients and real icons.

Canvas: 1200x1600px (Instagram portrait 3:4)
Grid: 2x3 = 6 panels @ 600x533px each
Style: Canva 2025 (gradients, shapes, generous whitespace)
"""

from PIL import Image, ImageDraw, ImageFont
from agents.story_panel_renderer import StoryPanelRenderer
from agents.tech_stack_panel_renderer import TechStackPanelRenderer
from agents.gradient_renderer import GradientRenderer


class LayoutCompositorPhase21:
    """Composes Phase 2.1 output: Canva-style story-driven layout"""

    def __init__(self):
        self.story_renderer = StoryPanelRenderer()
        self.tech_renderer = TechStackPanelRenderer()
        self.gradient_renderer = GradientRenderer()

        self.colors = {
            'bg': '#1A1A2E',
            'text': '#F2F4F8',
            'accent': '#06FFA5'
        }

    def compose(self, project_data, output_path):
        """
        Compose Phase 2.1 layout

        Canvas: 1200x1600px
        Layout:
        ┌──────────────────────────────────────┐
        │  HEADER (1200x200px)                 │
        ├─────────────────┬────────────────────┤
        │ PANEL 1         │ PANEL 2            │  600x533px
        │ The Mistake     │ The Catch          │
        ├─────────────────┼────────────────────┤
        │ PANEL 3         │ PANEL 4            │
        │ The Insight     │ Tech Stack         │
        ├─────────────────┼────────────────────┤
        │ PANEL 5         │ PANEL 6            │
        │ By Numbers      │ The Meta           │
        └─────────────────┴────────────────────┘
        """
        # Canvas (portrait format for mobile)
        canvas_width = 1200
        canvas_height = 1600
        img = Image.new('RGB', (canvas_width, canvas_height), self._hex_to_rgb(self.colors['bg']))

        # HEADER (1200x200px)
        self._draw_header(img, project_data)

        # Panel dimensions
        panel_width = 600
        panel_height = 533

        # ROW 1 (y=200)
        # Panel 1: The Mistake
        panel1 = self.story_renderer.render({
            'type': 'fail',
            'emoji': '❌',
            'title': 'Built with mock data',
            'subtitle': 'Created Phase 2 with invented decision paths. User caught it immediately.'
        }, panel_width, panel_height)
        img.paste(panel1, (0, 200))

        # Panel 2: The Catch
        panel2 = self.story_renderer.render({
            'type': 'success',
            'emoji': '✅',
            'title': 'User: Never use mock',
            'subtitle': 'Replaced ALL with real git commits. 28 commits analyzed, 100% traceable data.'
        }, panel_width, panel_height)
        img.paste(panel2, (600, 200))

        # ROW 2 (y=733)
        # Panel 3: The Insight
        panel3 = self.story_renderer.render({
            'type': 'insight',
            'emoji': '💡',
            'title': 'Mistake IS research',
            'subtitle': 'The failure became a decision path to visualize. Arkify documents its own learning.'
        }, panel_width, panel_height)
        img.paste(panel3, (0, 733))

        # Panel 4: Tech Stack (with REAL icons!)
        tech_stack = project_data.get('tech_stack', ['Python', 'PIL', 'cairosvg', 'Git'])
        panel4 = self.tech_renderer.render(tech_stack, panel_width, panel_height)
        img.paste(panel4, (600, 733))

        # ROW 3 (y=1266)
        # Panel 5: By Numbers
        commits = project_data.get('meta', {}).get('commits_analyzed', 28)
        panel5 = self.story_renderer.render({
            'type': 'dark',
            'number': str(commits),
            'title': 'Commits analyzed',
            'subtitle': '5 decision paths extracted from real git history'
        }, panel_width, panel_height)
        img.paste(panel5, (0, 1266))

        # Panel 6: The Meta
        panel6 = self.story_renderer.render({
            'type': 'meta',
            'emoji': '∞',
            'title': 'This panel documents itself',
            'subtitle': 'Infinite recursion as a feature. You are a researcher of your own thoughts.'
        }, panel_width, panel_height)
        img.paste(panel6, (600, 1266))

        # Save
        img.save(output_path, quality=95, optimize=True)
        print(f"✅ Phase 2.1 generated: {output_path}")

        return True

    def _draw_header(self, img, project_data):
        """Draw header with viral hook"""
        draw = ImageDraw.Draw(img)

        try:
            font_hook = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 56)
            font_sub = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 22)
        except:
            font_hook = ImageFont.load_default()
            font_sub = ImageFont.load_default()

        # Gradient background for header
        header_gradient = self.gradient_renderer.create_preset_gradient(
            1200, 200,
            'dark',
            direction='horizontal'
        )
        img.paste(header_gradient, (0, 0))

        # Main hook (THE viral message)
        hook = "Your Mistakes ARE Your Research"
        draw.text((60, 50), hook, fill=self._hex_to_rgb(self.colors['accent']), font=font_hook)

        # Subtext
        sub = "Arkify Phase 2.1 • Architecture through Real Decisions"
        draw.text((60, 130), sub, fill=self._hex_to_rgb(self.colors['text']), font=font_sub)

    def _hex_to_rgb(self, hex_color):
        """Convert hex to RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


if __name__ == '__main__':
    import yaml
    import os

    # Load test data
    test_data = {
        'name': 'Arkify Phase 2.1',
        'tagline': 'Architecture through Real Decisions',
        'tech_stack': ['Python', 'Anthropic', 'GitHub', 'PIL'],
        'meta': {
            'commits_analyzed': 28
        }
    }

    compositor = LayoutCompositorPhase21()

    os.makedirs('output', exist_ok=True)
    success = compositor.compose(test_data, 'output/arkify-phase2.1-test.png')

    if success:
        print("\n✅ Phase 2.1 test layout generated!")
        print("   Canvas: 1200x1600px (portrait)")
        print("   Panels: 6 @ 600x533px each")
        print("   Style: Canva 2025 (gradients + real icons)")
        print("\n📊 Panels:")
        print("   1. The Mistake (fail gradient)")
        print("   2. The Catch (success gradient)")
        print("   3. The Insight (insight gradient)")
        print("   4. Tech Stack (with REAL brand icons)")
        print("   5. By Numbers (28 commits)")
        print("   6. The Meta (infinite recursion)")
        print("\n🎯 Viral Hook: 'Your Mistakes ARE Your Research'")
