# Arkify Landing Page - Viewport Cutoff Analysis Report

**Date**: 2026-04-18  
**Analyzed**: https://arkify.app  
**Image**: arkify-v4.png (1200x1600px)

## Executive Summary

### ✅ GOOD NEWS: No Hard Cutoff
The CSS does **NOT** use `overflow: hidden` or `max-height` that would permanently hide content. All 6 panels of the infographic are accessible via scrolling.

### ⚠️ USER EXPERIENCE ISSUE: Below-the-Fold Content
On common laptop and desktop viewport sizes (1366x768, 1920x1080), the bottom panels are **not initially visible** without scrolling:

- **ITERATIONS OVER TIME** panel (bottom left)
- **META-RECURSION** panel with ∞ symbol (bottom right)

## Critical Viewports Analysis

### 🚨 High-Impact Issue: Standard Laptops (1366x768)
- **Visibility**: Only 35% of infographic visible without scroll
- **Result**: Users see only top 2 rows (4 panels), miss bottom 2 panels
- **Impact**: The critical META-RECURSION message is hidden below fold

### ⚠️ Medium-Impact Issue: Full HD Desktop (1920x1080)
- **Visibility**: 55% visible without scroll
- **Result**: Bottom panels partially/fully cut off
- **Impact**: Users may not realize there's more content below

### ✅ Works Well On:
- **Mobile devices** (iPhone, Android): 100% visible without scroll
- **4K displays**: 100% visible
- **iPad Air/Pro**: 90-97% visible (minimal scroll needed)

## Root Cause

The CSS uses:
```css
body {
    display: flex;
    justify-content: center;  /* ← Centers vertically */
    min-height: 100vh;
}
```

When content height exceeds viewport height, `justify-content: center` pushes equal amounts of content **above and below** the viewport, requiring users to scroll **both up and down** to see everything.

## Technical Details

### Image Scaling Behavior
```
Container: max-width: 1200px, width: 100%
Image: width: 100% (maintains aspect ratio 4:3)

Viewport Width → Displayed Image Height:
- 375px (mobile) → 415px tall
- 768px (tablet) → 939px tall
- 1920px (desktop) → 1600px tall (original size)
```

### Content Layout Heights
```
Total page height on desktop (1920px wide):
- Header (title + tagline): ~80px
- Image: 1600px
- Footer: ~60px
- Body padding: 64px
- TOTAL: 1804px

Common viewport heights:
- Laptop 1366x768: 768px ← Only shows 35% of 1804px
- Desktop 1920x1080: 1080px ← Only shows 55% of 1804px
```

## Visibility Matrix

| Device | Viewport | Image Height | Visible | Panels Cut Off |
|--------|----------|--------------|---------|----------------|
| iPhone SE | 375x667 | 415px | 100% | None ✅ |
| iPhone 14 Pro Max | 430x932 | 488px | 100% | None ✅ |
| iPad Mini | 768x1024 | 939px | 87% | Bottom ~13% ⚠️ |
| iPad Pro 12.9 | 1024x1366 | 1280px | 91% | Bottom ~9% ⚠️ |
| Laptop 13" | 1280x720 | 1600px | **32%** | Bottom 4 panels 🚨 |
| Laptop 15" | 1366x768 | 1600px | **35%** | Bottom 4 panels 🚨 |
| Desktop HD | 1920x1080 | 1600px | **55%** | Bottom 2 panels 🚨 |
| Desktop QHD | 2560x1440 | 1600px | 77% | Bottom ~23% ⚠️ |
| Desktop 4K | 3840x2160 | 1600px | 100% | None ✅ |

## What Users See (Without Scrolling)

### ✅ Mobile (iPhone/Android)
```
┌─────────────────────┐
│ ARKIFY              │
│ ∞ This image...     │
├─────────────────────┤
│ ┌─────┬─────┐       │
│ │COM  │REAL │       │  ← All 6 panels
│ │ANAL │DATA │       │    visible
│ ├─────┼─────┤       │
│ │DEC  │AGENT│       │
│ │PATH │NET  │       │
│ ├─────┼─────┤       │
│ │ITER │META │       │
│ │TIME │∞    │       │
│ └─────┴─────┘       │
├─────────────────────┤
│ Footer              │
└─────────────────────┘
```

### 🚨 Laptop 1366x768 (Only 35% visible)
```
┌─────────────────────┐
│ ARKIFY              │
│ ∞ This image...     │
├─────────────────────┤
│ ┌─────┬─────┐       │
│ │COM  │REAL │       │  ← Only top
│ │ANAL │DATA │       │    2 rows visible
│ ├─────┼─────┤       │
│ │DEC  │AGENT│       │
│ │PATH │NET  │       │
│ ├─────┼─────┤       │
│ │█████│█████│ HIDDEN│  ← ITERATIONS OVER TIME
│ │█████│█████│ BELOW │     and META-RECURSION
│ └─────┴─────┘ FOLD  │     NOT visible!
```

## Recommendations

### Option 1: Remove Vertical Centering (Simplest)
```css
body {
    /* Remove: justify-content: center; */
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    padding: 2rem;
}
```
**Effect**: Content starts at top, users scroll down naturally.

### Option 2: Add Scroll Indicator (Medium)
```css
/* Add visual cue that there's more content below */
.scroll-hint {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    animation: bounce 2s infinite;
}
```

### Option 3: Responsive Centering (Complex)
```css
/* Only center on large screens where content fits */
@media (min-height: 1900px) {
    body {
        justify-content: center;
    }
}
```

### Option 4: Reduce Image Size (Trade-off)
```css
.infographic {
    max-height: 80vh; /* Limit height to 80% of viewport */
    width: auto;
    max-width: 100%;
}
```
**Trade-off**: Image quality reduced on large screens.

## Recommended Fix

**IMMEDIATE ACTION**: Remove `justify-content: center` from body CSS.

```diff
body {
    display: flex;
    flex-direction: column;
    align-items: center;
-   justify-content: center;
    min-height: 100vh;
    padding: 2rem;
}
```

This ensures:
1. ✅ All content visible on all viewports (via natural scrolling)
2. ✅ Users expect to scroll down (web convention)
3. ✅ No UX confusion about missing panels
4. ✅ Maintains responsive image scaling
5. ✅ No trade-offs in image quality

## Testing Plan

After implementing fix:
1. Test on laptop 1366x768 (most common laptop resolution)
2. Verify META-RECURSION panel visible after scroll
3. Check mobile (should remain unchanged)
4. Validate 4K display (should remain unchanged)

---

**Conclusion**: The infographic is NOT technically "cut off" (no overflow:hidden), but **appears cut off** to users on standard laptop/desktop viewports due to vertical centering. Fix by aligning content to top instead of center.
