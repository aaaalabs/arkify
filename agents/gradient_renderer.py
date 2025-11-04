"""
Gradient Renderer Agent
Creates smooth linear gradients for Canva-style visual depth.
Supports horizontal, vertical, and diagonal gradients.
Pure PIL implementation - no numpy required.
"""

from PIL import Image, ImageDraw
import math


class GradientRenderer:
    """Renders smooth gradient backgrounds"""

    def __init__(self):
        self.gradients = {
            'fail': ['#E63946', '#D62839'],         # Red gradient
            'success': ['#06FFA5', '#00D981'],      # Green gradient
            'insight': ['#FFD93D', '#FFC300'],      # Gold gradient
            'tech': ['#3B82F6', '#2563EB'],         # Blue gradient
            'meta': ['#9333EA', '#7E22CE'],         # Purple gradient
            'dark': ['#22223B', '#1A1A2E'],         # Dark gradient
        }

    def create_linear_gradient(self, width, height, color_start, color_end, direction='vertical'):
        """
        Create linear gradient image

        Args:
            width, height: Image dimensions
            color_start: Starting color (hex string)
            color_end: Ending color (hex string)
            direction: 'vertical', 'horizontal', 'diagonal-tl-br', 'diagonal-tr-bl'

        Returns:
            PIL Image with gradient
        """
        # Convert hex to RGB
        start_rgb = self._hex_to_rgb(color_start)
        end_rgb = self._hex_to_rgb(color_end)

        # Create gradient image
        if direction == 'vertical':
            return self._vertical_gradient(width, height, start_rgb, end_rgb)
        elif direction == 'horizontal':
            return self._horizontal_gradient(width, height, start_rgb, end_rgb)
        elif direction == 'diagonal-tl-br':
            return self._diagonal_gradient_tlbr(width, height, start_rgb, end_rgb)
        elif direction == 'diagonal-tr-bl':
            return self._diagonal_gradient_trbl(width, height, start_rgb, end_rgb)
        else:
            return self._vertical_gradient(width, height, start_rgb, end_rgb)

    def create_preset_gradient(self, width, height, preset_name, direction='vertical'):
        """
        Create gradient using preset color scheme

        Args:
            width, height: Image dimensions
            preset_name: 'fail', 'success', 'insight', 'tech', 'meta', 'dark'
            direction: Gradient direction

        Returns:
            PIL Image with gradient
        """
        if preset_name not in self.gradients:
            preset_name = 'dark'

        colors = self.gradients[preset_name]
        return self.create_linear_gradient(width, height, colors[0], colors[1], direction)

    def _vertical_gradient(self, width, height, start_rgb, end_rgb):
        """Vertical gradient (top to bottom)"""
        img = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(img)

        for y in range(height):
            ratio = y / height
            r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
            g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
            b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)

            draw.line([(0, y), (width, y)], fill=(r, g, b))

        return img

    def _horizontal_gradient(self, width, height, start_rgb, end_rgb):
        """Horizontal gradient (left to right)"""
        img = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(img)

        for x in range(width):
            ratio = x / width
            r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
            g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
            b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)

            draw.line([(x, 0), (x, height)], fill=(r, g, b))

        return img

    def _diagonal_gradient_tlbr(self, width, height, start_rgb, end_rgb):
        """Diagonal gradient (top-left to bottom-right)"""
        img = Image.new('RGB', (width, height))
        pixels = img.load()
        max_dist = math.sqrt(width**2 + height**2)

        for y in range(height):
            for x in range(width):
                dist = math.sqrt(x**2 + y**2)
                ratio = dist / max_dist
                r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
                g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
                b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)

                pixels[x, y] = (r, g, b)

        return img

    def _diagonal_gradient_trbl(self, width, height, start_rgb, end_rgb):
        """Diagonal gradient (top-right to bottom-left)"""
        img = Image.new('RGB', (width, height))
        pixels = img.load()
        max_dist = math.sqrt(width**2 + height**2)

        for y in range(height):
            for x in range(width):
                dist = math.sqrt((width - x)**2 + y**2)
                ratio = dist / max_dist
                r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
                g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
                b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)

                pixels[x, y] = (r, g, b)

        return img

    def _hex_to_rgb(self, hex_color):
        """Convert hex to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


if __name__ == '__main__':
    import os

    # Test gradients
    renderer = GradientRenderer()

    os.makedirs('output/test_agents', exist_ok=True)

    # Test all presets
    presets = ['fail', 'success', 'insight', 'tech', 'meta', 'dark']
    directions = ['vertical', 'horizontal', 'diagonal-tl-br']

    for preset in presets:
        for direction in directions:
            img = renderer.create_preset_gradient(400, 300, preset, direction)
            filename = f'output/test_agents/gradient_{preset}_{direction}.png'
            img.save(filename)
            print(f"✅ Generated: {filename}")

    print(f"\n🎨 Generated {len(presets) * len(directions)} gradient test images")
