import tempfile
import time
from pathlib import Path

from models.scan_result import ScanResult
from scanners.base import BaseScanner
from utils.command_runner import CommandRunner


class NucleiScanner(BaseScanner):

    @property
    def name(self) -> str:
        return "nuclei"

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
            self.target.output_dir / "nuclei.txt"
        )

        command = [
            "nuclei",
            "-l",
            str(input_file),
            "-silent",
            "-o",
            str(output_file),
        ]

        # Fast Development Mode
        if self.context.fast:
            command.extend([
                "-severity",
                "critical,high,medium",
            ])

        result = CommandRunner.run(
            command,
            timeout=1800,
        )

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

            findings = [
                line.strip()
                for line in output_file.read_text().splitlines()
                if line.strip()
            ]

        else:
            findings = []

        self.context.findings.extend(findings)

        return ScanResult(
            scanner=self.name,
            target=self.target,
            success=True,
            execution_time=elapsed,
            output_file=output_file,
            data=findings,
            metadata={
                "count": len(findings),
            },
        )
