from models.execution_context import ExecutionContext
from models.target import Target
from scanners.manager import ScannerManager


class WorkflowEngine:
    """
    Orchestrates the complete reconnaissance workflow.
    """

    def __init__(self):
        self.manager = ScannerManager()

    def execute(self, target: Target):

        context = ExecutionContext(
            target=target.domain,
        )

        results = self.manager.run(
            target=target,
            context=context,
        )

        return context, results
