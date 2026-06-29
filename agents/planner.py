from models.target import Target
from scanners.manager import ScannerManager


class PlannerAgent:
    """
    Planner Agent.

    Decides which scanners should execute.
    """

    def __init__(self):

        self.manager = ScannerManager()

    def execute(self, target: Target):

        return self.manager.run(target)
