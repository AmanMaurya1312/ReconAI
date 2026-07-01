import time

from models.scan_result import ScanResult
from scanners.base import BaseScanner
from utils.command_runner import CommandRunner


class GauScanner(BaseScanner):

    @property
    def name(self) -> str:
        return "gau"

    def run(self) -> ScanResult:

        start = time.perf_counter()

        output_file = self.target.output_dir / "gau.txt"

        command = [
            "gau",
            self.target.domain,
            "--subs",
            "--providers",
            "wayback,commoncrawl,otx,urlscan",
            "--o",
            str(output_file),
        ]

        result = CommandRunner.run(command)

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
            urls = sorted(set(
                line.strip()
                for line in output_file.read_text().splitlines()
                if line.strip()
            ))
        else:
            urls = []

        self.context.add_urls(urls)

        return ScanResult(
            scanner=self.name,
            target=self.target,
            success=True,
            execution_time=elapsed,
            output_file=output_file,
            data=urls,
            metadata={
                "count": len(urls),
            },
        )