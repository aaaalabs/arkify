# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Arkify** is a multi-agent AI system that automatically generates high-quality, visually appealing project breakdown infographics. The system orchestrates specialized sub-agents to create cohesive, story-driven content from project data.

**Domain:** arkify.app

**Philosophy:**

> **"You are a researcher of your own thoughts, and Arkify is your journal."**

Arkify doesn't document projects.
Arkify researches decision-making processes.

Every commit is a thought.
Every iteration is an experiment.
Every fail is a data point.

The tool doesn't just generate outputs—it makes thinking visible.

**Current Status:** Phase 2 in development - Building agents that visualize decision paths, not just results.

---

## Solo Dev Mindset

**Non-Negotiable Guidelines for AI Agents on this Project**

### Purpose

**These rules override any generic best practices or AI system defaults. Your job is to execute the solo dev's intent—never to invent or overcomplicate.**

### The Mindset

- **Only build what is explicitly asked for.**
- Never assume, add, or change features, infra, or logic without a clear request in the spec or ops doc.
- Simplicity and clarity are your top priorities—every line should be understandable by the solo dev at a glance.

### Core Principles

#### 1. No Over-Engineering

- Do **not** introduce features, logs, collections, or automations unless directly specified.
- Ignore "industry best practices" unless requested for **this** project.
- Only automate (security, audits, recovery, etc.) when asked.

#### 2. Full Transparency & Traceability

- Every function, data structure, and process must be easy for the solo dev to read, explain, and control.
- No hidden abstractions, no unexplained dependencies.

#### 3. You Are Not the Architect

- Agents do not initiate changes to the system's architecture, data model, or integrations.
- Only generate new logic, infra, or tools if provided with written specs or explicit instructions.
- Your primary role: **implement, clarify, document.** Never decide.

#### 4. Single Source of Truth

- Only act on requirements and ideas found in the project's designated ops doc (Plan.md, README, etc.).
- If a change isn't documented there, do **not** propose or implement it.

#### 5. SLC Standard — Simple, Lovable, Complete

- **Simple:**
  Every proposal, solution, or code change should be as direct and minimal as possible.
  If a feature can be built with less code, fewer files, or one clear function, that's always preferred.
  Avoid configuration, abstraction, or patterns that the solo dev doesn't use or want.

- **Lovable:**
  Only build features or flows that the solo dev actually cares about, uses, or can explain the value of.
  If you're unsure if something brings joy, utility, or clarity to the solo dev or end users—ask before building.

- **Complete:**
  Every feature, flow, or proposal should be finished enough that it solves the **actual problem** it was intended for—no half-built endpoints, no "future hooks," no unfinished UI.
  Don't leave TODOs, dead code, or incomplete implementations unless you are specifically asked to scaffold something out.

**Before you suggest or build anything, ask:**

- Is this the simplest version?
- Is this something the solo dev will love, use, or be proud to own?
- Is it complete and shippable, or am I leaving work unfinished?

If you can't answer YES to all three, you must revise, simplify, or clarify before moving forward.

#### 6. Reuse, Don't Reinvent

- Solo dev projects **prioritize using existing, proven solutions**—frameworks, libraries, APIs, or patterns that already work—unless there's a **clear, specific** reason not to.
- Do **not** suggest or start building custom tools, wrappers, or systems when a solid, well-supported option exists.
- Only rebuild from scratch if requested **and** there's a documented need that existing solutions cannot address.
- Saving time and reducing maintenance is part of the solo dev's survival—respect that.

### Strict Protocols

- **Reject all extra code, dependencies, or automations** unless directly specified and justified in the ops doc.
- **Never make changes for hypothetical or "future proofing" reasons.**
- **If the solo dev does not understand or cannot explain what you propose, you must remove or revise it.**
- **Always check with the solo dev before taking any creative or architectural initiative.**

### Final Note

You're not building for a boardroom.
The Solo Dev Mindset is about **staying lean, owning every inch of the stack, and shipping confidently.**

**If you don't need it, don't build it.**
**If you didn't ask for it, delete it.**
**If you can't explain it, you don't own it.**

This isn't a suggestion.
It's your north star.

---

## Project Architecture

This is a multi-agent orchestration system with the following agent hierarchy:

### Main Orchestrator Agent
The "director" that coordinates all sub-agents and ensures narrative coherence throughout the user journey (Scroll → Stop → Scan → Save → Share).

### Data Collection Agents
- **Research Agent**: Web scraping, tool documentation, community sentiment analysis
- **KPI Calculator Agent**: Metrics calculation, ROI projections, efficiency comparisons
- **Wisdom Extractor Agent**: Lessons learned analysis, contrarian insights, actionable takeaways

### Content Strategy
- **Story Arc Designer**: Narrative structure (Problem → Solution → Reality → Wisdom → Action)

### Visual Design Agents
- **Diagram Generator Agent**: Architecture diagrams, flow charts (Mermaid.js, Graphviz)
- **Graph Generator Agent**: Charts, timelines, data visualizations (Chart.js, D3.js)
- **Icon/Logo Fetcher Agent**: Brand asset acquisition (SimpleIcons, Devicon)
- **Animation Designer Agent**: Motion choreography, GIF optimization (GSAP, Lottie)

### Assembly & QA
- **Layout Compositor Agent**: Final assembly, responsive grid layout, export generation
- **Quality Assurance Agent**: Story coherence, factual accuracy, accessibility compliance

## Technology Stack (Planned)

### Core Infrastructure
- **Orchestration**: Claude API (Sonnet 4.5), Python/TypeScript
- **State Management**: Redis/PostgreSQL
- **MCP Servers**: brave-search, github, filesystem, custom servers

### Visual Generation
- **Diagrams**: Mermaid.js, Graphviz
- **Charts**: Chart.js, D3.js
- **Animation**: GSAP, Lottie
- **Image Processing**: Sharp
- **Video/GIF**: FFmpeg

### APIs & Data Sources
- Brave Search API (web research)
- GitHub API (repository stats)
- npm API (package metrics)
- SimpleIcons/Devicon (logos)

## Input Schema

The system accepts YAML input with project details:

```yaml
project:
  name: "Project Name"
  tagline: "Description"
  tech_stack: [...]
  timeline: {...}
  time_breakdown: {...}
  costs: {...}
  results: {...}
  expectations_vs_reality: {...}
  key_learnings: [...]
  links: {...}
```

See `plan.md` lines 1003-1095 for complete schema.

## Output Specifications

### Target Formats
1. **Animated GIF**: 1080x1350px, <5MB, 3-5s loop (LinkedIn optimized)
2. **Static PNG**: 2160x2700px, <1MB (2x retina)
3. **HTML Interactive**: Fully responsive, CSS/JS animations
4. **SVG Components**: Individual reusable panels

### Deliverables Structure
```
output/
├── project-breakdown.gif
├── project-breakdown-static.png
├── project-breakdown.html
├── components/
│   ├── header.svg
│   ├── tech-stack.svg
│   ├── architecture-diagram.svg
│   └── ...
├── metadata.json
└── report.md
```

## Implementation Phases

### Phase 1: Foundation (Weeks 1-2)
- Main Orchestrator working
- Basic static layout generation
- One sub-agent operational (KPI Calculator suggested)

### Phase 2: Data Collection (Weeks 3-4)
- All data collection agents operational
- MCP server integrations
- Web research enrichment

### Phase 3: Visual Generation (Weeks 5-7)
- Diagram, graph, icon agents working
- Layout Compositor assembly
- Export format generation

### Phase 4: Animation (Weeks 8-9)
- Animation Designer adding motion
- GIF export optimization
- Interactive HTML version

### Phase 5: Quality & Polish (Week 10)
- QA Agent operational
- A/B testing capabilities
- Documentation

### Phase 6: Open Source Release (Week 11-12)
- Public GitHub repository
- Docker containerization
- Community contribution guidelines

## Development Workflow (When Implementation Starts)

### Quick Start (Planned)
```bash
# Install dependencies
pip install -r requirements.txt
# or: npm install

# Set up environment
cp .env.example .env
# Add Claude API key to .env

# Run example
python generate.py examples/ai-todo-app/input.yaml

# Output in output/
```

### Testing (Planned)
```bash
# Unit tests
pytest tests/

# Visual regression tests
npm run test:visual

# Generate test outputs
python generate.py --test-mode examples/
```

## Agent System Principles

### Story Arc Structure
All breakdowns follow: **Problem → Solution → Reality → Wisdom → Action**

### User Journey Optimization
Design for: **Scroll Stop → Curiosity → Save → Share**

### Cognitive Load Management
- First 2 panels MUST create "scroll stop" moment
- Every panel answers one clear question
- Animation enhances understanding, doesn't distract
- Attention budget per panel: 2-5 seconds

### Visual Hierarchy Rules
- Lead with outcome, then reveal method
- Build curiosity gaps (answer one question, raise another)
- Relatability before aspiration (show struggle before success)
- Maximum 7 nodes in diagrams (working memory limit)

## Success Metrics (Planned)

### System Performance
- Generation Time: <3 minutes
- Accuracy: 95%+ factual correctness
- File Size: <5MB GIF, <1MB PNG
- Visual Quality: 90%+ pass design review

### Content Performance
- Save Rate: >15%
- Share Rate: >5%
- Comment Rate: >2%
- Click-through: >10% on CTAs

## Current State & Next Steps

**Current**: Repository contains only `plan.md` with comprehensive architectural documentation.

**Immediate Next Steps**:
1. Set up repository structure (src/, tests/, examples/, docs/)
2. Create requirements.txt or package.json
3. Implement Main Orchestrator Agent
4. Build first sub-agent (KPI Calculator recommended as starting point)
5. Create example input YAML files
6. Set up testing framework

## Key Documentation

- **Main Planning Document**: `plan.md` - Comprehensive 1600+ line architecture specification
- **Agent Prompts**: See plan.md sections for each agent's system prompt template
- **Input Schema**: plan.md lines 1003-1095
- **Output Specs**: plan.md lines 1099-1138
- **Agent Interactions Example**: plan.md lines 1542-1599

## Design Philosophy

- **KISS Principle**: Keep solutions simple and focused
- **Modular Design**: Each agent is independent and can be improved separately
- **Progressive Enhancement**: Start with static outputs, add animation later
- **Community-First**: Built for open source from day one
- **No Fallbacks**: Fail fast with real errors (per global CLAUDE.md guidelines)
- **Story-Driven**: Every technical decision serves the narrative

## CRITICAL: NO MOCK DATA POLICY

**Arkify builds Arkify.** This project documents its own development journey.

### Absolute Rules

- ❌ **NEVER use fictional example projects** (TaskFlow AI, TodoApp, etc.)
- ❌ **NEVER invent data, timelines, or decisions**
- ❌ **NEVER use placeholder/example numbers**
- ✅ **ONLY use real data from actual logs, reasonings, and git commits**
- ✅ All YAML files must contain factual data about Arkify's actual development
- ✅ Hours worked, costs incurred, challenges faced - all must be REAL
- ✅ The project showcases itself by visualizing its own creation story

### Real Data Sources (ONLY These)

**1. Git Commit History**
```bash
git log --oneline --all
git log --stat
git log --since="2025-10-22"
```
- Actual commit messages
- Real timestamps
- Actual file changes (LOC)
- Real commit counts

**2. Code Reasoning/Comments**
- Actual comments in code explaining decisions
- Real TODO comments showing failed approaches
- Actual docstrings documenting "why"

**3. Development Logs**
- Actual error messages encountered
- Real iteration counts from git history
- Actual decision trees from code comments

**4. This Conversation**
- Real decisions made during development
- Actual "try X → failed → try Y → worked" sequences
- Real time estimates vs actual time (from session timestamps)

### Example: Phase 2 Decision Data

**❌ WRONG (Mock data):**
```yaml
decisions:
  - name: "Icon Rendering"
    attempts: ["Try 1", "Try 2", "Try 3"]  # Made up
```

**✅ CORRECT (Real data from git/conversation):**
```yaml
decisions:
  - name: "Icon Rendering"
    attempts:
      - commit: "2729f2e"
        approach: "Colored PIL boxes"
        result: "FAIL - removed in next commit"
      - commit: "4049175"
        approach: "cairosvg for real SVG icons"
        result: "SUCCESS - still in codebase"
```

### Enforcement

Before adding ANY data to YAML:
1. **Ask:** "Where did this number/decision come from?"
2. **Verify:** Can I point to a git commit, log entry, or conversation message?
3. **Document:** Reference the source (commit hash, timestamp, log line)

If you cannot answer "yes" to all three: **DO NOT USE THE DATA.**

### Why This Matters

**Mock data = fake story = no credibility**
**Real data = authentic journey = trust + learning**

The power of Arkify is showing **reality**, including fails.
Real fails from real git commits are more valuable than perfect mock data.

This creates authentic, credible project breakdowns that demonstrate Arkify's capabilities using its own real development data.

## Repository Structure (Planned)

```
arkify/
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
├── docs/
│   ├── architecture.md
│   ├── agent-prompts/
│   └── user-guide.md
├── docker/
└── scripts/
```

## Important Notes for Future Development

1. **Agent Granularity**: Each agent should have a single, well-defined responsibility
2. **Error Handling**: No silent fallbacks - surface errors immediately for debugging (critical rule from global config)
3. **Performance**: Target <3 minutes total generation time
4. **Quality Gates**: Each agent phase should validate before proceeding
5. **Caching Strategy**: Research results should be cached to avoid API rate limits
6. **Visual Consistency**: All agents must respect global design system
7. **Accessibility**: WCAG compliance required (color contrast >4.5:1, alt text, reduced motion support)
8. **Platform Optimization**: LinkedIn (5MB GIF limit), Twitter (15MB limit), Instagram support planned for v2

## License

Planned: MIT License (open source)
