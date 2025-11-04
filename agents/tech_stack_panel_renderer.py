"""
Tech Stack Panel Renderer (Canva Style)
Displays tech stack with REAL brand icons in 2x2 grid.
Uses gradients and generous whitespace for Canva aesthetic.
"""

from PIL import Image, ImageDraw, ImageFont
from agents.icon_fetcher import IconFetcher
from agents.gradient_renderer import GradientRenderer
from agents.shape_decorator import ShapeDecorator


class TechStackPanelRenderer:
    """Renders tech stack with real brand logos"""

    def __init__(self):
        self.icon_fetcher = IconFetcher()
        self.gradient_renderer = GradientRenderer()
        self.shape_decorator = ShapeDecorator()

        self.colors = {
            'text': '#F2F4F8',
            'dim': '#9A8C98'
        }

    def render(self, tech_stack, width=600, height=533):
        """
        Render tech stack panel with real icons

        Args:
            tech_stack: List of tech names (max 4)
            width, height: Panel dimensions

        Returns:
            PIL Image
        """
        # Create gradient background
        img = self.gradient_renderer.create_preset_gradient(
            width, height,
            'tech',
            direction='diagonal-tl-br'
        )

        draw = ImageDraw.Draw(img)

        # Load fonts
        try:
            font_title = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 32)
            font_tech = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 20)
        except:
            font_title = ImageFont.load_default()
            font_tech = ImageFont.load_default()

        # Title
        draw.text((40, 40), "TECH STACK", fill='#FFFFFF', font=font_title)

        # Fetch icons
        print(f"🔍 Fetching icons for: {tech_stack[:4]}")
        icons_data = self.icon_fetcher.fetch(tech_stack[:4])

        # 2x2 Grid layout
        icon_size = 100
        grid_start_x = 80
        grid_start_y = 120
        spacing_x = 200
        spacing_y = 180

        positions = [
            (grid_start_x, grid_start_y),                      # Top-left
            (grid_start_x + spacing_x, grid_start_y),          # Top-right
            (grid_start_x, grid_start_y + spacing_y),          # Bottom-left
            (grid_start_x + spacing_x, grid_start_y + spacing_y)  # Bottom-right
        ]

        for i, (icon_data, pos) in enumerate(zip(icons_data, positions)):
            if i >= len(tech_stack):
                break

            x, y = pos

            # Draw rounded white background for icon
            self.shape_decorator.draw_rounded_rectangle(
                draw,
                [(x - 10, y - 10), (x + icon_size + 10, y + icon_size + 10)],
                fill='#FFFFFF',
                radius=16
            )

            # Place icon
            if icon_data.get('success') and icon_data.get('png_path'):
                try:
                    icon_img = Image.open(icon_data['png_path'])
                    icon_img = icon_img.resize((icon_size, icon_size), Image.Resampling.LANCZOS)

                    # Convert RGBA to RGB if needed
                    if icon_img.mode == 'RGBA':
                        # Create white background
                        bg = Image.new('RGB', icon_img.size, '#FFFFFF')
                        bg.paste(icon_img, mask=icon_img.split()[3])
                        icon_img = bg

                    img.paste(icon_img, (x, y))
                except Exception as e:
                    print(f"⚠️ Could not load icon for {tech_stack[i]}: {e}")
                    # Fallback: Draw colored box with letter
                    self._draw_fallback_icon(draw, x, y, icon_size, tech_stack[i])
            else:
                # Fallback
                self._draw_fallback_icon(draw, x, y, icon_size, tech_stack[i])

            # Tech name below icon
            tech_name = tech_stack[i]
            name_bbox = draw.textbbox((0, 0), tech_name, font=font_tech)
            name_width = name_bbox[2] - name_bbox[0]
            name_x = x + (icon_size - name_width) // 2

            draw.text(
                (name_x, y + icon_size + 20),
                tech_name,
                fill='#FFFFFF',
                font=font_tech
            )

        return img

    def _draw_fallback_icon(self, draw, x, y, size, tech_name):
        """Draw fallback colored box if icon fetch fails"""
        # Use first letter
        letter = tech_name[0].upper()

        # Color based on first letter
        colors = ['#E63946', '#06FFA5', '#FFD93D', '#9333EA']
        color_index = ord(letter) % len(colors)
        color = colors[color_index]

        # Draw colored square
        draw.rectangle(
            [(x, y), (x + size, y + size)],
            fill=color
        )

        # Draw letter
        try:
            fallback_font = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 48)
        except:
            fallback_font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), letter, font=fallback_font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        text_x = x + (size - text_width) // 2
        text_y = y + (size - text_height) // 2

        draw.text((text_x, text_y), letter, fill='#FFFFFF', font=fallback_font)


if __name__ == '__main__':
    import os

    # Test
    renderer = TechStackPanelRenderer()

    tech_stack = ['Python', 'Anthropic', 'GitHub', 'PIL']

    img = renderer.render(tech_stack, 600, 533)

    os.makedirs('output/test_agents', exist_ok=True)
    img.save('output/test_agents/tech_stack_panel_test.png')

    print("✅ Tech stack panel generated: output/test_agents/tech_stack_panel_test.png")
    print(f"   Icons: {', '.join(tech_stack)}")
