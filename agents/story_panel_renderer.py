"""
Story Panel Renderer (Canva Style)
Renders narrative-driven panels with emotional hooks.
Uses gradients, big typography, and emojis for impact.
"""

from PIL import Image, ImageDraw, ImageFont
from agents.gradient_renderer import GradientRenderer
from agents.shape_decorator import ShapeDecorator


class StoryPanelRenderer:
    """Renders story panels with Canva-style visual impact"""

    def __init__(self):
        self.gradient_renderer = GradientRenderer()
        self.shape_decorator = ShapeDecorator()

    def render(self, story_data, width=600, height=533):
        """
        Render story panel

        Args:
            story_data: {
                'type': 'fail' | 'success' | 'insight' | 'meta',
                'emoji': '🔴' | '✅' | '💡' | '∞',
                'title': str (main hook),
                'subtitle': str (supporting text),
                'number': str (optional big number),
            }
            width, height: Panel dimensions

        Returns:
            PIL Image
        """
        # Get gradient type
        gradient_type = story_data.get('type', 'dark')

        # Create gradient background
        img = self.gradient_renderer.create_preset_gradient(
            width, height,
            gradient_type,
            direction='diagonal-tl-br'
        )

        draw = ImageDraw.Draw(img)

        # Load fonts
        try:
            font_emoji = ImageFont.truetype('/System/Library/Fonts/Apple Color Emoji.ttc', 80)
            font_title = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 36)
            font_subtitle = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 20)
            font_number = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 96)
        except:
            font_emoji = font_title = font_subtitle = font_number = ImageFont.load_default()

        # Content positioning
        y = 80

        # Emoji (if provided)
        emoji = story_data.get('emoji', '')
        if emoji:
            # Center emoji horizontally
            emoji_bbox = draw.textbbox((0, 0), emoji, font=font_emoji)
            emoji_width = emoji_bbox[2] - emoji_bbox[0]
            emoji_x = (width - emoji_width) // 2

            draw.text((emoji_x, y), emoji, font=font_emoji, embedded_color=True)
            y += 120

        # Number (if provided) - BIG and prominent
        number = story_data.get('number', '')
        if number:
            draw.text((60, y), number, fill='#FFFFFF', font=font_number)
            y += 120

        # Title (main hook)
        title = story_data.get('title', '')
        if title:
            # Word wrap for long titles
            words = title.split()
            lines = []
            current_line = []

            for word in words:
                test_line = ' '.join(current_line + [word])
                bbox = draw.textbbox((0, 0), test_line, font=font_title)
                if bbox[2] - bbox[0] < width - 80:  # 40px margin each side
                    current_line.append(word)
                else:
                    if current_line:
                        lines.append(' '.join(current_line))
                    current_line = [word]

            if current_line:
                lines.append(' '.join(current_line))

            # Draw title lines
            for line in lines:
                draw.text((40, y), line, fill='#FFFFFF', font=font_title)
                y += 45

            y += 20  # Space before subtitle

        # Subtitle (supporting text)
        subtitle = story_data.get('subtitle', '')
        if subtitle:
            # Word wrap subtitle
            words = subtitle.split()
            lines = []
            current_line = []

            for word in words:
                test_line = ' '.join(current_line + [word])
                bbox = draw.textbbox((0, 0), test_line, font=font_subtitle)
                if bbox[2] - bbox[0] < width - 80:
                    current_line.append(word)
                else:
                    if current_line:
                        lines.append(' '.join(current_line))
                    current_line = [word]

            if current_line:
                lines.append(' '.join(current_line))

            # Draw subtitle lines
            for line in lines:
                draw.text((40, y), line, fill='#FFFFFFCC', font=font_subtitle)  # Slightly transparent
                y += 30

        return img


if __name__ == '__main__':
    import os

    # Test different story panels
    renderer = StoryPanelRenderer()

    os.makedirs('output/test_agents', exist_ok=True)

    # Panel 1: The Mistake
    panel1 = renderer.render({
        'type': 'fail',
        'emoji': '❌',
        'title': 'Built with mock data',
        'subtitle': 'Created Phase 2 with invented decision paths. User caught it immediately.'
    })
    panel1.save('output/test_agents/story_panel_mistake.png')

    # Panel 2: The Success
    panel2 = renderer.render({
        'type': 'success',
        'emoji': '✅',
        'title': 'Extracted from git history',
        'subtitle': 'Replaced ALL mock data with real commits, timestamps, actual decisions.'
    })
    panel2.save('output/test_agents/story_panel_success.png')

    # Panel 3: The Insight
    panel3 = renderer.render({
        'type': 'insight',
        'emoji': '💡',
        'title': 'Mistake IS research',
        'subtitle': 'The failure became a decision path to visualize. Meta-learning in action.'
    })
    panel3.save('output/test_agents/story_panel_insight.png')

    # Panel 4: The Meta
    panel4 = renderer.render({
        'type': 'meta',
        'emoji': '∞',
        'title': 'This panel documents itself',
        'subtitle': 'Infinite recursion as a feature. Arkify researches its own thinking.'
    })
    panel4.save('output/test_agents/story_panel_meta.png')

    # Panel 5: Big Number
    panel5 = renderer.render({
        'type': 'dark',
        'number': '28',
        'title': 'Commits analyzed',
        'subtitle': '5 decision paths extracted from real git history'
    })
    panel5.save('output/test_agents/story_panel_number.png')

    print("✅ Generated 5 story panel test images:")
    print("   - Mistake (fail gradient, red)")
    print("   - Success (success gradient, green)")
    print("   - Insight (insight gradient, gold)")
    print("   - Meta (meta gradient, purple)")
    print("   - Number (dark gradient, big 28)")
