"""
Base Agent Class

All specialized agents inherit from this base class.
Provides common functionality and enforces agent contract.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List
from datetime import datetime


class BaseAgent(ABC):
    """
    Base class for all meta-agents.

    Each agent is specialized in one aspect of building Arkify.
    Agents must implement execute() and provide clear outputs.
    """

    def __init__(self, name: str, description: str):
        """
        Initialize base agent.

        Args:
            name: Agent name (e.g., "Architecture Designer")
            description: What this agent does
        """
        self.name = name
        self.description = description
        self.execution_history: List[Dict[str, Any]] = []

    @abstractmethod
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute agent's primary task.

        Args:
            context: Input context (phase info, current state, etc.)

        Returns:
            Dictionary with results and any generated artifacts
        """
        pass

    def log_execution(self, context: Dict[str, Any], result: Dict[str, Any]):
        """
        Log execution for audit trail.

        Args:
            context: Input context
            result: Execution result
        """
        self.execution_history.append({
            'timestamp': datetime.now().isoformat(),
            'context': context,
            'result': result,
        })

    def get_status(self) -> Dict[str, Any]:
        """
        Get current agent status.

        Returns:
            Status dictionary
        """
        return {
            'name': self.name,
            'description': self.description,
            'executions': len(self.execution_history),
            'last_execution': self.execution_history[-1] if self.execution_history else None,
        }

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name='{self.name}')>"
