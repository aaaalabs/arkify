# Arkify Claude Code Agents

**Six specialized agents that build Arkify phase by phase.**

## The Agents

### 1. Architecture Designer
**Invocation:** Use when planning new features or major refactoring
**Tools:** Read, Glob, Grep, Write
**Model:** Sonnet

Plans code structure, agent interfaces, and system architecture. Creates detailed YAML specifications for implementation.

### 2. Implementation Agent
**Invocation:** Use when writing or modifying code
**Tools:** Read, Write, Edit, Grep, Glob, Bash
**Model:** Sonnet

Writes production-quality Python code with type hints, docstrings, and fail-fast error handling. Matches existing code patterns.

### 3. Testing Agent
**Invocation:** Use when creating tests for new features
**Tools:** Read, Write, Edit, Bash, Grep, Glob
**Model:** Sonnet

Creates comprehensive pytest tests including unit, integration, and visual regression tests. Ensures backward compatibility.

### 4. Documentation Agent
**Invocation:** Use when features are added or modified
**Tools:** Read, Write, Edit, Bash, Grep, Glob
**Model:** Sonnet

Maintains clear, example-driven documentation. Updates README, CHANGELOG, examples, and migration guides.

### 5. QA Agent
**Invocation:** Use before phase completion
**Tools:** Read, Bash, Grep, Glob, Write
**Model:** Opus

Ensures production quality through code review, visual quality checks, story coherence validation, and performance benchmarking.

### 6. Breakdown Generator
**Invocation:** Use after phase completion
**Tools:** Read, Write, Bash, Grep, Glob
**Model:** Sonnet

Creates meta breakdowns documenting Arkify's development using Arkify itself. Beautiful recursion!

## How to Use

### View Available Agents
In Claude Code, type `/agents` to see all available agents.

### Invoke an Agent
Use the Task tool with the agent name:

```
Use the architecture-designer agent to plan Phase 1 features from ROADMAP.md
```

or

```
Use the testing-agent to create tests for the Story Arc Designer
```

## Agent Workflow: Phase 1 Example

```
1. architecture-designer → Plans 3x3 grid system
2. implementation-agent → Writes Story Arc Designer code
3. testing-agent → Creates comprehensive tests
4. documentation-agent → Updates docs and examples
5. qa-agent → Reviews quality, generates QA report
6. [Human Checkpoint] → Review and approve
7. breakdown-generator → Creates meta breakdown PNG
```

## Agent Coordination

### Sequential Dependencies
Some agents must run in order:
- Architecture → Implementation → Testing → Documentation → QA

### Parallel Opportunities
Some can run in parallel:
- Documentation + Testing (both work on implementation results)

### Human in the Loop
Critical checkpoint after QA, before finalization.

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
```

**This is ultrathinking meets ultrabuilding.** 🧠🚀

---

*Last updated: 2025-10-22*
*All 6 agents implemented and ready for use*
