"""
Shape Decorator Agent
Adds Canva-style decorative shapes: rounded rectangles, circles, arrows.
Provides visual polish and modern aesthetic.
"""

from PIL import Image, ImageDraw


class ShapeDecorator:
    """Draws decorative shapes with Canva-style polish"""

    def __init__(self):
        self.default_radius = 24  # Border radius for rounded corners

    def draw_rounded_rectangle(self, draw, xy, fill=None, outline=None, width=0, radius=None):
        """
        Draw rounded rectangle

        Args:
            draw: ImageDraw object
            xy: [(x1, y1), (x2, y2)] coordinates
            fill: Fill color
            outline: Outline color
            width: Outline width
            radius: Corner radius (default: self.default_radius)
        """
        if radius is None:
            radius = self.default_radius

        x1, y1 = xy[0]
        x2, y2 = xy[1]

        # Draw rounded rectangle using PIL's built-in method
        draw.rounded_rectangle(
            [(x1, y1), (x2, y2)],
            radius=radius,
            fill=fill,
            outline=outline,
            width=width
        )

    def draw_circle_badge(self, draw, center_x, center_y, radius, fill, text='', font=None):
        """
        Draw circular badge with optional text

        Args:
            draw: ImageDraw object
            center_x, center_y: Center coordinates
            radius: Circle radius
            fill: Fill color
            text: Optional text inside circle
            font: Font for text
        """
        # Draw circle
        draw.ellipse(
            [(center_x - radius, center_y - radius),
             (center_x + radius, center_y + radius)],
            fill=fill
        )

        # Draw text if provided
        if text and font:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            text_x = center_x - text_width // 2
            text_y = center_y - text_height // 2

            draw.text((text_x, text_y), text, fill='#FFFFFF', font=font)

    def draw_arrow(self, draw, start_xy, end_xy, color, width=4, arrow_size=20):
        """
        Draw arrow from start to end point

        Args:
            draw: ImageDraw object
            start_xy: (x, y) start point
            end_xy: (x, y) end point
            color: Arrow color
            width: Line width
            arrow_size: Size of arrow head
        """
        x1, y1 = start_xy
        x2, y2 = end_xy

        # Draw line
        draw.line([(x1, y1), (x2, y2)], fill=color, width=width)

        # Calculate arrow head points
        import math
        angle = math.atan2(y2 - y1, x2 - x1)

        # Arrow head triangle
        arrow_p1 = (
            x2 - arrow_size * math.cos(angle - math.pi / 6),
            y2 - arrow_size * math.sin(angle - math.pi / 6)
        )
        arrow_p2 = (
            x2 - arrow_size * math.cos(angle + math.pi / 6),
            y2 - arrow_size * math.sin(angle + math.pi / 6)
        )

        # Draw filled triangle
        draw.polygon([arrow_p1, (x2, y2), arrow_p2], fill=color)

    def draw_dotted_line(self, draw, start_xy, end_xy, color, width=2, dash_length=8, gap_length=4):
        """
        Draw dotted line

        Args:
            draw: ImageDraw object
            start_xy: (x, y) start point
            end_xy: (x, y) end point
            color: Line color
            width: Line width
            dash_length: Length of each dash
            gap_length: Length of gaps
        """
        x1, y1 = start_xy
        x2, y2 = end_xy

        import math
        total_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        segment_length = dash_length + gap_length

        num_segments = int(total_length / segment_length)

        for i in range(num_segments + 1):
            # Calculate segment start
            t_start = (i * segment_length) / total_length
            seg_x1 = x1 + t_start * (x2 - x1)
            seg_y1 = y1 + t_start * (y2 - y1)

            # Calculate segment end (dash only, not gap)
            t_end = min(((i * segment_length) + dash_length) / total_length, 1.0)
            seg_x2 = x1 + t_end * (x2 - x1)
            seg_y2 = y1 + t_end * (y2 - y1)

            draw.line([(seg_x1, seg_y1), (seg_x2, seg_y2)], fill=color, width=width)

    def add_panel_frame(self, img, padding=20, outline_color='#FFFFFF', outline_width=2, radius=24):
        """
        Add decorative frame around image

        Args:
            img: PIL Image
            padding: Inner padding
            outline_color: Frame color
            outline_width: Frame width
            radius: Corner radius

        Returns:
            PIL Image with frame
        """
        draw = ImageDraw.Draw(img)

        self.draw_rounded_rectangle(
            draw,
            [(padding, padding), (img.width - padding, img.height - padding)],
            outline=outline_color,
            width=outline_width,
            radius=radius
        )

        return img


if __name__ == '__main__':
    import os
    from PIL import ImageFont

    # Test shapes
    decorator = ShapeDecorator()

    # Create test image
    img = Image.new('RGB', (600, 400), '#22223B')
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype('/System/Library/Fonts/SFNSDisplay.ttf', 32)
    except:
        font = ImageFont.load_default()

    # Test rounded rectangle
    decorator.draw_rounded_rectangle(
        draw,
        [(50, 50), (250, 150)],
        fill='#06FFA5',
        radius=20
    )

    # Test circle badge
    decorator.draw_circle_badge(
        draw,
        center_x=150,
        center_y=250,
        radius=50,
        fill='#3B82F6',
        text='28',
        font=font
    )

    # Test arrow
    decorator.draw_arrow(
        draw,
        start_xy=(300, 100),
        end_xy=(500, 100),
        color='#FFD93D',
        width=6
    )

    # Test dotted line
    decorator.draw_dotted_line(
        draw,
        start_xy=(300, 200),
        end_xy=(500, 300),
        color='#E63946',
        width=3
    )

    # Add frame
    img = decorator.add_panel_frame(img, padding=15, outline_color='#06FFA5', outline_width=3)

    os.makedirs('output/test_agents', exist_ok=True)
    img.save('output/test_agents/shapes_test.png')

    print("✅ Shape decorator test generated: output/test_agents/shapes_test.png")
    print("   - Rounded rectangle (green)")
    print("   - Circle badge with '28' text")
    print("   - Arrow (gold)")
    print("   - Dotted line (red)")
    print("   - Frame border")
