"""
Panel Agent Base Class
Autonomous panel design within strict design system constraints

Every Panel Agent must inherit from this base and implement render().
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any, List, Tuple
from PIL import Image, ImageDraw, ImageFont
from dataclasses import dataclass


@dataclass
class DesignSystemContract:
    """
    The Sacred Rules - violations result in rejection.
    Based on Future Dust 2025 design system.
    """
    # Spatial
    panel_size: Tuple[int, int] = (300, 400)
    grid_unit: int = 8
    margin_min: int = 16  # 2 grid units
    margin_max: int = 32  # 4 grid units

    # Typography
    font_family: str = "Helvetica"
    font_sizes: List[int] = None  # [18, 24, 32, 48, 72]
    line_height: int = 24  # 3 grid units

    # Color (Future Dust palette)
    colors: Dict[str, str] = None

    # Accessibility
    contrast_ratio_min: float = 4.5
    font_size_min: int = 18
    touch_target_min: int = 44

    def __post_init__(self):
        if self.font_sizes is None:
            self.font_sizes = [18, 24, 32, 48, 72]

        if self.colors is None:
            self.colors = {
                'future_dust': '#4A4E69',
                'electric_green': '#06FFA5',
                'cosmic_white': '#FFFFFF',
                'deep_space': '#22223B',
                'expected_grey': '#8B92A0',
                'text': '#FFFFFF',
                'text_dim': '#C7C7C7',
            }


@dataclass
class PanelAgentMessage:
    """Communication protocol between agents and orchestrator."""
    agent_id: str
    phase: str  # "negotiation" | "render" | "validation"
    panel_position: Tuple[int, int]  # (col, row)
    data_requested: List[str] = None
    data_consumed: Dict[str, Any] = None
    visual_weight: float = 0.3  # 0.0-1.0
    color_emphasis: str = "cosmic_white"
    animation_intent: str = "none"
    render_output: Image.Image = None
    metadata: Dict[str, Any] = None


class ValidationResult:
    """Result of design system validation."""

    def __init__(self):
        self.passed = True
        self.violations: List[Dict[str, Any]] = []
        self.warnings: List[Dict[str, Any]] = []

    def add_violation(self, rule: str, expected: Any, actual: Any):
        self.passed = False
        self.violations.append({
            "rule": rule,
            "expected": expected,
            "actual": actual
        })

    def add_warning(self, warning_type: str, location: str):
        self.warnings.append({
            "type": warning_type,
            "location": location
        })


class PanelAgentBase(ABC):
    """
    Base class for all Panel Agents.

    Provides:
    - Design system contract enforcement
    - Typography helpers
    - Color validation
    - Common rendering utilities

    Agents must implement:
    - render(): Create panel image from assigned data
    - negotiate(): Declare data needs and visual weight
    """

    def __init__(self, agent_id: str, design_system: DesignSystemContract = None):
        self.agent_id = agent_id
        self.design_system = design_system or DesignSystemContract()

        # Load fonts
        self.fonts = self._load_fonts()

        # Agent state
        self.assigned_data: Dict[str, Any] = {}
        self.panel_position: Tuple[int, int] = (0, 0)
        self.narrative_context: Dict[str, Any] = {}

    # === Abstract Methods (Agents MUST implement) ===

    @abstractmethod
    def negotiate(self, available_data: Dict[str, Any]) -> PanelAgentMessage:
        """
        Phase 1: Declare what data this agent wants and visual weight.

        Args:
            available_data: All data from input YAML

        Returns:
            PanelAgentMessage with data_requested and visual_weight
        """
        pass

    @abstractmethod
    def render(self, assigned_data: Dict[str, Any]) -> Image.Image:
        """
        Phase 2: Create panel image (300x400px).

        Args:
            assigned_data: Data allocated by orchestrator

        Returns:
            PIL Image (must be exactly 300x400px)
        """
        pass

    # === Provided Methods (Agents CAN use) ===

    def validate(self, panel_image: Image.Image) -> ValidationResult:
        """
        Validate panel against design system contract.

        Checks:
        - Panel size (300x400px)
        - Grid alignment (8px)
        - Color contrast (WCAG AA)
        - Typography (approved sizes)
        """
        result = ValidationResult()

        # Check panel size
        if panel_image.size != self.design_system.panel_size:
            result.add_violation(
                "panel_size",
                self.design_system.panel_size,
                panel_image.size
            )

        # TODO: Add more validation
        # - Grid alignment detection
        # - Color contrast analysis
        # - Font size verification

        return result

    def create_panel_canvas(self, bg_color: str = None) -> Tuple[Image.Image, ImageDraw.Draw]:
        """
        Create blank panel canvas with design system background.

        Args:
            bg_color: Background color (default: deep_space)

        Returns:
            (PIL Image, ImageDraw object)
        """
        if bg_color is None:
            bg_color = self.design_system.colors['deep_space']

        canvas = Image.new('RGB', self.design_system.panel_size, bg_color)
        draw = ImageDraw.Draw(canvas)

        return canvas, draw

    def draw_text(self,
                  draw: ImageDraw.Draw,
                  text: str,
                  pos: Tuple[int, int],
                  font_key: str,
                  color: str,
                  align: str = 'left') -> None:
        """
        Draw text with alignment.

        Args:
            draw: ImageDraw object
            text: Text to draw
            pos: (x, y) position
            font_key: Font size key ('tiny', 'small', 'medium', 'large', 'huge')
            color: Color key from design system
            align: 'left' | 'center' | 'right'
        """
        font = self.fonts.get(font_key, self.fonts['small'])
        color_hex = self.design_system.colors.get(color, color)

        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]

            x, y = pos
            if align == 'center':
                x -= text_width // 2
            elif align == 'right':
                x -= text_width

            draw.text((x, y), text, font=font, fill=color_hex)
        except:
            # Fallback without bbox
            draw.text(pos, text, fill=color_hex)

    def draw_wrapped_text(self,
                          draw: ImageDraw.Draw,
                          text: str,
                          x: int,
                          y: int,
                          max_width: int,
                          font_key: str,
                          color: str) -> int:
        """
        Draw text with word wrapping.

        Args:
            draw: ImageDraw object
            text: Text to wrap
            x, y: Starting position
            max_width: Maximum line width
            font_key: Font size key
            color: Color key

        Returns:
            Total height of wrapped text
        """
        font = self.fonts.get(font_key, self.fonts['small'])
        color_hex = self.design_system.colors.get(color, color)

        lines = self._get_wrapped_lines(draw, text, max_width, font)

        line_height = self.design_system.line_height
        for i, line in enumerate(lines):
            draw.text((x, y + i * line_height), line, font=font, fill=color_hex)

        return len(lines) * line_height

    def _get_wrapped_lines(self,
                           draw: ImageDraw.Draw,
                           text: str,
                           max_width: int,
                           font: ImageFont.FreeTypeFont) -> List[str]:
        """Calculate wrapped lines without drawing."""
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            current_line.append(word)
            line_text = ' '.join(current_line)

            try:
                bbox = draw.textbbox((0, 0), line_text, font=font)
                line_width = bbox[2] - bbox[0]
            except:
                line_width = len(line_text) * 8

            if line_width > max_width:
                if len(current_line) > 1:
                    current_line.pop()
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(line_text)
                    current_line = []

        if current_line:
            lines.append(' '.join(current_line))

        return lines

    def align_to_grid(self, value: int) -> int:
        """
        Snap value to 8px grid.

        Args:
            value: Pixel value

        Returns:
            Nearest grid-aligned value
        """
        return round(value / self.design_system.grid_unit) * self.design_system.grid_unit

    def _load_fonts(self) -> Dict[str, ImageFont.FreeTypeFont]:
        """Load typography system fonts."""
        font_map = {
            'tiny': 18,
            'small': 24,
            'small_bold': 24,
            'medium': 32,
            'large': 48,
            'huge': 72
        }

        fonts = {}
        for name, size in font_map.items():
            try:
                # Try macOS system fonts
                fonts[name] = ImageFont.truetype(
                    "/System/Library/Fonts/Helvetica.ttc", size
                )
            except:
                try:
                    # Fallback to Linux fonts
                    fonts[name] = ImageFont.truetype(
                        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size
                    )
                except:
                    # Last resort
                    fonts[name] = ImageFont.load_default()

        return fonts
