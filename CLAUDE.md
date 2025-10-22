# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Arkify** is a universal multi-layer storytelling system that transforms complex narratives into beautiful visual breakdowns. While initially focused on technical project documentation, the long-term vision encompasses life stories, business ventures, creative projects, and multi-dimensional narratives.

**Domain:** arkify.app

**Current Status:** Phase 0 MVP - 2x2 grid generator for tech projects (working)

**Current Focus:** Tech project breakdowns (Phase 0-6)
**Future Vision:** Universal storytelling for any narrative with depth (Phase 7+)

### Multi-Domain Vision (Phase 7+ Roadmap)

Arkify will ultimately support multiple story domains:

- **💻 Tech Projects** - Software development journeys (Phase 0-6 focus)
- **👤 Life Stories** - Personal evolution, career pivots, biographical arcs
- **🚀 Business Ventures** - Startup journeys, entrepreneurial pivots, company growth
- **🎨 Creative Projects** - Album creation, book writing, artistic evolution
- **🌀 Multi-Layer Narratives** - Stories that exist on multiple dimensions simultaneously

**Architecture Philosophy:**
- Phase 0-6: Perfect tech domain implementation
- Phase 7+: Expand to universal storytelling
- Core Schema + Domain Extensions pattern
- Domain-specific Story Arcs

See `docs/MULTI-DOMAIN-VISION.md` for complete specification.

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
- **SLC (Simple-Lovable-Complete)**: All development follows this framework
- **First Principles Thinking**: Start with "Why?" before "How?"

### Universal Development Principles

**Complete framework available in:** `docs/UNIVERSAL-DEVELOPMENT-PRINCIPLES.md`

Diese universellen, code-stack-agnostischen Prinzipien gelten für ALLE Entwicklung in diesem Projekt:

#### **Core Framework: KISS + First Principles + SLC**

**First Principles Analysis:**
- Core Problem Definition: Welches User-Problem eliminieren wir?
- Essential Solution: Einfachster Ansatz mit echtem Wert?
- Enhancement vs. Creation: Kann Bestehendes erweitert werden?

**KISS Principle:**
- One-Sentence Test: Nicht in einem Satz erklärbar? → Vereinfachen
- Concept Minimization: Jedes neue Konzept = exponentielle Komplexität
- Enhancement Priority: IMMER erst Enhancement prüfen vor Neu-Erstellung

**SLC (Simple-Lovable-Complete):**
- **Simple**: Minimale notwendige Komplexität, keine "vielleicht später" Features
- **Lovable**: Fail-fast mit transparenten Errors, klares Feedback
- **Complete**: Produktionsreif, keine "coming soon" Platzhalter

#### **Atomic-Molecular-Organic Pattern**

- **Atomic**: Single-Responsibility Grundbausteine (z.B. Agent Base Classes)
- **Molecular**: Funktionale Kombinationen (z.B. Agent Koordination)
- **Organic**: Komplexe Features (z.B. Phase Orchestration)

#### **The "Planner Mode" Process (Mandatory)**

Vor JEDER signifikanten Änderung:

1. **Deep Reflection**: Impact auf bestehende Features? Edge Cases? Skalierung?
2. **6 Clarifying Questions**: Was könnte brechen? Wie testen? Rollback-Plan?
3. **Step-by-Step Plan**: File Changes, neue Komponenten, Tests, Migration
4. **Wait for Approval**: Kein Cowboy Coding
5. **Implementation**: Plan befolgen, Tests schreiben
6. **Post-Implementation Reflection**: Scalability, Maintainability, Performance, Error Handling

#### **Red Flags to Avoid**

- ❌ Files > 250 Zeilen
- ❌ Functions > 25 Zeilen
- ❌ Multiple Komponenten in einer Datei
- ❌ Unbehandelte Exceptions
- ❌ Fehlende Error Messages
- ❌ Magic Numbers ohne Erklärung
- ❌ Tight Coupling zwischen Komponenten
- ❌ Fehlende Loading/Error/Empty States

#### **The No Fallbacks Rule (CRITICAL)**

```python
# ❌ VERBOTEN - Silent Fallback
try:
    data = fetch_data()
except:
    data = []  # Versteckt das Problem!

# ✅ KORREKT - Fail Fast
try:
    data = fetch_data()
except ConnectionError as e:
    raise RuntimeError(f"Failed to fetch: {e}") from e
```

**Warum?** Fallbacks verstecken echte Probleme, degradieren Qualität, verhindern schnelles Debugging.

#### **Enhancement-First Strategy**

```
1. Kann bestehende Funktion erweitert werden? → JA: Erweitern
2. Kann bestehende Komponente Parameter kriegen? → JA: Parameter hinzufügen
3. Kann bestehende Architektur angepasst werden? → JA: Refactor
4. Ist neue Komponente absolut notwendig? → LAST RESORT: Neu erstellen
```

**Regel:** Neue Komponenten sind der letzte Ausweg, nicht der erste.

#### **File Organization Rules (Enforced)**

- **One Component Per File**: NIEMALS mehrere Komponenten/Klassen in einem File
- **File Size Limits**: Soft 250 Zeilen, Hard 400 Zeilen
- **Function Size**: Max 25 Zeilen
- **Clear Naming**: File heißt wie Komponente (`StoryArcDesigner.py` → `class StoryArcDesigner`)

#### **Quality Gates Before Every Commit**

```bash
# MANDATORY
python -m pytest tests/          # Tests müssen grün sein
python -m flake8 agents/         # Code Quality Check
python -m mypy agents/           # Type Check (falls mypy verwendet)
```

**Detaillierte Dokumentation:** Siehe `docs/UNIVERSAL-DEVELOPMENT-PRINCIPLES.md` für:
- State Management Decision Tree
- Performance Patterns
- Error Prevention Philosophy
- UX Principles
- Code Review Checklist
- Complete Implementation Examples

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

## Claude Code Project Agents - Effiziente Nutzung

Dieses Projekt hat 6 spezialisierte Claude Code Agents in `.claude/agents/` die für maximale Entwicklungseffizienz genutzt werden sollten.

### Die 6 Agents

1. **architecture-designer** - Plant Code-Struktur und technische Spezifikationen
2. **implementation-agent** - Schreibt produktionsreifen Python Code
3. **testing-agent** - Erstellt umfassende pytest Tests
4. **documentation-agent** - Pflegt Dokumentation und Beispiele
5. **qa-agent** - Prüft Produktionsqualität (verwendet Opus Model!)
6. **breakdown-generator** - Erstellt Meta-Breakdowns (Arkify dokumentiert sich selbst!)

### Wann welchen Agent nutzen?

#### Phase Planning (STARTE HIER)
```
Use the architecture-designer agent to plan Phase 1 features from ROADMAP.md
```
**Output:** Detaillierter Architecture Plan als YAML mit:
- Neue Agents die erstellt werden müssen
- Bestehende Files die modifiziert werden
- Data Structures und Interfaces
- Dependencies und Build Order

#### Implementation (NACH Architecture Plan)
```
Use the implementation-agent to implement the architecture plan
```
**Output:** Produktionsreifer Python Code mit:
- Type hints auf allen Funktionen
- Google-style docstrings
- Fail-fast error handling (keine silent fallbacks!)
- PEP 8 compliance

#### Testing (PARALLEL zu Implementation möglich)
```
Use the testing-agent to create tests for the Story Arc Designer agent
```
**Output:** Umfassende Test Suite mit:
- Unit tests (individual agent methods)
- Integration tests (agent interactions)
- Visual regression tests (PNG comparison)
- Backward compatibility tests

#### Documentation (NACH Implementation)
```
Use the documentation-agent to update docs for Phase 1 features
```
**Output:** Aktuelle Dokumentation:
- README mit neuen Features
- CHANGELOG (Keep a Changelog Format)
- Neue YAML Beispiele die funktionieren
- Migration Guides bei Breaking Changes

#### Quality Assurance (VOR Phase Completion)
```
Use the qa-agent to review Phase 1 quality and create QA report
```
**Output:** Umfassender QA Report mit:
- Code Quality Review (PEP 8, Types, Docstrings)
- Backward Compatibility Check
- Visual Quality Assessment
- Story Coherence Validation
- Performance Benchmarks
- Human Validation Questions

#### Meta Documentation (NACH Human Approval)
```
Use the breakdown-generator to create Phase 1 meta breakdown
```
**Output:** Meta Breakdown PNG der Phase:
- YAML File in `meta/phase-1-breakdown.yaml`
- PNG generiert mit Arkify selbst
- Zeigt Development Journey visuell
- Authentische Learnings und Challenges

### Optimaler Workflow für höchste Effizienz

```
┌─────────────────────────────────────────────────────────┐
│ PHASE KICKOFF: Lese ROADMAP.md für Phase Requirements  │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ 1. ARCHITECTURE DESIGNER                                │
│    → Erstellt detaillierten Architecture Plan           │
│    → ~30 Min                                            │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ 2. IMPLEMENTATION AGENT                                 │
│    → Implementiert alle neuen Agents                    │
│    → Modifiziert bestehende Files                       │
│    → ~2-3 Stunden                                       │
└─────────────────────────────────────────────────────────┘
                          ↓
         ┌────────────────┴────────────────┐
         ↓                                  ↓
┌──────────────────────┐      ┌──────────────────────┐
│ 3a. TESTING AGENT    │      │ 3b. DOCUMENTATION    │
│     → Tests          │      │     AGENT            │
│     → ~1 Stunde      │      │     → Docs           │
└──────────────────────┘      │     → ~45 Min        │
                              └──────────────────────┘
         └────────────────┬────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ 4. QA AGENT (Opus Model für höchste Qualität)          │
│    → Comprehensive Quality Review                       │
│    → Generiert QA Report mit Human Validation Questions │
│    → ~45 Min                                            │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ 🛑 HUMAN CHECKPOINT                                      │
│    → Review QA Report                                   │
│    → Test Generated Examples                            │
│    → Answer Validation Questions                        │
│    → APPROVE / REJECT / ITERATE                         │
└─────────────────────────────────────────────────────────┘
                          ↓ (if approved)
┌─────────────────────────────────────────────────────────┐
│ 5. BREAKDOWN GENERATOR                                  │
│    → Dokumentiert Phase mit Arkify selbst               │
│    → Beautiful Recursion!                               │
│    → ~15 Min                                            │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ ✅ PHASE COMPLETE                                        │
│    → Git Commit & Tag (v0.X.0)                          │
│    → Meta Breakdown PNG in meta/ directory              │
│    → Ready for Next Phase                               │
└─────────────────────────────────────────────────────────┘
```

### Efficiency Tips

#### Parallele Execution
Testing Agent und Documentation Agent können parallel laufen sobald Implementation fertig ist:
```
# In einem Message beide Agents aufrufen:
Use the testing-agent to create tests AND use the documentation-agent to update docs
```

#### Iterative QA
Falls QA Agent Issues findet:
```
# Direkt Implementation Agent für Fixes nutzen:
Use the implementation-agent to fix the issues from the QA report
```

#### Context Management
Alle Agents haben Zugriff auf:
- `ROADMAP.md` - Phase Requirements
- `CLAUDE.md` - Projekt Guidelines (dieses File!)
- Existing Code in `agents/` directory
- Examples in `examples/` directory

### Agent Invocation Patterns

#### Einfache Invocation
```
Use the [agent-name] to [specific task]
```

#### Mit Context
```
Use the architecture-designer agent to plan Phase 1 features.
Focus on 3x3 grid layout and story arc designer.
Reference ROADMAP.md Phase 1 requirements.
```

#### Mit Constraints
```
Use the implementation-agent to create Story Arc Designer.
Must follow existing agent patterns.
Type hints and docstrings required.
Maximum 200 lines of code.
```

### Quality Gates

Jeder Agent ist ein Quality Gate:

```
Architecture ✓ → Implementation ✓ → Testing ✓ → Documentation ✓ → QA ✓ → Human ✓ → Meta ✓
```

Falls ein Gate failed → iterieren bis alle grün sind.

### Pro Tips

1. **Architecture First**: IMMER mit architecture-designer starten. Spart Zeit bei Implementation.

2. **Read Before Write**: Alle Implementation/Documentation Agents lesen bestehenden Code um Patterns zu matchen.

3. **QA verwendet Opus**: Der qa-agent nutzt das Opus Model für höchste Review-Qualität.

4. **Backward Compatibility**: Testing Agent prüft IMMER dass Phase 0 Examples noch funktionieren.

5. **Meta Documentation**: Breakdown Generator dokumentiert den Build-Prozess selbst - radikale Transparenz!

6. **Human Checkpoint ist kritisch**: QA Agent generiert spezifische Fragen. Diese beantworten bevor approve!

### Status Check

```
# Verfügbare Agents anzeigen:
/agents

# Alle 6 sollten sichtbar sein
```

## Git-Based Development Metrics (Mandatory)

### Philosophy: Git is the Single Source of Truth

**CRITICAL RULE:** Development time and all KPIs must be extracted from Git commit history, not manual estimates.

**Why?**
- Manual estimates are inherently inaccurate (Phase 0: estimated 12h, actual 2.6h!)
- Git commits provide authentic, verifiable data
- Transparency and authenticity are core values
- Creates trust with community and stakeholders

### The Git KPI Extraction System

Located in: `utils/git_kpis.py`

```python
from utils.git_kpis import GitKPIExtractor

# Extract all Git-based metrics
extractor = GitKPIExtractor()
kpis = extractor.get_phase_kpis()

# Use in YAML breakdowns:
# hours: {kpis['development']['total_hours']}  # Git-measured
# commits: {kpis['commits']['total']}
# files_changed: {kpis['code']['files_changed']}
# lines_of_code: {kpis['code']['net_lines']}
```

### Available Metrics

#### Timeline Metrics
- `get_first_commit_time()` - Start of development
- `get_latest_commit_time()` - Most recent commit
- `calculate_development_hours()` - Actual hours between first/last commit

#### Code Metrics
- `get_total_commits()` - Total commit count
- `get_files_changed()` - Unique files touched
- `get_lines_added_removed()` - Lines added/removed/net

#### Author Metrics
- `get_commits_by_author()` - Commit distribution
- `get_commit_messages()` - Recent commit history

### Usage in Phase Breakdowns

**Phase 0 Example:**
```yaml
project:
  name: "Arkify Phase 0"

  # MANDATORY: Git-measured hours
  hours: 2.6  # Actual: First commit (07:21) to last commit (10:00) = 2.6h
  cost: 0

  # Optional: Extended Git stats
extended:
  git_stats:
    total_commits: 14
    files_changed: 59
    lines_of_code: 12943
    commits_per_hour: 5.4
```

### Running Git KPI Extraction

```bash
# Generate summary for terminal
python3 utils/git_kpis.py

# Output includes:
# - Timeline (start/end dates and times)
# - Commit count and authors
# - File changes and line counts
# - Recent commit messages
```

### Integration with Meta Breakdowns

When creating meta breakdowns (Arkify documenting itself):

1. **Extract Git KPIs first:**
   ```bash
   python3 utils/git_kpis.py
   ```

2. **Update YAML with real data:**
   ```yaml
   hours: 2.6  # From Git extraction, not estimate
   ```

3. **Generate breakdown:**
   ```bash
   python3 arkify.py meta/phase-X-breakdown.yaml
   ```

### Reality Check Metrics

The Git KPI system provides "reality check" metrics:

- **Commits per hour** - Development velocity indicator
- **Lines per commit** - Code churn indicator
- **Duration days** - Actual calendar time vs. development hours
- **Author distribution** - Team collaboration patterns

### Example Output

```
Phase Development Summary
=========================

📅 Timeline:
   Start: 2025-10-22 at 07:21
   End:   2025-10-22 at 10:00
   Duration: 2.6 hours (0 days)

💻 Commits:
   Total commits: 14
   Authors: Thomas (14)

📝 Code Changes:
   Files changed: 59
   Lines added: 13,421
   Lines removed: 478
   Net lines: 12,943

Recent Commits:
   - claude: convert all agents to proper Claude Code format
   - docs: add complete system overview
   - feat: add meta-agent system
```

### Best Practices

1. **Always Use Git Time** - Never hardcode manual estimates
2. **Document Reality vs. Expectations** - Show both in YAML extended fields
3. **Track Per-Phase** - Use Git tags for phase boundaries (v0.0.0, v0.1.0, etc.)
4. **Transparent Metrics** - Include commits_per_hour, lines_per_commit
5. **Update CLAUDE.md** - Document learnings from Git analysis

### Edge Cases

**Multiple Contributors:**
```python
# Get per-author stats
kpis = extractor.get_phase_kpis()
authors = kpis['commits']['by_author']
# {'Thomas': 14, 'Claude': 3}
```

**Phase Boundaries:**
```python
# Extract KPIs for specific phase (using Git tags)
kpis = extractor.get_phase_kpis(phase_tag='v0.1.0')
```

**Continuous Development:**
```python
# Calculate hours assumes continuous work between commits
# For more accurate tracking, consider commit frequency analysis
```

## License

Planned: MIT License (open source)
