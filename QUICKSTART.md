# Arkify Quick Start - 60 Seconds to Your First Breakdown

## TL;DR

```bash
git clone https://github.com/yourusername/arkify.git
cd arkify
pip install -r requirements.txt
python arkify.py examples/ai-todo-app.yaml
open output/ai-todo-app.png
```

Done. 🎉

---

## For Your Own Project

### 1. Create YAML (30 seconds)

```yaml
# my-project.yaml
project:
  name: "Your Project Name"
  hours: 42                    # Total hours spent
  cost: 100                    # Total cost (EUR)
  tech_stack:                  # Max 4 technologies
    - "React"
    - "Python"
    - "PostgreSQL"
    - "Vercel"
  learning: "Ship fast, iterate later"  # One key insight
```

### 2. Generate (10 seconds)

```bash
python arkify.py my-project.yaml
```

### 3. Share (20 seconds)

```bash
open output/your-project-name.png
# Post on LinkedIn, Twitter, your blog
# Tag with #arkify
```

---

## Troubleshooting (If Something Breaks)

### "command not found: python"
```bash
python3 arkify.py my-project.yaml
```

### "No module named 'yaml'"
```bash
pip install -r requirements.txt
# or: pip3 install -r requirements.txt
```

### "Error: Input file 'my-project.yaml' not found"
```bash
ls *.yaml  # Check filename
python arkify.py examples/ai-todo-app.yaml  # Try example first
```

### Icons show as colored boxes (not logos)
This is normal in Phase 0! Proper SVG rendering comes in Phase 2.

---

## What to Post

**LinkedIn Template:**
```
I just shipped [PROJECT NAME] in [X] hours for €[Y]!

Here's the complete breakdown 👇

Tech stack: [list]
Key learning: [your insight]

Built with #arkify - the open-source project breakdown generator.

[your-breakdown.png]
```

**Twitter Template:**
```
Shipped [PROJECT] in [X]h for €[Y]

[list emojis for tech stack]

TIL: [your key learning]

Full breakdown 👇

[your-breakdown.png]

#arkify #buildinpublic #indiehacker
```

---

## Next Steps

### Contribute
- Add your project to `examples/`
- Create a color palette
- Improve documentation
- See [CONTRIBUTING.md](CONTRIBUTING.md)

### Customize
- Edit `agents/layout_compositor.py` for different colors
- Modify panel layouts (lines 50-150)
- Add your own tech stack mappings (lines 40-60 in `icon_fetcher.py`)

### Follow Development
- ⭐ Star the repo for updates
- 👀 Watch for Phase 1 release (3x3 grids!)
- 💬 Join discussions
- 🐛 Report bugs

---

## The 5 Required Fields Explained

1. **name** - Your project name (appears in header)
2. **hours** - Total time spent (we'll calculate cost per hour)
3. **cost** - Total expenses in EUR (can be 0 for free projects)
4. **tech_stack** - List of tools used (max 4 for now)
5. **learning** - Your key insight (the "I wish I knew this on day 1" moment)

**That's it.** Everything else is optional (for now).

---

## Examples Included

| File | Project Type | Hours | Cost |
|------|--------------|-------|------|
| `ai-todo-app.yaml` | AI-powered SaaS | 29 | €37 |
| `saas-mvp.yaml` | Landing page builder | 48 | €145 |
| `weekend-hack.yaml` | Quick utility | 16 | €8 |

Try them all:
```bash
python arkify.py examples/ai-todo-app.yaml
python arkify.py examples/saas-mvp.yaml
python arkify.py examples/weekend-hack.yaml
```

---

## Advanced: Extended Fields (Phase 1+)

```yaml
extended:
  tagline: "One-line description"
  results:
    users: 127
    signups: 89
    revenue: 0
  expectations:
    timeline: "2-3 days"
    challenges: ["Auth", "UI"]
  reality:
    timeline: "5 days"
    challenges: ["AI bugs", "CSS"]
    surprises: ["Styling took 3x longer"]
```

These fields don't do anything yet in Phase 0, but will unlock:
- Better storytelling (Phase 1)
- Expectations vs Reality panels (Phase 1)
- AI-generated insights (Phase 4)

---

## FAQ

**Q: Can I use USD instead of EUR?**
A: Yes! Just use your currency. The symbol is hardcoded to € but you can change it in `agents/kpi_calculator.py` line 70.

**Q: What if I used more than 4 technologies?**
A: Phase 0 only shows 4 (grid limitation). List your most important ones. Phase 1 will support unlimited.

**Q: The output looks basic. Can I customize it?**
A: Yes! Edit `agents/layout_compositor.py`. Or wait for Phase 2's theme system.

**Q: Does this work on Windows?**
A: Should work! But not tested yet. If you find issues, please report them.

**Q: Can I use this commercially?**
A: Yes! MIT license. Use it for client work, portfolios, whatever. Attribution appreciated but not required.

---

## Support

- 🐛 **Bug reports:** [GitHub Issues](https://github.com/yourusername/arkify/issues)
- 💬 **Questions:** [GitHub Discussions](https://github.com/yourusername/arkify/discussions)
- 🚀 **Feature requests:** Check [ROADMAP.md](ROADMAP.md) first, then Discussions

---

**Ready? Let's build in public! 🚀**

```bash
python arkify.py examples/ai-todo-app.yaml
```
