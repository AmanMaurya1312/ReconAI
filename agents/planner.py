from models.target import Target
from workflow.engine import WorkflowEngine


class PlannerAgent:
    """
    Planner Agent.

    Decides which workflow should execute.
    """

    def __init__(self):
        self.engine = WorkflowEngine()

    def execute(
        self,
        target: Target,
        fast: bool = False,
    ):
        """
        Execute the reconnaissance workflow.
        """
        return self.engine.execute(
            target,
            fast=fast,
        )