#!/usr/bin/env python3
"""
Meta Runner - Execute Arkify Development with Multi-Agent System

This script orchestrates the meta-agent system to build Arkify itself,
phase by phase, with human validation checkpoints.

Usage:
    python meta_runner.py --phase 1
    python meta_runner.py --phase 2 --skip-checkpoint
    python meta_runner.py --resume checkpoint-id
"""

import sys
import argparse
from pathlib import Path

from meta_agents.orchestrator import MainOrchestrator
from meta_agents.sub_agents import (
    ArchitectureDesigner,
    ImplementationAgent,
    TestingAgent,
    DocumentationAgent,
    QualityAssuranceAgent,
    BreakdownGenerator
)


def setup_orchestrator() -> MainOrchestrator:
    """
    Set up Main Orchestrator with all sub-agents.

    Returns:
        Configured orchestrator
    """
    print("\n🎬 Initializing Meta-Agent System...")
    print("="*70)

    orchestrator = MainOrchestrator()

    # Register all sub-agents
    print("\n📋 Registering Sub-Agents:")
    orchestrator.register_agent(ArchitectureDesigner())
    orchestrator.register_agent(ImplementationAgent())
    orchestrator.register_agent(TestingAgent())
    orchestrator.register_agent(DocumentationAgent())
    orchestrator.register_agent(QualityAssuranceAgent())
    orchestrator.register_agent(BreakdownGenerator())

    print(f"\n✅ {len(orchestrator.list_available_agents())} agents ready")
    print("="*70)

    return orchestrator


def execute_phase(phase: int, skip_checkpoint: bool = False):
    """
    Execute a single phase.

    Args:
        phase: Phase number to execute
        skip_checkpoint: Skip human validation (for testing)
    """
    orchestrator = setup_orchestrator()

    print(f"\n{'='*70}")
    print(f"  🚀 EXECUTING PHASE {phase}")
    print(f"{'='*70}\n")

    context = {
        'phase': phase,
        'skip_checkpoint': skip_checkpoint
    }

    result = orchestrator.execute(context)

    # Display results
    print("\n" + "="*70)
    print("  📊 PHASE EXECUTION SUMMARY")
    print("="*70 + "\n")

    print(f"Status: {result.get('status', 'UNKNOWN')}")
    print(f"Phase:  {result.get('phase')}")

    if result.get('status') == 'COMPLETED':
        print(f"\n✅ Phase {phase} completed successfully!")
        print(f"\nMilestone Breakdown:")
        breakdown = result.get('breakdown', {})
        print(f"  YAML: {breakdown.get('yaml_file')}")
        print(f"  PNG:  {breakdown.get('output_file')}")

        if result.get('human_feedback'):
            print(f"\nHuman Feedback:")
            print(f"  {result['human_feedback']}")

    elif result.get('status') == 'REJECTED':
        print(f"\n❌ Phase {phase} rejected by human validation")
        print(f"\nFeedback: {result.get('feedback')}")

    elif result.get('status') == 'FAILED':
        print(f"\n❌ Phase {phase} failed")
        print(f"\nError: {result.get('error')}")

    print("\n" + "="*70)


def show_status():
    """Show overall meta-agent system status."""
    orchestrator = setup_orchestrator()

    print("\n" + "="*70)
    print("  📊 META-AGENT SYSTEM STATUS")
    print("="*70 + "\n")

    print("Registered Agents:")
    for agent_name in orchestrator.list_available_agents():
        print(f"  ✓ {agent_name}")

    print(f"\nPhase History:")
    if orchestrator.phase_history:
        for phase_record in orchestrator.phase_history:
            phase = phase_record['phase']
            status = phase_record['status']
            print(f"  Phase {phase}: {status}")
    else:
        print("  (No phases executed yet)")

    print("\n" + "="*70)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Meta-Agent System for building Arkify'
    )

    parser.add_argument(
        '--phase',
        type=int,
        help='Phase number to execute (1-8)'
    )

    parser.add_argument(
        '--skip-checkpoint',
        action='store_true',
        help='Skip human validation checkpoint (for testing)'
    )

    parser.add_argument(
        '--status',
        action='store_true',
        help='Show system status'
    )

    parser.add_argument(
        '--resume',
        type=str,
        help='Resume from checkpoint ID'
    )

    args = parser.parse_args()

    # Show banner
    print("\n" + "="*70)
    print("  🤖 ARKIFY META-AGENT SYSTEM")
    print("  Building Arkify Using Multi-Agent Orchestration")
    print("="*70)

    if args.status:
        show_status()

    elif args.phase:
        if args.phase < 1 or args.phase > 8:
            print(f"\n❌ Invalid phase: {args.phase}")
            print("   Valid phases: 1-8 (see ROADMAP.md)")
            sys.exit(1)

        execute_phase(args.phase, skip_checkpoint=args.skip_checkpoint)

    elif args.resume:
        print(f"\n⏸️  Resume functionality coming soon...")
        print(f"   Checkpoint ID: {args.resume}")

    else:
        parser.print_help()
        print("\n💡 Examples:")
        print("   python meta_runner.py --status")
        print("   python meta_runner.py --phase 1")
        print("   python meta_runner.py --phase 2 --skip-checkpoint")


if __name__ == '__main__':
    main()
