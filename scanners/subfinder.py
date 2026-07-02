import time

from models.scan_result import ScanResult
from scanners.base import BaseScanner
from utils.command_runner import CommandRunner


class SubfinderScanner(BaseScanner):

    @property
    def name(self) -> str:
        return "subfinder"

    def run(self) -> ScanResult:

        start = time.perf_counter()

        output_file = self.target.output_dir / "subfinder.txt"

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        command = [
            "subfinder",
            "-silent",
            "-d",
            self.target.domain,
            "-o",
            str(output_file),
        ]

        result = CommandRunner.run(
            command,
            timeout=180,
        )

        elapsed = time.perf_counter() - start

        if result.returncode != 0:
            return ScanResult(
                scanner=self.name,
                target=self.target,
                success=False,
                execution_time=elapsed,
                output_file=output_file,
                errors=[result.stderr.strip()],
            )

        if output_file.exists():
            data = [
                line.strip()
                for line in output_file.read_text().splitlines()
                if line.strip()
            ]
        else:
            data = []

        # Save unique subdomains into shared context
        self.context.add_subdomains(data)

        unique_subdomains = self.context.subdomains

        return ScanResult(
            scanner=self.name,
            target=self.target,
            success=True,
            execution_time=elapsed,
            output_file=output_file,
            data=unique_subdomains,
            metadata={
                "raw_count": len(data),
                "unique_count": len(unique_subdomains),
            },
        )