from models.execution_context import ExecutionContext
from models.target import Target
from scanners.manager import ScannerManager


class WorkflowEngine:
    """
    Orchestrates the complete reconnaissance workflow.
    """

    def __init__(self):
        self.manager = ScannerManager()

    def execute(
        self,
        target: Target,
        fast: bool = False,
    ):

        context = ExecutionContext(
            target=target.domain,
        )

        # Fast mode flag
        context.fast = fast

        results = self.manager.run(
            target=target,
            context=context,
        )

        return context, results