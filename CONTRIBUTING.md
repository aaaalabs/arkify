# Contributing to Arkify

First off, thank you for considering contributing to Arkify! 🎉

Arkify is built by indie hackers, for indie hackers. We believe the best ideas come from the community, and we welcome contributions at all skill levels.

## 🌟 How You Can Contribute

### 🎨 Design Contributions (No Coding Required!)

**Create Layout Templates**
- Design new 2x2, 3x3, or custom grid layouts
- Submit as mockups (Figma, Sketch, even hand-drawn!)
- We'll help implement them

**Color Palettes**
- Create new color schemes
- Submit as hex codes or design files
- Must meet WCAG contrast requirements (we'll help verify)

**Example Projects**
- Share your own project breakdowns
- Create diverse YAML examples
- Show what's possible with Arkify

### 💻 Code Contributions

**Good First Issues**
- Look for [`good first issue`](https://github.com/yourusername/arkify/labels/good%20first%20issue) label
- Typically take <2 hours to complete
- Great for first-time contributors

**Agent Improvements**
- Enhance existing agents (KPI Calculator, Icon Fetcher, etc.)
- Better error handling
- Performance optimizations
- Add new visualization types

**New Features**
- See [ROADMAP.md](ROADMAP.md) for planned features
- Propose new ideas in Discussions first
- Break into small, reviewable PRs

### 📝 Documentation Contributions

**Improve Docs**
- Fix typos and clarify explanations
- Add more examples
- Translate to other languages
- Create video tutorials

**Write Blog Posts**
- Share your Arkify workflow
- Case studies of generated breakdowns
- Technical deep-dives on agents

## 🚀 Getting Started

### 1. Fork & Clone

```bash
# Fork the repository on GitHub
# Then clone your fork:

git clone https://github.com/YOUR_USERNAME/arkify.git
cd arkify

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/arkify.git
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (coming in Phase 1)
# pip install -r requirements-dev.txt
```

### 3. Create a Branch

```bash
# Update your fork
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/your-feature-name
# or: git checkout -b fix/bug-description
```

### 4. Make Your Changes

**Code Style (Python)**
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to all functions
- Keep functions small and focused (KISS principle)

**Example:**
```python
def calculate_cost_per_hour(total_cost: float, hours: float) -> float:
    """
    Calculate cost per hour.

    Args:
        total_cost: Total project cost in EUR
        hours: Total hours spent

    Returns:
        Cost per hour, rounded to 2 decimals

    Raises:
        ValueError: If hours is zero or negative
    """
    if hours <= 0:
        raise ValueError("Hours must be positive")

    return round(total_cost / hours, 2)
```

**Design Principles**
- **[CP01] KISS:** Keep it simple
- **[EH01] No Fallbacks:** Fail fast with real errors
- **[CS03] Small Functions:** <50 lines per function
- See [CLAUDE.md](CLAUDE.md) for full coding rules

### 5. Test Your Changes

```bash
# Run on example files
python arkify.py examples/ai-todo-app.yaml
python arkify.py examples/saas-mvp.yaml
python arkify.py examples/weekend-hack.yaml

# Verify outputs look correct
open output/*.png

# Run tests (coming in Phase 1)
# pytest tests/
```

### 6. Commit Your Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "feat: add support for custom color palettes"

# Or for bug fixes:
# git commit -m "fix: handle missing tech stack gracefully"
```

**Commit Message Format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, no logic change)
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

### 7. Push & Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Go to GitHub and create Pull Request
```

**PR Guidelines:**
- Link to related issue (if exists)
- Describe what changes and why
- Add before/after screenshots (for visual changes)
- Keep PRs focused (one feature/fix per PR)

## 📋 Contribution Checklist

Before submitting a PR, check:

- [ ] Code follows Python style guide (PEP 8)
- [ ] All functions have docstrings
- [ ] Tested on at least 2 example YAML files
- [ ] No new errors or warnings
- [ ] Updated documentation (if needed)
- [ ] Added example (if new feature)
- [ ] Commit messages are descriptive

## 🐛 Reporting Bugs

**Before Reporting:**
1. Check [existing issues](https://github.com/yourusername/arkify/issues)
2. Try latest version from `main` branch
3. Verify it's reproducible

**Bug Report Should Include:**
- Python version (`python --version`)
- Operating system
- Input YAML file (if relevant)
- Full error message
- Steps to reproduce

**Template:**
```markdown
## Bug Description
[Clear description of the bug]

## Steps to Reproduce
1. Run `python arkify.py examples/my-project.yaml`
2. See error

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- OS: macOS 13.2
- Python: 3.11.1
- Arkify: Phase 0 (commit abc123)

## Screenshots/Logs
[If applicable]
```

## 💡 Feature Requests

**Before Requesting:**
1. Check [ROADMAP.md](ROADMAP.md) - might already be planned!
2. Check [Discussions](https://github.com/yourusername/arkify/discussions)
3. Consider if it fits Arkify's philosophy (Simple, Lovable, Complete)

**Feature Request Should Include:**
- Problem it solves
- Proposed solution
- Alternative solutions considered
- Mockups/examples (if applicable)

**Use Discussions, not Issues, for:**
- General questions
- Feature ideas (before formal request)
- Showing off what you built
- Asking for help

## 🎯 Contribution Tiers

### Level 1: Template Designer 🎨
**No coding required!**
- Design layout templates
- Create color palettes
- Share example projects
- Write documentation

**First contribution ideas:**
- Create a dark mode color palette
- Design a 1x6 vertical layout for Instagram Stories
- Add 5 new example YAML files

### Level 2: Python Developer 💻
**Basic Python skills**
- Improve agent implementations
- Add error handling
- Optimize performance
- Write tests

**First contribution ideas:**
- Add support for more tech logos
- Improve text wrapping algorithm
- Add progress bar during generation

### Level 3: Advanced Developer 🚀
**Experienced with AI/design systems**
- Build new agents
- Implement complex features
- Architecture decisions
- Review PRs

**Contribution ideas:**
- Implement Phase 1 Story Arc Designer
- Add SVG rendering support
- Build animation system (Phase 3)

### Level 4: Core Maintainer ⚙️
**Trusted long-term contributors**
- Release management
- Community leadership
- Strategic direction
- Mentor new contributors

## 🏆 Recognition

Contributors are recognized in:
- README.md "Contributors" section
- Monthly showcase of contributions
- Special role in community Discord (future)

Top contributors:
- Early access to new features
- Input on roadmap priorities
- Invitation to core team (after consistent contributions)

## 📜 Code of Conduct

### Our Pledge

We pledge to make participation in Arkify a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity, level of experience, nationality, personal appearance, race, religion, or sexual identity.

### Our Standards

**Positive behavior:**
- Being respectful and welcoming
- Accepting constructive criticism
- Focusing on what's best for the community
- Showing empathy

**Unacceptable behavior:**
- Harassment or discriminatory language
- Trolling or insulting comments
- Publishing others' private information
- Other conduct inappropriate for a professional setting

### Enforcement

Report issues to [maintainer email]. All complaints will be reviewed and investigated.

## 💬 Questions?

- **General questions:** [GitHub Discussions](https://github.com/yourusername/arkify/discussions)
- **Bug reports:** [GitHub Issues](https://github.com/yourusername/arkify/issues)
- **Direct contact:** [maintainer email]

## 🎉 Thank You!

Every contribution makes Arkify better. Whether you're fixing a typo, designing a template, or building a new agent - thank you for being part of the indie hacker community! 🙏

---

**Ready to contribute? Pick a [`good first issue`](https://github.com/yourusername/arkify/labels/good%20first%20issue) and let's ship! 🚀**
