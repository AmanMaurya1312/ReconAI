from models.execution_context import ExecutionContext
from models.scan_result import ScanResult
from models.target import Target

from scanners.factory import ScannerFactory


class ScannerManager:
    """
    Executes all scanners returned by the ScannerFactory.
    """

    def run(
        self,
        target: Target,
        context: ExecutionContext | None = None,
    ) -> list[ScanResult]:

        results: list[ScanResult] = []

        for scanner_cls in ScannerFactory.get_scanners():

            scanner = scanner_cls(target, context)

            result = scanner.run()

            results.append(result)

        return results
