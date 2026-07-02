import tempfile
import time
from pathlib import Path

from models.scan_result import ScanResult
from scanners.base import BaseScanner
from utils.command_runner import CommandRunner


class HttpxScanner(BaseScanner):

    @property
    def name(self) -> str:
        return "httpx"

    def run(self) -> ScanResult:

        start = time.perf_counter()

        if not self.context.subdomains:
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

            f.write("\n".join(self.context.subdomains))
            input_file = Path(f.name)

        output_file = (
            self.target.output_dir / "httpx.txt"
        )

        command = [
            "httpx",
            "-silent",
            "-l",
            str(input_file),
            "-o",
            str(output_file),
        ]

        # Fast Development Mode
        if self.context.fast:
            command.extend([
                "-threads", "50",
                "-timeout", "5",
                "-retries", "1",
            ])
        else:
            command.extend([
                "-threads", "200",
                "-timeout", "10",
                "-retries", "2",
            ])

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

            live_hosts = [
                line.strip()
                for line in output_file.read_text().splitlines()
                if line.strip()
            ]

        else:
            live_hosts = []

        self.context.add_live_hosts(live_hosts)

        return ScanResult(
            scanner=self.name,
            target=self.target,
            success=True,
            execution_time=elapsed,
            output_file=output_file,
            data=live_hosts,
            metadata={
                "count": len(live_hosts)
            },
        )