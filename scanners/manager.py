from models.target import Target
from models.scan_result import ScanResult

from scanners.factory import ScannerFactory


class ScannerManager:
    """
    Executes all scanners returned by the ScannerFactory.
    """

    def run(self, target: Target) -> list[ScanResult]:

        results: list[ScanResult] = []

        for scanner_cls in ScannerFactory.get_scanners():

            scanner = scanner_cls(target)

            result = scanner.run()

            results.append(result)

        return results
