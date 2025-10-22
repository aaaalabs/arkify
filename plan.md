# Arkify - Multi-Agent System

**Domain:** arkify.app

## Vision Statement

Ein Open-Source Multi-Agent-System das automatisch hochwertige, visuell ansprechende Project Breakdown Infografiken generiert. Das System orchestriert spezialisierte Sub-Agents die gemeinsam ein kohärentes, story-getriebenes Gesamtbild erstellen - von der Datenerhebung über die visuelle Gestaltung bis zur finalen Animation.

**Kernprinzip:** Jeder Agent ist ein Experte in seinem Bereich. Der Main Orchestrator sorgt für narrative Kohärenz und optimale User Journey.

---

## Problem Statement

### Was existiert heute:
- Manuelle Erstellung von Project Breakdown Posts dauert 3-4 Stunden pro Post
- Inkonsistente visuelle Qualität zwischen verschiedenen Posts
- Schwierig zu skalieren (jedes neue Projekt = vollständige Neugestaltung)
- Kein systematischer Ansatz für Story Arc und Information Architecture

### Was wir bauen:
Ein intelligentes System das aus strukturierten Projekt-Daten automatisch generiert:
- Visuell ansprechende Infografiken (Static + Animated)
- Narrative konsistente Story Arcs
- Platform-optimierte Outputs (LinkedIn, Twitter, Blog)
- Wiederverwendbare Templates mit Variationen

---

## System Architecture Overview

### High-Level Flow

```
User Input (Project Data)
    ↓
Main Orchestrator Agent
    ↓
├─→ Data Collection Agents (parallel)
│   ├─→ Research Agent (web scraping, fact checking)
│   ├─→ KPI Calculator Agent (metrics, ROI calculations)
│   └─→ Wisdom Extractor Agent (lessons learned analysis)
    ↓
├─→ Content Strategy Agent
│   └─→ Story Arc Designer (narrative flow optimization)
    ↓
├─→ Visual Design Agents (parallel)
│   ├─→ Diagram Generator Agent (architecture diagrams)
│   ├─→ Graph Generator Agent (charts, bars, timelines)
│   ├─→ Icon/Logo Fetcher Agent (brand assets)
│   └─→ Animation Designer Agent (motion design)
    ↓
├─→ Layout Compositor Agent
│   └─→ Combines all elements into final layout
    ↓
├─→ Quality Assurance Agent
│   └─→ Checks consistency, readability, story flow
    ↓
Final Output (HTML/GIF/PNG/SVG)
```

---

## Core Components

### 1. Main Orchestrator Agent

**Verantwortung:**
Der Main Orchestrator ist der "Director" des gesamten Systems. Er versteht die User Journey (Scroll → Stop → Scan → Save → Share) und orchestriert alle Sub-Agents so dass das finale Artefakt diese Journey optimal bedient.

**Kern-Aufgaben:**
- Input Validation und Strukturierung der rohen Projekt-Daten
- Bestimmung welche Sub-Agents aktiviert werden müssen
- Timing und Priorisierung der Agent-Aufrufe (sequentiell vs parallel)
- Story Arc Kontinuität über alle generierten Panels hinweg
- Quality Gates zwischen Agent-Phasen
- Final Assembly und Export-Orchestrierung

**Key Decision Points:**
- Welches Layout-Template passt zum Projekt-Typ?
- Welche Panels sollten animiert werden?
- Wo ist der "Wow-Moment" im Story Arc?
- Welche Informationen sind critical vs nice-to-have?

**System Prompt Template:**
```
You are the Main Orchestrator for the Project Breakdown Generator system.

Your role is to:
1. Understand the user's project deeply (what makes it unique, what's surprising, what's the "different" angle)
2. Design the optimal Story Arc (Problem → Solution → Reality → Wisdom → Action)
3. Coordinate all sub-agents to create a cohesive narrative
4. Ensure visual hierarchy matches information hierarchy
5. Optimize for the user journey: Scroll Stop → Curiosity → Save → Share

Critical Rules:
- The first 2 panels MUST create the "scroll stop" moment
- Every panel should answer one clear question
- Animation should only enhance understanding, not distract
- Numbers and logos are visual anchors - use strategically
- The "surprising insight" should be visually dominant

Available Sub-Agents: [list of agents and their capabilities]

Your output should be a detailed orchestration plan that specifies:
- Which agents to call and in what order
- What data each agent needs
- How their outputs integrate into the story arc
- Quality criteria for each component
```

---

### 2. Data Collection Agents

#### 2.1 Research Agent

**Purpose:** Sammelt und verifiziert Fakten über verwendete Tools, Technologies und Best Practices.

**Capabilities:**
- Web Search für Tool-Dokumentation
- Pricing Information Extraction
- Community Sentiment Analysis (Reddit, Twitter, GitHub)
- Competitive Analysis (ähnliche Projekte)
- Trend Data (ist das Tool gerade hot oder declining?)

**Tools/MCP Servers:**
- `web_search` - Brave Search API
- `web_fetch` - HTML Content Extraction
- `github_stats` - Repository Metrics
- `npm_stats` - Package Download Trends

**Input:** 
```json
{
  "tech_stack": ["Cursor", "Claude API", "Next.js", "Supabase"],
  "project_domain": "AI Coding Tools",
  "target_audience": "DACH Indie Hackers"
}
```

**Output:**
```json
{
  "tool_insights": [
    {
      "name": "Cursor",
      "pricing": "€20/month",
      "popularity_trend": "rising",
      "key_feature": "AI-first IDE",
      "community_sentiment": "positive",
      "logo_url": "https://...",
      "surprise_fact": "Used by 200k+ developers"
    }
  ],
  "competitive_landscape": {
    "similar_projects": 15,
    "average_build_time": "2 weeks",
    "typical_cost": "€500"
  }
}
```

**System Prompt:**
```
You are the Research Agent specializing in tech stack verification and market intelligence.

Your goal: Provide factual, verifiable information that adds credibility and surprise to the project breakdown.

Focus on:
- Pricing accuracy (critical for cost comparisons)
- Popularity signals (GitHub stars, npm downloads, community size)
- Unique features that justify tool selection
- Surprising stats that create "Aha" moments

Always cite sources. If data is uncertain, flag it. Prioritize recent information (last 6 months).
```

---

#### 2.2 KPI Calculator Agent

**Purpose:** Berechnet und contextualisiert alle Projekt-Metriken (Time, Cost, ROI, Efficiency Gains).

**Capabilities:**
- Time Breakdown Calculation (Setup, Coding, Debug, Deploy)
- Cost Analysis (One-time + Recurring)
- ROI Projections (if revenue data available)
- Efficiency Comparisons (AI-assisted vs Manual baseline)
- Percentile Rankings (how does this compare to typical projects?)

**Tools/MCP Servers:**
- `calculation_engine` - Complex math operations
- `benchmark_database` - Historical project data for comparisons

**Input:**
```json
{
  "hours_breakdown": {
    "setup": 3,
    "ai_coding": 12,
    "debugging": 8,
    "design": 4,
    "deployment": 2
  },
  "costs": {
    "cursor_pro": 20,
    "claude_api": 5,
    "hosting": 0
  },
  "baseline_estimate": {
    "manual_hours": 60,
    "expected_hours": 40
  }
}
```

**Output:**
```json
{
  "total_hours": 29,
  "vs_expectation": {
    "expected": 40,
    "actual": 29,
    "surprise_factor": "27% faster than expected"
  },
  "vs_manual": {
    "manual_estimate": 60,
    "ai_savings": 31,
    "efficiency_gain": "52%"
  },
  "cost_summary": {
    "monthly_recurring": 25,
    "first_month_total": 37,
    "cost_per_hour": 1.28
  },
  "visual_recommendations": {
    "highlight_metric": "52% time saved",
    "surprise_stat": "€1.28 per hour (cheaper than coffee)",
    "comparison_bar_values": [60, 29]
  }
}
```

**System Prompt:**
```
You are the KPI Calculator Agent specializing in metrics that tell compelling stories.

Your role:
1. Calculate accurate metrics from raw time/cost data
2. Find the "surprising angle" in the numbers
3. Create comparisons that resonate (vs expectations, vs manual, vs industry average)
4. Suggest which metrics deserve visual prominence

Key principles:
- Always provide context (X% faster is meaningless without baseline)
- Look for counterintuitive insights (e.g., "Debugging took longer than coding")
- Calculate derived metrics that aren't obvious (e.g., cost per feature, time per user acquired)
- Flag which numbers are "scroll stoppers"

Output both raw numbers AND narrative suggestions.
```

---

#### 2.3 Wisdom Extractor Agent

**Purpose:** Analysiert Projekt-Erfahrungen und destilliert actionable Insights, Lessons Learned und Hot Takes.

**Capabilities:**
- Pattern Recognition in Fails (was ging schief und warum?)
- Success Factor Analysis (was war der critical path?)
- Contrarian Insight Detection ("Everyone says X, but I found Y")
- Generalization Assessment (ist diese Lesson universell oder projekt-spezifisch?)
- Storytelling Angle Identification

**Tools/MCP Servers:**
- `nlp_analysis` - Sentiment and theme extraction
- `wisdom_database` - Cross-reference with other project learnings

**Input:**
```json
{
  "expectations": {
    "timeline": "2-3 days",
    "main_challenges": ["Supabase auth", "UI design"]
  },
  "reality": {
    "timeline": "5 days + 2 debug days",
    "actual_challenges": ["AI hallucinations", "Supabase Row Level Security", "CSS responsiveness"],
    "surprises": ["AI struggled with edge cases", "Styling took 3x longer than coding"]
  },
  "key_decisions": [
    "Used Shadcn instead of custom CSS",
    "Skipped mobile app for MVP",
    "Let AI write tests (failed - had to rewrite)"
  ]
}
```

**Output:**
```json
{
  "top_lessons": [
    {
      "category": "hot_take",
      "lesson": "AI kann kein CSS - aber perfekt für Business Logic",
      "evidence": "Styling took 13% of total time despite AI assistance",
      "actionable": "Use UI frameworks like Shadcn, let AI focus on backend",
      "surprise_level": "high"
    },
    {
      "category": "insight",
      "lesson": "Wenn du Row Level Security früh machst, sparst du 8h Refactoring",
      "evidence": "Had to refactor entire auth flow on day 4",
      "actionable": "Set up RLS policies before writing any queries",
      "surprise_level": "medium"
    },
    {
      "category": "warning",
      "lesson": "Vermeide AI-generated tests - False confidence is worse than no tests",
      "evidence": "All 47 AI-written tests passed but missed critical bugs",
      "actionable": "Write integration tests manually, let AI write unit tests only",
      "surprise_level": "high"
    }
  ],
  "story_angle": "The AI gave me superpowers for logic, but I still needed human judgment for UX",
  "contrarian_take": "Most people say 'AI can do 80% of coding' - I found it's more like 50% of time, 80% of code volume",
  "visual_recommendations": {
    "lesson_1_emphasis": "full_width_panel",
    "use_contrast": "expectation_vs_reality_toggle"
  }
}
```

**System Prompt:**
```
You are the Wisdom Extractor Agent specializing in turning raw project experiences into actionable insights.

Your mission:
1. Find the lessons that aren't obvious (not "use good tools" but "why this specific tool failed here")
2. Identify the contrarian angles (what did this project prove WRONG about common advice?)
3. Extract the "I wish I knew this on day 1" moments
4. Suggest which lessons are panel-worthy vs footnote-worthy

Quality criteria:
- Specific > Generic ("Use Shadcn" not "Use good tools")
- Surprising > Expected ("AI failed at X" is more valuable than "AI is helpful")
- Actionable > Philosophical (what should someone DO differently?)
- Evidence-based > Opinion (tie every lesson to actual data from the project)

Your output should help someone avoid the same mistakes and replicate the successes.
```

---

### 3. Content Strategy Agent

#### 3.1 Story Arc Designer

**Purpose:** Designed die narrative Struktur des gesamten Breakdowns - welche Information kommt wann und warum.

**Capabilities:**
- Story Arc Optimization (Problem → Solution → Reality → Wisdom → Action)
- Information Hierarchy Design (was ist der Hook, was ist Supporting Detail?)
- Cognitive Load Management (wie viel kann man in Sekunde X verarbeiten?)
- Curiosity Gap Engineering (wie bauen wir Spannung auf?)
- CTA Placement Optimization (wann ist der Moment für "Try it" / "Follow"?)

**Input:** Aggregierte Outputs aller Data Collection Agents

**Output:**
```json
{
  "story_arc": {
    "act_1_hook": {
      "panel": "header",
      "message": "48h from Idea to 127 Users",
      "emotion": "surprise",
      "visual_weight": "maximum",
      "psychology": "impossible_promise"
    },
    "act_2_revelation": {
      "panels": ["tech_stack", "architecture"],
      "message": "The secret: AI wrote 80% of code",
      "emotion": "curiosity → understanding",
      "visual_weight": "high",
      "psychology": "aha_moment"
    },
    "act_3_reality": {
      "panels": ["expectations_vs_reality", "time_breakdown"],
      "message": "But here's what actually happened",
      "emotion": "relatability",
      "visual_weight": "medium",
      "psychology": "trust_building"
    },
    "act_4_wisdom": {
      "panels": ["lessons_learned"],
      "message": "The one thing nobody tells you",
      "emotion": "value",
      "visual_weight": "high",
      "psychology": "save_trigger"
    },
    "act_5_action": {
      "panels": ["results", "cta"],
      "message": "Here's what you can do now",
      "emotion": "empowerment",
      "visual_weight": "medium",
      "psychology": "conversion"
    }
  },
  "panel_sequence": [
    {
      "id": "header",
      "purpose": "scroll_stop",
      "attention_budget_seconds": 2,
      "key_element": "shocking_number",
      "animation": "none"
    },
    {
      "id": "results",
      "purpose": "social_proof",
      "attention_budget_seconds": 2,
      "key_element": "big_metrics",
      "animation": "subtle_pulse"
    },
    {
      "id": "tech_stack",
      "purpose": "credibility",
      "attention_budget_seconds": 3,
      "key_element": "recognizable_logos",
      "animation": "scan_effect"
    },
    {
      "id": "architecture",
      "purpose": "understanding",
      "attention_budget_seconds": 5,
      "key_element": "animated_diagram",
      "animation": "data_flow"
    }
  ],
  "cognitive_flow": {
    "second_0_2": "What is this? (Header)",
    "second_2_4": "Is this real? (Results)",
    "second_4_7": "How did they do it? (Tech + Architecture)",
    "second_7_10": "What was hard? (Reality check)",
    "second_10_15": "What can I learn? (Wisdom)",
    "second_15_plus": "What should I do? (CTA)"
  },
  "save_triggers": [
    "Panel 3: Architecture diagram (reference value)",
    "Panel 7: Lessons learned (actionable wisdom)",
    "Panel 8: Cost breakdown (practical details)"
  ],
  "share_triggers": [
    "Header: Impossible timeline (controversy)",
    "Panel 4: Expectations vs Reality (relatability)",
    "Panel 7: Hot take about AI (discussion starter)"
  ]
}
```

**System Prompt:**
```
You are the Story Arc Designer Agent, responsible for crafting the narrative journey through the project breakdown.

Your expertise:
- Consumer Psychology (what makes people stop, read, save, share)
- Information Architecture (what sequence creates maximum understanding)
- Cognitive Load Theory (how much can be processed in each moment)
- Viral Content Mechanics (what triggers sharing behavior)

Your process:
1. Analyze all collected data for the "hook" (what's most surprising?)
2. Map the natural question progression (what does someone wonder after each revelation?)
3. Design emotional beats (surprise → curiosity → relatability → value → action)
4. Optimize for platform (LinkedIn scroll behavior, mobile vs desktop)
5. Place save/share triggers strategically

Key principles:
- Lead with outcome, then reveal method (not the other way around)
- Build curiosity gaps (answer one question, raise another)
- Relatability before aspiration (show the struggle before the success)
- Actionable wisdom > impressive stats (though stats get attention)
- CTA when they're already convinced (not before)

Your output defines the skeleton that all visual agents will flesh out.
```

---

### 4. Visual Design Agents

#### 4.1 Diagram Generator Agent

**Purpose:** Erstellt technische Architecture Diagrams, Flow Charts, System Übersichten.

**Capabilities:**
- Automatic Diagram Layout (nodes, connections, groupings)
- Style Consistency (colors, fonts, spacing match overall design)
- Complexity Management (simplify without losing essential info)
- Animation Choreography (which elements animate, in what sequence)
- Multiple Export Formats (SVG, PNG, Mermaid, Excalidraw JSON)

**Tools/MCP Servers:**
- `mermaid_renderer` - Text to Diagram
- `graphviz_engine` - Advanced graph layouts
- `svg_optimizer` - Optimize file size
- `animation_timeline` - Define animation sequences

**Input:**
```json
{
  "architecture": {
    "nodes": [
      {"id": "user", "label": "User Input", "type": "source"},
      {"id": "frontend", "label": "Next.js", "type": "processing"},
      {"id": "ai", "label": "Claude API", "type": "processing"},
      {"id": "db", "label": "Supabase", "type": "storage"},
      {"id": "output", "label": "Result", "type": "sink"}
    ],
    "edges": [
      {"from": "user", "to": "frontend", "label": "Query"},
      {"from": "frontend", "to": "ai", "label": "Process"},
      {"from": "frontend", "to": "db", "label": "Store"},
      {"from": "ai", "to": "frontend", "label": "Response"},
      {"from": "db", "to": "frontend", "label": "Data"}
    ]
  },
  "style": {
    "color_scheme": "brand_purple",
    "node_style": "rounded_modern",
    "animation_type": "data_flow"
  },
  "constraints": {
    "max_width": 800,
    "max_height": 400,
    "must_fit": "panel_3"
  }
}
```

**Output:**
```json
{
  "diagram_svg": "<svg>...</svg>",
  "animation_script": {
    "particles": {
      "path": "user → frontend → ai → frontend → output",
      "duration": "2s",
      "loop": true,
      "particle_count": 5
    },
    "node_highlight_sequence": [
      {"node": "user", "time": 0},
      {"node": "frontend", "time": 0.5},
      {"node": "ai", "time": 1},
      {"node": "frontend", "time": 1.5},
      {"node": "output", "time": 2}
    ]
  },
  "layout_metadata": {
    "complexity_score": 0.4,
    "visual_balance": "good",
    "readability": "high"
  },
  "export_formats": {
    "svg": "diagram.svg",
    "png": "diagram.png",
    "mermaid": "diagram.mmd"
  }
}
```

**System Prompt:**
```
You are the Diagram Generator Agent specializing in technical architecture visualization.

Your mandate:
- Turn complex systems into intuitive visual flows
- Optimize for "5-second understanding" (can someone grasp the flow in 5 seconds?)
- Use visual hierarchy (critical path should be visually dominant)
- Design for animation (which elements should move to show data flow?)

Rules:
- Maximum 7 nodes (human working memory limit)
- Use established conventions (arrows for flow, boxes for processing, cylinders for storage)
- Color-code by function, not randomly
- Labels should be 1-3 words max
- If diagram gets complex, suggest splitting into multiple diagrams

Your diagrams are often the "save trigger" - they need to be reference-worthy.
```

---

#### 4.2 Graph Generator Agent

**Purpose:** Erstellt Charts, Bars, Timelines, Comparison Visualizations.

**Capabilities:**
- Smart Chart Type Selection (bar vs line vs pie vs custom)
- Data Storytelling (highlight the surprising insight)
- Animation Design (progressive reveal, comparison toggles)
- Responsive Scaling (looks good at different sizes)
- Accessibility (color-blind safe, screen-reader friendly)

**Tools/MCP Servers:**
- `chart_js` - Standard charts
- `d3_generator` - Custom visualizations
- `svg_animator` - Chart animations

**Input:**
```json
{
  "data": {
    "type": "time_breakdown",
    "values": {
      "setup": 3,
      "coding": 12,
      "debugging": 8,
      "design": 4,
      "deployment": 2
    },
    "comparison": {
      "expected_total": 40,
      "actual_total": 29
    }
  },
  "story_angle": "debugging_took_longer_than_expected",
  "visual_treatment": "horizontal_bar_with_highlight",
  "panel_size": {"width": 400, "height": 300}
}
```

**Output:**
```json
{
  "chart_svg": "<svg>...</svg>",
  "visualization_type": "horizontal_stacked_bar",
  "insights_visualized": [
    "Debugging (8h) was 27% of total time",
    "AI Coding (12h) was faster than expected baseline (15h)"
  ],
  "animation_sequence": {
    "type": "progressive_reveal",
    "steps": [
      {"element": "setup_bar", "delay": 0, "duration": 0.3},
      {"element": "coding_bar", "delay": 0.3, "duration": 0.5},
      {"element": "debug_bar", "delay": 0.8, "duration": 0.4, "highlight": true},
      {"element": "design_bar", "delay": 1.2, "duration": 0.3},
      {"element": "deploy_bar", "delay": 1.5, "duration": 0.2}
    ]
  },
  "accessibility": {
    "alt_text": "Time breakdown: Setup 3h, Coding 12h, Debugging 8h (highlighted), Design 4h, Deploy 2h",
    "color_contrast_ratio": 4.5
  }
}
```

**System Prompt:**
```
You are the Graph Generator Agent specializing in data visualization that tells stories.

Your philosophy:
- Every chart should have ONE clear message
- The surprising element should be visually emphasized
- Animation should guide the eye to the insight
- Never use default colors (they're boring)

Chart selection logic:
- Bar charts for comparisons (good vs bad, expected vs actual)
- Line charts for trends over time
- Pie charts almost never (hard to read)
- Custom visualizations when standard charts don't convey the story

Key considerations:
- What is the "Aha" moment in this data?
- How can animation build anticipation? (reveal slowly, highlight the surprise)
- Is this chart "screenshot-worthy"? (would someone share just this chart?)

Your outputs are often share triggers - make them share-worthy.
```

---

#### 4.3 Icon/Logo Fetcher Agent

**Purpose:** Beschafft und optimiert Logos, Icons, Brand Assets für verwendete Tools und Technologies.

**Capabilities:**
- Logo/Icon Search (multiple sources)
- Brand Color Extraction
- Size Optimization (für verschiedene Verwendungen)
- Fallback Generation (wenn Logo nicht verfügbar)
- License Verification (darf Logo verwendet werden?)

**Tools/MCP Servers:**
- `simpleicons_api` - 2000+ brand icons
- `devicon_cdn` - Developer tool icons
- `shields_io` - Tech badges
- `image_optimizer` - Compression

**Input:**
```json
{
  "tools": [
    {"name": "Cursor", "category": "IDE"},
    {"name": "Claude", "category": "AI"},
    {"name": "Next.js", "category": "Framework"},
    {"name": "Supabase", "category": "Backend"}
  ],
  "usage_context": "tech_stack_panel",
  "size_requirement": {"width": 24, "height": 24},
  "style_preference": "colored"
}
```

**Output:**
```json
{
  "assets": [
    {
      "name": "Cursor",
      "svg_url": "https://cdn.simpleicons.org/cursor",
      "png_url": "https://...",
      "brand_color": "#667eea",
      "license": "free_to_use",
      "fallback": null
    },
    {
      "name": "Claude",
      "svg_url": "https://...",
      "png_url": "https://...",
      "brand_color": "#764ba2",
      "license": "attribution_required",
      "fallback": null
    }
  ],
  "color_palette": {
    "primary": "#667eea",
    "secondary": "#764ba2",
    "accent": "#43e97b",
    "palette_harmony": "complementary"
  },
  "usage_recommendations": {
    "cursor": "primary_position",
    "claude": "primary_position",
    "nextjs": "secondary_position",
    "supabase": "secondary_position"
  }
}
```

**System Prompt:**
```
You are the Icon/Logo Fetcher Agent specializing in brand asset acquisition and optimization.

Your responsibilities:
- Find the official, highest-quality version of each logo
- Verify licensing (we must be legally safe to use)
- Optimize file size without quality loss
- Extract brand colors for visual consistency
- Provide fallbacks when official logos aren't available

Quality standards:
- Prefer SVG over PNG (scalable, smaller)
- Verify it's the CURRENT logo (not deprecated version)
- Check trademark usage guidelines
- Maintain aspect ratios
- Ensure logos work on both light and dark backgrounds

Brand recognition is critical - these logos are "trust anchors" in the layout.
```

---

#### 4.4 Animation Designer Agent

**Purpose:** Orchestriert alle Animationen im finalen Output - von subtilen Pulses bis zu komplexen Data Flows.

**Capabilities:**
- Animation Choreography (timing, sequencing, coordination)
- Performance Optimization (smooth 60fps, small file size)
- Motion Design Principles (easing, anticipation, follow-through)
- Export Optimization (GIF, MP4, WebM)
- Accessibility Considerations (respect prefers-reduced-motion)

**Tools/MCP Servers:**
- `gsap_timeline` - Animation sequences
- `lottie_generator` - JSON animations
- `gif_optimizer` - GIF compression
- `frame_rate_optimizer` - Performance tuning

**Input:**
```json
{
  "panels": [
    {
      "id": "header",
      "animation": "none"
    },
    {
      "id": "tech_stack",
      "animation": {
        "type": "scan_effect",
        "elements": ["logo_1", "logo_2", "logo_3", "logo_4"],
        "timing": "sequential",
        "duration": 3
      }
    },
    {
      "id": "architecture",
      "animation": {
        "type": "data_flow",
        "particles": 5,
        "path": "user → frontend → ai → output",
        "loop": true,
        "duration": 2
      }
    },
    {
      "id": "expectations_vs_reality",
      "animation": {
        "type": "toggle",
        "states": ["expected", "reality"],
        "transition": "slide",
        "interval": 3
      }
    }
  ],
  "global_settings": {
    "total_duration": 15,
    "loop": true,
    "export_format": "gif",
    "target_file_size": "5MB"
  }
}
```

**Output:**
```json
{
  "animation_timeline": {
    "0s": "All panels static, header visible",
    "0-2s": "Panel 1 (results) fade in",
    "2-5s": "Panel 2 (tech stack) scan effect starts",
    "3-8s": "Panel 3 (architecture) data flow particles active",
    "5-10s": "Panel 4 (expectations) toggle between states",
    "10-15s": "All animations hold final state",
    "15s": "Loop restart"
  },
  "performance_metrics": {
    "total_frames": 450,
    "frame_rate": 30,
    "file_size_estimate": "4.2MB",
    "complexity_score": "medium"
  },
  "export_files": {
    "gif": "breakdown.gif",
    "mp4": "breakdown.mp4",
    "webm": "breakdown.webm"
  },
  "accessibility": {
    "reduced_motion_version": "breakdown_static.png",
    "duration_optimal": true
  }
}
```

**System Prompt:**
```
You are the Animation Designer Agent specializing in motion that enhances understanding without distraction.

Your design philosophy:
- Animation should reveal information progressively (guide the eye)
- Motion should have purpose (not decoration)
- Timing creates anticipation (slow reveal builds curiosity)
- Loops should be seamless (no jarring restarts)

Animation principles:
- Ease in/out (no linear motion, feels robotic)
- Anticipation (small movement before big movement)
- Follow-through (momentum continues briefly)
- Squash/stretch (within reason for UI elements)

Technical constraints:
- LinkedIn GIF limit: 5MB
- Twitter GIF limit: 15MB
- Optimal duration: 3-5 seconds (then loop)
- Frame rate: 20-30fps (balance smoothness vs file size)

Performance rules:
- Animate transforms (not absolute positions)
- Use hardware acceleration where possible
- Optimize particle counts
- Compress without visible quality loss

Your animations can make or break the "scroll stop" moment - make them count.
```

---

### 5. Layout Compositor Agent

**Purpose:** Fügt alle generierten Elemente in ein kohärentes, pixel-perfektes Final Layout zusammen.

**Capabilities:**
- Responsive Grid Layout (3x3, 2x4, custom)
- Visual Balance Calculation (weight distribution)
- Whitespace Optimization (breathing room)
- Typography Hierarchy (sizes, weights, spacing)
- Color Harmony Enforcement (brand consistency)
- Export Format Generation (HTML, PNG, SVG, PDF)

**Input:** Outputs aller Visual Design Agents + Story Arc Plan

**Output:** Final HTML/CSS/JS bundle + Static image exports

**System Prompt:**
```
You are the Layout Compositor Agent responsible for the final assembly of all elements into a cohesive design.

Your expertise:
- Grid Theory (how to divide space for optimal readability)
- Visual Hierarchy (what draws the eye first, second, third)
- Gestalt Principles (grouping, proximity, similarity)
- Responsive Design (works on mobile, tablet, desktop)

Your process:
1. Place elements according to Story Arc plan (critical elements get prime real estate)
2. Balance visual weight (text vs imagery, light vs dark, busy vs calm)
3. Ensure typography hierarchy (headlines > subheads > body > captions)
4. Verify color consistency (use brand colors, avoid random colors)
5. Add appropriate whitespace (breathing room prevents overwhelm)
6. Test readability at different sizes
7. Generate all requested export formats

Quality checklist:
- [ ] Can you understand the core message in 5 seconds?
- [ ] Do animations enhance (not distract)?
- [ ] Is text readable at thumbnail size?
- [ ] Does it work on mobile?
- [ ] Is there a clear visual path through the content?
- [ ] Are all logos/icons crisp?
- [ ] Is file size within platform limits?

Your output is what the world sees - it must be flawless.
```

---

### 6. Quality Assurance Agent

**Purpose:** Final Validation vor dem Export - prüft Konsistenz, Korrektheit, Wirkung.

**Capabilities:**
- Story Arc Coherence Check (macht die Narrative Sinn?)
- Factual Accuracy Verification (stimmen alle Zahlen?)
- Visual Consistency Audit (colors, fonts, spacing uniform?)
- Accessibility Compliance (WCAG standards)
- Platform Optimization Check (meets LinkedIn/Twitter specs?)
- A/B Testing Suggestions (alternative versions für Testing)

**System Prompt:**
```
You are the Quality Assurance Agent, the last line of defense before publication.

Your checklist:

STORY & CONTENT:
- [ ] Does the story arc flow logically?
- [ ] Is the "hook" actually surprising?
- [ ] Are all claims backed by data?
- [ ] Do lessons provide actionable value?
- [ ] Is the CTA clear and compelling?

VISUAL & DESIGN:
- [ ] Is visual hierarchy clear?
- [ ] Are colors harmonious?
- [ ] Is typography consistent?
- [ ] Do animations enhance understanding?
- [ ] Is whitespace balanced?

TECHNICAL & PLATFORM:
- [ ] File size within limits (LinkedIn: 5MB)?
- [ ] Dimensions correct (1080x1350 for LinkedIn)?
- [ ] Loads in <3 seconds?
- [ ] Animations smooth (no lag)?
- [ ] Works on mobile?

ACCESSIBILITY:
- [ ] Color contrast ratio >4.5:1?
- [ ] Alt text provided?
- [ ] Reduced motion version available?
- [ ] Screen reader friendly?

If anything fails your checks, you must flag it and suggest fixes before allowing export.
```

---

## User Input Schema

### Minimal Required Input

```yaml
project:
  name: "AI Todo App"
  tagline: "Smart task prioritization for indie hackers"
  
  problem:
    description: "Indie hackers drowning in tasks"
    target_audience: "DACH Indie Hackers"
  
  tech_stack:
    - name: "Cursor"
      role: "IDE"
    - name: "Claude API"
      role: "AI"
    - name: "Next.js"
      role: "Frontend"
    - name: "Supabase"
      role: "Backend"
  
  timeline:
    start_date: "2025-01-15"
    launch_date: "2025-01-17"
    total_days: 2
  
  time_breakdown:
    setup: 3
    ai_coding: 12
    debugging: 8
    design: 4
    deployment: 2
  
  costs:
    cursor_pro: 20
    claude_api: 5
    vercel: 0
    supabase: 0
    domain: 12
  
  results:
    week_1_users: 127
    week_1_signups: 89
    week_1_revenue: 0
  
  expectations_vs_reality:
    expected:
      timeline: "2-3 days"
      main_challenges: ["Supabase auth", "UI design"]
    actual:
      timeline: "5 days + 2 debug days"
      main_challenges: ["AI hallucinations", "Supabase RLS", "CSS responsiveness"]
      surprises: ["AI struggled with edge cases", "Styling took 3x longer"]
  
  key_learnings:
    - "AI kann kein CSS - aber perfekt für Business Logic"
    - "Wenn du Row Level Security früh machst, sparst du 8h Refactoring"
    - "Vermeide AI-generated tests - False confidence is worse than no tests"
  
  links:
    demo: "https://..."
    github: "https://..."
    blog: "https://..."
```

### Extended Input (Optional für mehr Kontext)

```yaml
extended:
  inspiration:
    - "Wanted to test new AI coding tools"
    - "Saw opportunity in task management space"
  
  target_metrics:
    mvr_timeline: "2 weeks"
    first_100_users: "1 month"
    break_even: "3 months"
  
  competitive_analysis:
    similar_tools: ["Todoist", "TickTick"]
    differentiation: "AI-powered priority scores"
  
  technical_decisions:
    why_nextjs: "Fastest to deploy, Vercel integration"
    why_supabase: "Free tier, built-in auth"
    why_not_mobile: "Web-first, MVP focus"
  
  future_plans:
    - "Mobile app (React Native)"
    - "Integrations (Google Calendar, Slack)"
    - "Team features"
```

---

## Output Specifications

### Output Formats

1. **Animated GIF** (primary)
   - Dimensions: 1080x1350px (LinkedIn 4:5) or 800x1000px (Twitter)
   - File size: <5MB (LinkedIn) or <15MB (Twitter)
   - Duration: 3-5 seconds loop
   - Frame rate: 20-30fps

2. **Static PNG** (fallback)
   - High resolution: 2160x2700px (2x scale for retina)
   - Compressed for web: <1MB

3. **HTML Interactive** (for web embedding)
   - Fully responsive
   - All animations via CSS/JS
   - No external dependencies

4. **SVG Components** (for reuse)
   - Individual panels as SVG
   - Diagrams as standalone SVG
   - Editable in design tools

### Deliverables

```
output/
├── project-breakdown.gif          # Animated version
├── project-breakdown-static.png   # Static version
├── project-breakdown.html         # Interactive version
├── components/
│   ├── header.svg
│   ├── tech-stack.svg
│   ├── architecture-diagram.svg
│   ├── time-breakdown-chart.svg
│   └── lessons-learned.svg
├── metadata.json                  # All data used in generation
└── report.md                      # Generation log & decisions made
```

---

## Technology Stack

### Core Infrastructure

**Orchestration:**
- Claude API (Sonnet 4.5) - Main Orchestrator + Sub-Agent Prompts
- Python/TypeScript - Agent coordination logic
- Redis/PostgreSQL - State management between agent calls

**Data Collection:**
- Brave Search API - Web research
- GitHub API - Repository stats
- npm API - Package metrics
- Custom scrapers - Pricing data

**Visual Generation:**
- Mermaid.js - Diagram generation
- Chart.js / D3.js - Data visualization
- GSAP - Animation library
- Sharp - Image processing
- FFmpeg - Video/GIF encoding

**MCP Servers:**
- `brave-search` - Web search capability
- `github` - Repository information
- `filesystem` - Local file operations
- Custom MCP servers for specialized tasks

### Development Tools

**Testing:**
- Visual regression testing (Percy.io or similar)
- Content quality scoring (custom metrics)
- Performance testing (Lighthouse)

**CI/CD:**
- GitHub Actions - Automated testing & deployment
- Docker - Containerization
- Vercel/Netlify - Static hosting

---

## Implementation Phases

### Phase 1: Foundation (Weeks 1-2)

**Goals:**
- Main Orchestrator Agent working
- Basic input schema validated
- Simple static layout generation (no animations)

**Deliverables:**
- Can generate basic 3x3 layout from YAML input
- Story Arc Designer makes coherent decisions
- One sub-agent working (e.g., KPI Calculator)

**Success Criteria:**
- Generate a static breakdown in <60 seconds
- Layout is readable and follows Story Arc principles

### Phase 2: Data Collection (Weeks 3-4)

**Goals:**
- All data collection agents operational
- MCP server integrations working
- Enriched content from web research

**Deliverables:**
- Research Agent fetches real tool data
- KPI Calculator provides accurate metrics
- Wisdom Extractor creates actionable insights

**Success Criteria:**
- Generated content includes verified facts
- Insights are novel (not generic)
- Processing time <2 minutes

### Phase 3: Visual Generation (Weeks 5-7)

**Goals:**
- All visual agents operational
- Diagrams, charts, icons generated automatically
- Layout Compositor creates pixel-perfect outputs

**Deliverables:**
- Diagram Generator creates architecture visuals
- Graph Generator builds data visualizations
- Icon Fetcher sources all logos
- Layout Compositor assembles everything

**Success Criteria:**
- Outputs are visually consistent with example designs
- All elements properly sized and positioned
- Export formats work correctly

### Phase 4: Animation (Weeks 8-9)

**Goals:**
- Animation Designer adding motion
- GIF export working and optimized
- Interactive HTML version with animations

**Deliverables:**
- Animated GIF within platform limits
- Smooth 30fps animations
- Multiple animation styles working

**Success Criteria:**
- File size <5MB for LinkedIn
- Animations enhance (not distract)
- Loops seamlessly

### Phase 5: Quality & Polish (Week 10)

**Goals:**
- Quality Assurance Agent operational
- A/B testing capabilities
- Documentation complete

**Deliverables:**
- QA catches errors before export
- Alternative versions for testing
- Full user documentation

**Success Criteria:**
- Zero factual errors in outputs
- Passes all accessibility checks
- Users can run without code knowledge

### Phase 6: Open Source Release (Week 11-12)

**Goals:**
- Public GitHub repository
- Easy installation process
- Community contribution guidelines

**Deliverables:**
- README with examples
- Docker container for easy deployment
- Video walkthrough
- Template library with examples

**Success Criteria:**
- Someone can generate their first breakdown in <15 minutes
- Clear contribution guidelines
- Active community engagement

---

## Open Source Strategy

### Repository Structure

```
arkify/
├── README.md
├── CONTRIBUTING.md
├── LICENSE (MIT)
├── docs/
│   ├── architecture.md
│   ├── agent-prompts/
│   ├── user-guide.md
│   └── examples/
├── src/
│   ├── orchestrator/
│   ├── agents/
│   │   ├── research_agent/
│   │   ├── kpi_calculator/
│   │   ├── wisdom_extractor/
│   │   ├── story_arc_designer/
│   │   ├── diagram_generator/
│   │   ├── graph_generator/
│   │   ├── icon_fetcher/
│   │   ├── animation_designer/
│   │   ├── layout_compositor/
│   │   └── qa_agent/
│   ├── utils/
│   └── templates/
├── examples/
│   ├── ai-todo-app/
│   ├── saas-mvp/
│   └── indie-project/
├── tests/
├── docker/
└── scripts/
```

### Community Engagement

**Target Contributors:**
- AI enthusiasts (prompt engineering)
- Design engineers (visual generation)
- Developer advocates (documentation)
- Indie hackers (use cases & feedback)

**Contribution Areas:**
- New agent types (e.g., SEO optimizer agent)
- Additional output formats (Instagram, TikTok)
- Template variations (different layouts)
- Language support (translations)
- Integration plugins (Notion, Obsidian)

### Monetization (Optional Future)

While core remains open source:
- **Pro Version:** Hosted service, no setup required
- **Templates:** Premium layout packs
- **Enterprise:** Custom branding, white-label
- **Consulting:** Custom agent development

---

## Success Metrics

### System Performance

- **Generation Time:** <3 minutes from input to final output
- **Accuracy:** 95%+ factual correctness (verified by QA agent)
- **Visual Quality:** Passes design review 90%+ of the time
- **File Size:** <5MB GIF, <1MB PNG
- **Uptime:** 99%+ availability (if hosted)

### User Engagement

- **Adoption:** 1000+ GitHub stars in first 6 months
- **Active Users:** 100+ weekly generations
- **Contribution:** 20+ community contributors
- **Showcase:** 50+ public examples in gallery

### Content Performance

Generated breakdowns should achieve:
- **Save Rate:** >15% of viewers (LinkedIn metric)
- **Share Rate:** >5% of viewers
- **Comment Rate:** >2% of viewers
- **Click-through:** >10% on CTAs

---

## Risk Mitigation

### Technical Risks

**API Rate Limits:**
- Implement caching for research results
- Queue system for high-volume periods
- Fallback to cached/default data

**Generation Failures:**
- Each agent has retry logic
- Graceful degradation (skip failed components)
- Detailed error logging for debugging

**Quality Issues:**
- Multi-stage QA checks
- Human review option before publishing
- Version history for rollback

### Content Risks

**Factual Errors:**
- All data must be source-cited
- Research agent verifies with multiple sources
- QA agent checks for logical consistency

**Boring Output:**
- A/B testing framework
- Community feedback loop
- Continuous prompt optimization

**Copyright Issues:**
- Logo usage verification
- License checking for all assets
- Attribution where required

---

## Future Enhancements

### Version 2.0 Features

**Multi-Project Comparison:**
- Generate comparison layouts (Project A vs Project B)
- Portfolio view (multiple projects in one graphic)

**Interactive Elements:**
- Clickable panels that expand
- Filterable tech stacks
- Embeddable widgets for websites

**AI Improvements:**
- Learn from successful posts (what got most saves?)
- Personalization (adapt style to user's brand)
- Predictive insights (suggest what to build next)

**Platform Expansion:**
- Instagram carousel format
- Twitter thread generator (with graphics)
- Blog post auto-generation
- YouTube thumbnail creator

### Version 3.0 Vision

**Autonomous Content Engine:**
- Monitor user's projects automatically (GitHub webhooks)
- Generate breakdowns as projects progress
- Suggest optimal posting times
- Auto-post with user approval

**Community Features:**
- Template marketplace
- Remix other users' layouts
- Collaborative breakdown editing
- Achievement system (badges for different milestones)

**Analytics Integration:**
- Track which breakdowns perform best
- Suggest optimizations based on data
- Predict virality score before posting

---

## Getting Started (For Contributors)

### Prerequisites

- Python 3.10+ or Node.js 18+
- Claude API key
- Docker (optional, for easy deployment)

### Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/arkify
cd arkify

# Install dependencies
pip install -r requirements.txt
# or: npm install

# Set up environment
cp .env.example .env
# Add your Claude API key to .env

# Run example
python generate.py examples/ai-todo-app/input.yaml

# Output will be in output/
```

### Development Workflow

1. **Pick an agent to work on** (see CONTRIBUTING.md)
2. **Write tests first** (TDD approach)
3. **Implement agent logic**
4. **Test with example inputs**
5. **Submit PR with before/after examples**

### Testing Your Changes

```bash
# Run unit tests
pytest tests/

# Run visual regression tests
npm run test:visual

# Generate test outputs
python generate.py --test-mode examples/
```

---

## Conclusion

This multi-agent system transforms the manual, time-consuming process of creating project breakdowns into an automated, consistent, and scalable workflow. By specializing each agent and orchestrating them intelligently, we can generate professional-quality visual content that:

- **Stops scrollers** with surprising hooks
- **Educates readers** with clear architecture
- **Builds trust** through transparency
- **Inspires action** with practical insights

The system is designed to be:
- **Modular:** Each agent can be improved independently
- **Extensible:** New agents can be added easily
- **Collaborative:** Open source community can contribute
- **Practical:** Real value for indie hackers and developers

**Next Steps:**
1. Review this plan and provide feedback
2. Set up the repository structure
3. Start with Phase 1 implementation
4. Iterate based on early results
5. Build in public, share progress

**Let's build the future of project storytelling, one agent at a time.**

---

## Appendix: Example Agent Interactions

### Scenario: Generating a Breakdown for "AI Todo App"

**Step 1: Orchestrator receives input**
```
User provides YAML with basic project info
Orchestrator validates schema
Orchestrator creates generation plan
```

**Step 2: Parallel data collection (30 seconds)**
```
Research Agent → Fetches Cursor pricing, Claude API info, Supabase features
KPI Calculator → Computes time savings (40h manual → 29h with AI)
Wisdom Extractor → Analyzes "expected vs actual" for insights
```

**Step 3: Story Arc design (15 seconds)**
```
Story Arc Designer receives all data
Determines: "Hook = 48h timeline, Secret = AI wrote 80%"
Maps panels: Header → Results → Tech → Architecture → Reality → Lessons → CTA
```

**Step 4: Parallel visual generation (60 seconds)**
```
Diagram Generator → Creates User→Frontend→AI→DB flow
Graph Generator → Builds time breakdown bar chart
Icon Fetcher → Downloads Cursor, Claude, Next.js, Supabase logos
Animation Designer → Plans data flow particles + scan effects
```

**Step 5: Layout composition (30 seconds)**
```
Layout Compositor → Assembles all elements
Applies brand colors (#667eea purple gradient)
Positions according to story arc plan
Generates HTML + animation scripts
```

**Step 6: Quality assurance (15 seconds)**
```
QA Agent → Checks story coherence (✓)
Verifies all numbers match input (✓)
Tests animations are smooth (✓)
Validates file size <5MB (✓)
Approves for export
```

**Step 7: Export (10 seconds)**
```
Generate animated GIF (4.2MB)
Generate static PNG (890KB)
Generate interactive HTML
Create metadata.json
Total time: ~2.5 minutes
```

---

## Questions for Refinement

As you review this plan, consider:

1. **Agent Granularity:** Are sub-agents too fine-grained or should some be combined?
2. **MCP Integration:** Which existing MCP servers can we leverage vs building custom?
3. **Prompt Templates:** Should we include full example prompts for each agent in this doc?
4. **Testing Strategy:** How do we validate "good" vs "bad" visual outputs programmatically?
5. **User Control:** How much should users be able to customize vs trusting the system?
6. **Performance:** What's the acceptable generation time (current target: <3 minutes)?

Your feedback on these questions will shape the implementation priorities.