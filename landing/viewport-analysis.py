#!/usr/bin/env python3
"""
Viewport Analysis for Arkify Landing Page
Calculates if the infographic is cut off at different viewport sizes
"""

# Image dimensions
IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 1600

# Page elements (estimated heights in pixels)
HEADER_HEIGHT = 80  # h1 + tagline + margins
FOOTER_HEIGHT = 60  # footer text + margins
BODY_PADDING = 32 * 2  # 2rem top + 2rem bottom (assuming 1rem = 16px)

# Common viewport sizes to test
VIEWPORTS = {
    # Mobile
    "iPhone SE": (375, 667),
    "iPhone 12/13": (390, 844),
    "iPhone 14 Pro Max": (430, 932),
    "Samsung Galaxy S20": (360, 800),

    # Tablet
    "iPad Mini": (768, 1024),
    "iPad Air": (820, 1180),
    "iPad Pro 11": (834, 1194),
    "iPad Pro 12.9": (1024, 1366),

    # Desktop
    "Laptop 13": (1280, 720),
    "Laptop 15": (1366, 768),
    "Desktop HD": (1920, 1080),
    "Desktop QHD": (2560, 1440),
    "Desktop 4K": (3840, 2160),
}

def calculate_displayed_image_height(viewport_width, container_max_width=1200):
    """
    Calculate the actual displayed height of the image based on viewport width.
    The image has width: 100% and maintains aspect ratio.
    """
    # Container is max-width: 1200px, but also constrained by viewport
    container_width = min(viewport_width - 64, container_max_width)  # Subtract body padding

    # Image maintains aspect ratio
    aspect_ratio = IMAGE_HEIGHT / IMAGE_WIDTH
    displayed_height = container_width * aspect_ratio

    return displayed_height

def analyze_viewport(name, width, height):
    """Analyze if the infographic fits in the given viewport."""
    displayed_image_height = calculate_displayed_image_height(width)
    total_content_height = HEADER_HEIGHT + displayed_image_height + FOOTER_HEIGHT + BODY_PADDING

    fits_without_scroll = total_content_height <= height
    overflow = total_content_height - height if not fits_without_scroll else 0

    # Calculate what percentage of the image is visible without scrolling
    available_height_for_image = height - HEADER_HEIGHT - FOOTER_HEIGHT - BODY_PADDING
    visible_percentage = min(100, (available_height_for_image / displayed_image_height) * 100) if displayed_image_height > 0 else 100

    return {
        'viewport': (width, height),
        'displayed_image_height': displayed_image_height,
        'total_content_height': total_content_height,
        'fits': fits_without_scroll,
        'overflow': overflow,
        'visible_percentage': visible_percentage
    }

def main():
    print("=" * 80)
    print("ARKIFY VIEWPORT ANALYSIS")
    print("=" * 80)
    print(f"\nOriginal Image: {IMAGE_WIDTH}x{IMAGE_HEIGHT}px")
    print(f"Container: max-width 1200px, padding 2rem (32px)")
    print(f"Estimated Header: {HEADER_HEIGHT}px")
    print(f"Estimated Footer: {FOOTER_HEIGHT}px")
    print("\n" + "=" * 80)

    issues = []

    for category in ["Mobile", "Tablet", "Desktop"]:
        print(f"\n{category.upper()} DEVICES:")
        print("-" * 80)

        for name, (width, height) in VIEWPORTS.items():
            if (category == "Mobile" and width < 768) or \
               (category == "Tablet" and 768 <= width < 1280) or \
               (category == "Desktop" and width >= 1280):

                result = analyze_viewport(name, width, height)

                status = "✅ FITS" if result['fits'] else "⚠️  SCROLLS"

                print(f"\n{name:20} ({width}x{height})")
                print(f"  Status: {status}")
                print(f"  Image displayed as: {result['displayed_image_height']:.0f}px tall")
                print(f"  Total content: {result['total_content_height']:.0f}px")
                print(f"  Visible without scroll: {result['visible_percentage']:.1f}%")

                if not result['fits']:
                    print(f"  ⚠️  Overflow: {result['overflow']:.0f}px (user must scroll)")

                    # Check if bottom panels are visible
                    if result['visible_percentage'] < 70:
                        issue = f"{name}: Only {result['visible_percentage']:.0f}% visible - ITERATIONS OVER TIME and META-RECURSION likely cut off!"
                        issues.append(issue)
                        print(f"  🚨 {issue}")

    print("\n" + "=" * 80)
    print("CRITICAL ISSUES SUMMARY:")
    print("=" * 80)

    if issues:
        print("\n⚠️  POTENTIAL CUTOFF ISSUES DETECTED:\n")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
    else:
        print("\n✅ No critical cutoff issues detected.")
        print("All viewports show at least 70% of the image without scrolling.")

    print("\n" + "=" * 80)
    print("CSS RECOMMENDATIONS:")
    print("=" * 80)

    print("""
The current CSS uses:
  body {
    display: flex;
    justify-content: center;  ← Centers content vertically
    min-height: 100vh;        ← Minimum viewport height
  }

This is CORRECT and will not cut off content. When content exceeds viewport
height, the page becomes scrollable, allowing users to see all panels.

However, the CONCERN is that users may not realize they need to scroll,
especially on mobile devices where the META-RECURSION panel (bottom right)
might be below the fold.

POTENTIAL SOLUTION:
- Add a subtle scroll indicator on mobile
- Or remove 'justify-content: center' to start content at top
- Or add lazy loading / fade-in for bottom panels to signal more content below
""")

if __name__ == "__main__":
    main()
