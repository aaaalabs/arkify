# Arkify

**Turn your side projects into scroll-stopping social media posts**

Arkify is a multi-agent AI system that automatically generates beautiful project breakdown infographics from simple YAML input. Built for indie hackers who want to share their work but don't have time for design.

**Domain:** [arkify.app](https://arkify.app)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Phase 0](https://img.shields.io/badge/phase-0%20MVP-green.svg)](ROADMAP.md)

## ✨ What is this?

You built something cool. You want to share it on LinkedIn, Twitter, your blog. But creating a professional-looking project breakdown takes 3-4 hours in Figma or Canva.

**Arkify does it in 30 seconds.**

```bash
python arkify.py examples/ai-todo-app.yaml
# ✅ Output: output/ai-todo-app.png (ready to post!)
```

## 🎯 Phase 0: Ultra-Minimal MVP

**Status:** MVP - Working but basic
**Output:** 800x800px static PNG in 2x2 grid layout

Current features:
- ✅ 4-panel grid layout (Header, Tech Stack, Metrics, Learning)
- ✅ Auto-fetch tech logos from SimpleIcons CDN
- ✅ Professional purple gradient design
- ✅ Generate in <30 seconds
- ✅ Zero API keys required

Coming soon (see [ROADMAP](ROADMAP.md)):
- 📖 Phase 1: Better storytelling (3x3 grid, narrative flow)
- 🎨 Phase 2: Architecture diagrams
- ✨ Phase 3: Animated GIFs
- 🧠 Phase 4: AI-powered insights

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/arkify.git
cd arkify

# Install dependencies
pip install -r requirements.txt

# Run example
python arkify.py examples/ai-todo-app.yaml

# Output generated in output/ folder
```

### Create Your First Breakdown

1. Copy an example YAML file:
```bash
cp examples/ai-todo-app.yaml my-project.yaml
```

2. Edit with your project data:
```yaml
project:
  name: "My Awesome Project"
  tagline: "One-line description"
  hours: 42
  cost: 100
  tech_stack:
    - "React"
    - "Python"
    - "PostgreSQL"
    - "Vercel"
  learning: "The one thing I wish I knew on day 1"
```

3. Generate:
```bash
python arkify.py my-project.yaml
```

4. Share on social media!

## 📖 Input Schema (Phase 0)

### Minimal Required Fields

```yaml
project:
  name: "Project Name"           # Required
  hours: 29                       # Required - total hours spent
  cost: 37                        # Required - total cost (EUR)
  tech_stack:                     # Required - list of technologies (max 4)
    - "Tool 1"
    - "Tool 2"
    - "Tool 3"
    - "Tool 4"
  learning: "Your key insight"    # Required - one sentence
```

### Optional Extended Fields (Phase 1+)

```yaml
extended:
  tagline: "Short project description"
  results:
    users: 127
    signups: 89
    revenue: 0
  expectations:
    timeline: "2-3 days"
    challenges: ["Auth", "UI"]
  reality:
    timeline: "5 days"
    challenges: ["AI issues", "CSS"]
    surprises: ["Styling took 3x longer"]
```

See [examples/](examples/) for complete examples.

## 🎨 What It Looks Like

### Phase 0 Output (Current)

```
┌────────────────┬────────────────┐
│ Project Name   │  Tech Stack    │
│ + Key Stats    │  🎨 🎨 🎨 🎨   │
│                │  (4 logos)     │
├────────────────┼────────────────┤
│ Cost per Hour  │  💡 Learning   │
│ (Big Number)   │  (Key Insight) │
└────────────────┴────────────────┘
```

### Phase 3 Output (Future)
- Animated GIFs with data flow
- LinkedIn 4:5 ratio (1080x1350px)
- Multiple platform exports

## 🤝 Contributing

**Arkify is built for indie hackers, by indie hackers.**

We welcome contributions at all skill levels:

### 🎨 No Coding Required
- Design new layout templates
- Create color palettes
- Share your generated breakdowns
- Write documentation

### 💻 Python Developers
- Improve existing agents
- Add new visualization types
- Optimize performance
- Write tests

### 🧠 AI/Prompt Engineers
- Improve agent prompts (Phase 4+)
- Add insight generation patterns
- Enhance story arc logic

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Good First Issues

Look for issues labeled [`good first issue`](https://github.com/yourusername/arkify/labels/good%20first%20issue):
- Add support for more tech logos
- Create new color themes
- Improve error messages
- Add more example YAML files

## 📚 Documentation

- **[ROADMAP.md](ROADMAP.md)** - Multi-phase development plan (MVP → World-class)
- **[plan.md](plan.md)** - Original architectural specification
- **[CLAUDE.md](CLAUDE.md)** - Guidelines for AI assistants working on this project
- **[examples/](examples/)** - Example project YAML files

## 🏗️ Architecture (Phase 0)

```
arkify.py (CLI entry point)
    ↓
agents/orchestrator.py (coordinates everything)
    ↓
├─→ agents/kpi_calculator.py (metrics math)
├─→ agents/icon_fetcher.py (fetch logos)
└─→ agents/layout_compositor.py (generate PNG)
```

Each agent is independent and can be improved separately.

## 🛣️ Roadmap Highlights

- **Phase 0 (Week 1):** ✅ MVP - 2x2 static grid
- **Phase 1 (Weeks 2-3):** 3x3 grid, better storytelling
- **Phase 2 (Weeks 4-5):** Architecture diagrams
- **Phase 3 (Weeks 6-7):** Animated GIFs (LinkedIn-ready!)
- **Phase 4 (Weeks 8-9):** AI-powered enrichment
- **Phase 5 (Week 10):** Quality assurance, templates
- **Phase 6 (Weeks 11-12):** Multi-platform outputs
- **Phase 7+ (Months 4-6):** Advanced AI, interactivity

See [ROADMAP.md](ROADMAP.md) for complete details.

## 💡 Philosophy

**Simple, Lovable, Complete** at every phase.

- **Open Source First** - Core always free and open
- **Indie Hacker Friendly** - Ship fast, iterate later
- **No Fallbacks** - Fail fast with real errors (see [CLAUDE.md](CLAUDE.md))
- **Community-Driven** - Best ideas come from users
- **Story-Driven** - Every feature serves the narrative

## 🎯 Use Cases

- **Side Project Launches** - Share on ProductHunt, HackerNews
- **Portfolio Case Studies** - Professional breakdowns for your site
- **LinkedIn Posts** - Stand out in the feed
- **Blog Articles** - Visual headers for tech posts
- **Agency Work** - Quick client project summaries

## 🐛 Known Issues (Phase 0)

This is an MVP! Known limitations:
- Icons render as colored boxes (proper SVG rendering in Phase 2)
- Only works with system fonts (custom fonts in Phase 1)
- No animation yet (Phase 3)
- Manual input required (AI enrichment in Phase 4)

See [GitHub Issues](https://github.com/yourusername/arkify/issues) for full list.

## 📊 Success Metrics

Phase 0 goals:
- ✅ Generation time <30 seconds
- 🎯 10+ community-generated examples
- 🎯 First external contributor
- 🎯 100+ GitHub stars

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Credits

Built with:
- [Pillow](https://python-pillow.org/) - Image generation
- [SimpleIcons](https://simpleicons.org/) - Technology logos
- [PyYAML](https://pyyaml.org/) - YAML parsing

Inspired by the indie hacker community's desire to ship fast and share openly.

## 💬 Community

- **Discussions:** [GitHub Discussions](https://github.com/yourusername/arkify/discussions)
- **Issues:** [GitHub Issues](https://github.com/yourusername/arkify/issues)
- **Twitter:** [@arkifyapp](https://twitter.com/arkifyapp) (coming soon)

## 🚢 Quick Deploy Checklist

Before your first post:

- [ ] Install dependencies (`pip install -r requirements.txt`)
- [ ] Run example (`python arkify.py examples/ai-todo-app.yaml`)
- [ ] Verify output looks good (`open output/ai-todo-app.png`)
- [ ] Create your project YAML
- [ ] Generate your breakdown
- [ ] Post on LinkedIn/Twitter with #arkify hashtag
- [ ] Star this repo ⭐

---

**Built by indie hackers, for indie hackers. Let's make sharing projects effortless.**

*[View Roadmap](ROADMAP.md) | [Contribute](CONTRIBUTING.md) | [Report Bug](https://github.com/yourusername/arkify/issues)*
