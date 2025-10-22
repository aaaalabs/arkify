# Arkify Claude Code Agents

**Multi-agent orchestration for building Arkify itself, powered by Claude Code.**

## Overview

This directory contains specifications for six specialized Claude Code agents that work together to build Arkify phase by phase. Each agent is an expert in one aspect of software development.

## Agent Architecture

```
Main Orchestrator (Claude Code)
    ├── Architecture Designer (plans structure)
    ├── Implementation Agent (writes code)
    ├── Testing Agent (creates tests)
    ├── Documentation Agent (maintains docs)
    ├── Quality Assurance Agent (reviews quality)
    └── Breakdown Generator (meta documentation)
```

## The Six Agents

### 1. Architecture Designer
**File:** `architecture-designer.md`
**Role:** Plans code structure and technical specifications

**Responsibilities:**
- Design file structure for new features
- Plan agent interfaces and data contracts
- Map data flow through the system
- Identify dependencies and build order
- Create architecture diagrams

**Input:** Phase requirements from ROADMAP.md
**Output:** Architecture plan (YAML) with new agents, modifications, data structures

**Example Output:**
```yaml
architecture_plan:
  new_agents:
    - name: story_arc_designer
      file: agents/story_arc_designer.py
      purpose: "Designs narrative flow across 9 panels"
  modifications:
    - file: agents/layout_compositor.py
      changes:
        - "Add support for 3x3 grid"
```

### 2. Implementation Agent
**File:** `implementation-agent.md`
**Role:** Writes production-quality Python code

**Responsibilities:**
- Write new agents with full implementation
- Modify existing code preserving style
- Add type hints and docstrings to all functions
- Handle errors explicitly (no silent fallbacks)
- Test code with example usage

**Input:** Architecture plan from Architecture Designer
**Output:** New/modified Python files with complete implementations

**Quality Standards:**
- PEP 8 compliance
- Type hints on all functions
- Google-style docstrings
- Fail-fast error handling

### 3. Testing Agent
**File:** `testing-agent.md`
**Role:** Creates comprehensive tests

**Responsibilities:**
- Create pytest test files for new agents
- Write integration tests for agent interactions
- Create visual regression tests
- Test backward compatibility
- Document test coverage

**Input:** Code implementation
**Output:** Test suite with unit, integration, and visual tests

**Coverage Goals:**
- Phase 0: 60%
- Phase 1: 70%
- Phase 2: 80%
- Phase 3+: 85%+

### 4. Documentation Agent
**File:** `documentation-agent.md`
**Role:** Maintains comprehensive documentation

**Responsibilities:**
- Update README with new features
- Create/update example YAML files
- Write phase completion summaries
- Update CHANGELOG with changes
- Document breaking changes with migration guides
- Create visual documentation

**Input:** Code changes and new features
**Output:** Updated docs, new examples, phase summaries

**Documentation Standards:**
- All examples must work
- Clear migration guides for breaking changes
- Visual examples (screenshots)
- Keep a Changelog format

### 5. Quality Assurance Agent
**File:** `qa-agent.md`
**Role:** Ensures production quality

**Responsibilities:**
- Review code quality (PEP 8, type hints, docstrings)
- Test backward compatibility
- Verify documentation accuracy
- Check visual quality of outputs
- Validate story coherence
- Performance benchmarking
- Generate QA reports

**Input:** Implementation results
**Output:** QA report with pass/fail, issues, human validation questions

**Quality Checks:**
- Code quality (PEP 8, types, docs)
- Functionality (tests, backward compat)
- Visual quality (contrast, layout)
- Story coherence (narrative flow)
- Performance (<5s generation)
- Accessibility (WCAG AA)

### 6. Breakdown Generator
**File:** `breakdown-generator.md`
**Role:** Creates meta breakdowns documenting Arkify's development

**Responsibilities:**
- Extract phase development data
- Create YAML file documenting the phase
- Run Arkify on the YAML to generate PNG
- Ensure meta breakdown is story-driven
- Capture authentic learnings

**Input:** Phase number and execution results
**Output:** YAML + PNG showing how the phase was built

**The Meta Beauty:**
Arkify documents its own development by generating breakdowns of each phase!

## Workflow Example: Phase 1 Execution

```
┌─────────────────────────────────────────────┐
│  USER INITIATES PHASE 1                     │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  1. ARCHITECTURE DESIGNER                   │
│  - Reads ROADMAP.md Phase 1 requirements    │
│  - Designs 3x3 grid layout system           │
│  - Plans Story Arc Designer agent           │
│  - Plans Graph Generator agent              │
│  - Output: architecture_plan.yaml           │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  2. IMPLEMENTATION AGENT                    │
│  - Reads architecture_plan.yaml             │
│  - Creates agents/story_arc_designer.py     │
│  - Creates agents/graph_generator.py        │
│  - Modifies agents/layout_compositor.py     │
│  - All code has type hints & docstrings     │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  3. TESTING AGENT                           │
│  - Creates tests/unit/test_story_arc.py     │
│  - Creates tests/integration/test_flow.py   │
│  - Runs all tests                           │
│  - Reports coverage: 78%                    │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  4. DOCUMENTATION AGENT                     │
│  - Updates README with 3x3 grid info        │
│  - Creates examples/story-example.yaml      │
│  - Updates CHANGELOG                        │
│  - Creates PHASE-1-COMPLETE.md              │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  5. QUALITY ASSURANCE AGENT                 │
│  - Reviews code quality: PASS               │
│  - Tests backward compatibility: PASS       │
│  - Validates visual outputs: PASS           │
│  - Checks story coherence: PASS             │
│  - Generates QA report                      │
│  - Creates validation questions             │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  🛑 HUMAN VALIDATION CHECKPOINT              │
│  - Review QA report                         │
│  - Test generated examples                  │
│  - Answer validation questions              │
│  - APPROVE / REJECT / DEFER                 │
└─────────────────────────────────────────────┘
                    ↓ (if approved)
┌─────────────────────────────────────────────┐
│  6. BREAKDOWN GENERATOR                     │
│  - Extracts Phase 1 development data        │
│  - Creates meta/phase-1-breakdown.yaml      │
│  - Runs: python arkify.py meta/phase-1...   │
│  - Output: meta/phase-1-breakdown.png       │
│  - Beautiful recursion! ✨                  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  PHASE 1 COMPLETE!                          │
│  - Code committed to git                    │
│  - Tagged as v0.1.0                         │
│  - Meta breakdown generated                 │
│  - Ready for next phase                     │
└─────────────────────────────────────────────┘
```

## How to Use These Agents

### Option 1: Manual Agent Invocation (Current)
Use Claude Code's Task tool to invoke individual agents:

```python
# Example: Architecture planning for Phase 1
Task(
    subagent_type="architecture-designer",
    description="Plan Phase 1 architecture",
    prompt="""
    Review ROADMAP.md Phase 1 requirements and create an architecture plan.
    Focus on 3x3 grid layout and story arc features.
    """
)
```

### Option 2: Coordinated Workflow (Future)
Create a main orchestration script that coordinates all agents:

```python
# phase_orchestrator.py (to be created)
def execute_phase(phase_number: int):
    # 1. Architecture planning
    arch_plan = invoke_agent("architecture-designer", phase=phase_number)

    # 2. Implementation
    code_results = invoke_agent("implementation-agent", plan=arch_plan)

    # 3. Testing
    test_results = invoke_agent("testing-agent", code=code_results)

    # 4. Documentation
    doc_results = invoke_agent("documentation-agent", changes=code_results)

    # 5. QA
    qa_report = invoke_agent("qa-agent", phase=phase_number)

    # 6. Human checkpoint
    approved = await_human_approval(qa_report)

    if approved:
        # 7. Meta breakdown
        breakdown = invoke_agent("breakdown-generator", phase=phase_number)
        return {"status": "COMPLETE", "breakdown": breakdown}
    else:
        return {"status": "REJECTED", "feedback": approved.feedback}
```

## Agent Coordination Principles

### 1. Sequential Dependencies
Some agents must run in order:
- Architecture → Implementation → Testing → Documentation → QA

### 2. Parallel Opportunities
Some can run in parallel:
- Documentation + Testing (both work on implementation results)
- QA can review code while Documentation creates examples

### 3. Human in the Loop
Critical checkpoint after QA, before finalization:
- Human reviews QA report
- Human tests generated examples
- Human approves/rejects phase
- System iterates if rejected

### 4. Self-Documentation
Every phase generates its own breakdown:
- Breakdown Generator uses Arkify on itself
- Creates meta/phase-X-breakdown.png
- Shows development journey visually

## Quality Gates

Each agent acts as a quality gate:

```
Architecture → Implementation → Testing → Documentation → QA → Human → Meta
     ↓              ↓             ↓            ↓         ↓       ↓      ↓
  [PLAN OK]    [CODE OK]    [TESTS OK]   [DOCS OK] [QA PASS] [APPROVE] [SHIP]
```

If any gate fails, the phase doesn't proceed.

## File Organization

```
.claude/agents/
├── README.md                      # This file
├── architecture-designer.md       # Plans structure
├── implementation-agent.md        # Writes code
├── testing-agent.md              # Creates tests
├── documentation-agent.md        # Maintains docs
├── qa-agent.md                   # Reviews quality
└── breakdown-generator.md        # Meta documentation
```

## Key Differences from Python Meta-Agents

**Python Meta-Agents (meta_agents/):**
- Executable Python code
- Runs in meta_runner.py
- Automated coordination
- Checkpoint Manager handles human validation

**Claude Code Agents (.claude/agents/):**
- Markdown specifications
- Invoked via Claude Code Task tool
- Manual/semi-automated coordination
- Human validation via interactive Q&A

**Both approaches are valid!** The Claude Code agents leverage Claude's strengths in understanding complex specifications and generating high-quality code from detailed prompts.

## Design Philosophy

### KISS (Keep It Simple, Stupid)
Each agent has ONE clear responsibility. No god agents.

### Fail Fast
Agents surface errors immediately. No silent fallbacks. (Critical from CLAUDE.md)

### Story-Driven
Even technical agents think about narrative (Architecture Designer considers user journey).

### Quality Over Speed
Each agent prioritizes doing things right over doing things fast.

### Recursive Meta-Programming
The system documents itself using its own output. Beautiful recursion.

## Next Steps

1. **Test Agent Workflow** - Execute Phase 1 using these agents
2. **Create Orchestration Script** - Automate agent coordination
3. **Add Agent Templates** - Standardize agent output formats
4. **Measure Performance** - Track agent execution times
5. **Iterate Based on Results** - Improve agent prompts based on real usage

## Contributing

To add a new agent:
1. Create `new-agent.md` in this directory
2. Follow the structure of existing agents
3. Define role, responsibilities, input/output
4. Add examples and quality standards
5. Update this README

## The Meta Loop

```
Arkify generates project breakdowns
    ↓
Claude Code agents build Arkify
    ↓
Breakdown Generator uses Arkify on itself
    ↓
Meta breakdowns document the development
    ↓
Community sees the journey
    ↓
Both Arkify and agents improve
```

**This is ultrathinking meets ultrabuilding.** 🧠🚀

---

*Last updated: 2025-10-22*
*System Status: All 6 agents specified, ready for Phase 1 execution*
