import tempfile
import time
from pathlib import Path

from models.scan_result import ScanResult
from scanners.base import BaseScanner
from utils.command_runner import CommandRunner


class KatanaScanner(BaseScanner):

    @property
    def name(self) -> str:
        return "katana"

    def run(self) -> ScanResult:

        start = time.perf_counter()

        if not self.context.live_hosts:
            return ScanResult(
                scanner=self.name,
                target=self.target,
                success=True,
                data=[],
                metadata={"count": 0},
            )

        with tempfile.NamedTemporaryFile(
            mode="w",
            delete=False,
        ) as f:

            f.write("\n".join(self.context.live_hosts))
            input_file = Path(f.name)

        output_file = (
            self.target.output_dir / "katana.txt"
        )

        command = [
            "katana",
            "-silent",
            "-list",
            str(input_file),
            "-o",
            str(output_file),
        ]

        result = CommandRunner.run(command)

        elapsed = time.perf_counter() - start

        input_file.unlink(missing_ok=True)

        if result.returncode != 0:

            return ScanResult(
                scanner=self.name,
                target=self.target,
                success=False,
                execution_time=elapsed,
                errors=[result.stderr.strip()],
            )

        if output_file.exists():

            urls = [
                line.strip()
                for line in output_file.read_text().splitlines()
                if line.strip()
            ]

        else:
            urls = []

        self.context.urls.extend(urls)

        return ScanResult(
            scanner=self.name,
            target=self.target,
            success=True,
            execution_time=elapsed,
            output_file=output_file,
            data=urls,
            metadata={
                "count": len(urls)
            },
        )
