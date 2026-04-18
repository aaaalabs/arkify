# Phase 2 Panel Designs - Greifbar & Anschaulich

**SLC Principle:** Simple, Lovable, Complete
**Ziel:** Architecture durch konkrete Beispiele zeigen, nicht Abstraktionen

---

## Panel Layout (3x3 Grid)

```
┌─────────────────────────────────────────┐
│  HEADER - "Architecture meets Story"    │ (900x400px)
├─────────────┬─────────────┬─────────────┤
│ DECISION 1  │ DECISION 2  │ DECISION 3  │ (300x400px each)
│ Icon Path   │ Contrast    │ Grid System │
├─────────────┼─────────────┼─────────────┤
│ AUTONOMY    │ TIMELINE    │ RESULTS     │
│ Spectrum    │ 10h Story   │ Numbers     │
├─────────────┼─────────────┼─────────────┤
│ TECH STACK  │ REALITY     │ LEARNING    │
│ (evolved)   │ (kept)      │ (evolved)   │
└─────────────┴─────────────┴─────────────┘
```

---

## Panel 1: "Icon Rendering - 4 Tries"

**Visual:** 4 squares horizontal, progress bar style

```
TRY 1        TRY 2        TRY 3        TRY 4
[████]  →   [████]  →   [████]  →   [████]
 ❌           ❌           ❌           ✅
Colored     Download    SimpleIcons  cairosvg
boxes       PNGs        CDN
UGLY        MANUAL      NO SVG       WORKS!
30min       1h          2h           1h
```

**Layout:**
- Title: "REAL ICONS: 4 TRIES"
- 4 boxes, each with:
  - Visual representation (colored box → PNG → SVG → perfect icon)
  - Result (❌ or ✅)
  - Reason (one word: UGLY, MANUAL, NO SVG, WORKS)
  - Time spent
- Bottom: "4.5 hours to solve"

**Colors:**
- Failed tries: Red background (#FF006E)
- Success: Green background (#06FFA5)
- Icons get progressively better visually

**Greifbar:** You SEE the evolution from ugly boxes to perfect icons

---

## Panel 2: "Contrast Journey"

**Visual:** Before/After split, big numbers

```
┌──────────────────────┐
│ CONTRAST JOURNEY     │
├──────────┬───────────┤
│ BEFORE   │   AFTER   │
│          │           │
│  [████]  │  [████]   │
│  Text    │  Text     │
│          │           │
│   2:1    │   7.12:1  │
│  FAIL    │  WCAG AA  │
│          │           │
│ Barely   │  Crystal  │
│ visible  │  clear    │
└──────────┴───────────┘
```

**Layout:**
- Split 50/50 vertical
- Left: Dark grey text on grey bg (simulate bad contrast)
- Right: White text on navy bg (good contrast)
- Big numbers: 2:1 vs 7.12:1
- Labels: "FAIL" vs "WCAG AA"

**Colors:**
- Left side: Desaturated, hard to read
- Right side: Vivid, easy to read
- Actual contrast difference visible

**Greifbar:** You FEEL the difference by looking

---

## Panel 3: "Grid System - Invisible but Felt"

**Visual:** Misaligned vs Aligned grids

```
┌─────────────────────┐
│ GRID ALIGNMENT      │
├──────────┬──────────┤
│ EYEBALL  │  8PX     │
│          │          │
│ ▭  ▭     │  ▭  ▭   │  ← Aligned
│  ▭   ▭   │  ▭  ▭   │  ← Perfect
│ ▭    ▭   │  ▭  ▭   │  ← Spacing
│          │          │
│ Looks    │ Pixel    │
│ okay     │ perfect  │
└──────────┴──────────┘
```

**Layout:**
- Left: Slightly off grid (2-3px variations)
- Right: Perfect 8px grid
- Overlay grid lines on right side
- Label: "You can't see 2px. But you feel it."

**Colors:**
- Left: Subtle red grid overlay (off)
- Right: Green grid overlay (perfect)
- Grid lines visible to show alignment

**Greifbar:** You see the grid, understand the precision

---

## Panel 4: "Agent Autonomy Spectrum"

**Visual:** Horizontal bar chart, 6 agents

```
AGENT AUTONOMY

Header        ████░░░░░░  40%  Fixed structure
Results       ███░░░░░░░  30%  Numbers + rules
Tech Stack    ██████░░░░  60%  Icon + layout
Timeline      █████░░░░░  50%  Data viz
Reality       ████████░░  80%  Story control
Learning      █████████░  90%  Pure creativity
```

**Layout:**
- 6 rows, each is an agent
- Bar shows autonomy level (filled vs empty)
- Percentage visible
- Short reason (3-4 words)

**Colors:**
- Low autonomy (20-40%): Grey bars
- Medium (50-60%): Blue bars
- High (70-90%): Green bars
- Gradient within bars

**Greifbar:** Bar length = freedom level, instantly clear

---

## Panel 5: "Timeline - 10 Hours Breakdown"

**Visual:** Horizontal timeline with colored segments

```
PHASE 2: 10 HOURS

0h   2h   4h   6h   8h   10h
├────┼────┼────┼────┼────┤
│████│████│████│    │    │  Try 1-3 (Fails)
│    │    │    │████│████│  Try 4+ (Works)
│    │    │    │    │░░░░│  Polish

█ Failed attempts (60%)
█ Working iterations (30%)
░ Final polish (10%)
```

**Layout:**
- Horizontal bar 0-10h
- Segments colored by outcome
- Red = fails, Yellow = working, Green = polish
- Percentages below

**Colors:**
- Red (#FF006E): Failed attempts (dominates)
- Yellow (#FFD93D): Working but iterating
- Green (#06FFA5): Final polish (small)

**Greifbar:** Most time = red (fails), that's the truth

---

## Panel 6: Results (Evolved)

**Visual:** Big numbers, meta-recursive

```
┌─────────────┐
│ RESULTS     │
│             │
│     3       │  Decision paths
│             │  visualized
│             │
│     8       │  Failed attempts
│             │  shown
│             │
│    27       │  Commits to
│             │  honesty
└─────────────┘
```

**Layout:**
- Same as Phase 1 Results panel
- But metrics about Phase 2 itself
- Meta: "We visualized 3 decisions, showed 8 fails"

**Greifbar:** Numbers tell the meta-story

---

## Panel 7-9: Keep from Phase 1

- **Tech Stack**: Python, PIL, cairosvg, Mermaid
- **Reality**: "Expected 6h → Reality 12h with decision trees"
- **Learning**: "Architecture is decisions. Decisions are stories. Show the fails."

---

## Visual Style Guide

**Colors:**
- ✅ Success: #06FFA5 (neon green)
- ❌ Fail: #FF006E (neon magenta)
- ⚠️ In Progress: #FFD93D (yellow)
- Background: #22223B (dark navy)
- Text: #F2F4F8 (off-white)

**Typography:**
- Decision titles: 24pt, bold
- Try numbers: 18pt, medium
- Reasons: 16pt, regular
- Numbers: 48-72pt for key metrics

**Icons:**
- ✅ = Success checkmark
- ❌ = Fail X
- ⚠️ = Warning triangle
- → = Progress arrow
- ░ = Empty/unfilled
- █ = Filled/completed

**Layout Rules:**
- Max 4 tries shown per decision
- Each try: Visual + Label + Result + Time
- Progress always left-to-right
- Fails in red, success in green
- Big numbers for impact

---

## Why This Works (SLC Check)

**Simple:**
- Visual progress bars (bars = intuitive)
- Before/After splits (instant understanding)
- Color coding (red = bad, green = good)
- No complex diagrams

**Lovable:**
- Shows fails honestly (relatable)
- Visual evolution (satisfying to see)
- Big numbers (impressive)
- Clean, modern aesthetic

**Complete:**
- All 3 major decisions covered
- Timeline shows full 10h
- Autonomy shows all 6 agents
- Nothing hidden

---

## Implementation Notes

### New Agent Needed: `decision_path_renderer.py`

```python
def render_decision_path(decision_data):
    """
    Renders 4-try visualization
    Input: {attempts: [{approach, result, time}]}
    Output: PIL Image with horizontal progress
    """
    # Create 4 boxes horizontally
    # Color by success/fail
    # Add icons (❌/✅)
    # Add labels
    return img
```

### New Agent: `autonomy_spectrum_renderer.py`

```python
def render_autonomy_bars(agents):
    """
    Renders 6 horizontal bars
    Input: [{agent: name, autonomy: 0-100, why: reason}]
    Output: PIL Image with color-coded bars
    """
    # 6 rows
    # Bars with gradient
    # Labels + percentages
    return img
```

### Reuse: Timeline from Phase 1

Can adapt timeline renderer for fail/success segments.

---

## The Story Phase 2 Tells

**Not:** "Here's our architecture"
**But:** "We tried 4 ways to render icons. 3 failed. Here's why."

**Not:** "Our system has 6 agents"
**But:** "Each agent has different freedom. Here's the spectrum."

**Not:** "We built it in 10 hours"
**But:** "60% of time was fails. That's normal. Here's the breakdown."

**Architecture through Decisions.**
**System through Stories.**
**Technical through Human.**

---

**Greifbar = You can point at the visual and understand it.**
**Anschaulich = You see the journey, not just the result.**
**SLC = Simple enough to get in 3 seconds, complete enough to be honest.**

---

Next: Implement these panels? 🚀
