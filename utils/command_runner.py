import subprocess
from pathlib import Path
from typing import Optional

from loguru import logger


class CommandRunner:
    """
    Executes external commands safely.
    """

    @staticmethod
    def run(
        command: list[str],
        cwd: Optional[Path] = None,
        timeout: int = 300,
    ) -> subprocess.CompletedProcess:

        logger.info(f"Running command: {' '.join(command)}")

        try:
            result = subprocess.run(
                command,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False,
            )

            logger.info(
                f"Command finished with exit code {result.returncode}"
            )

            return result

        except subprocess.TimeoutExpired as e:
            logger.error("Command timed out")
            raise RuntimeError("Command execution timed out.") from e

        except FileNotFoundError as e:
            logger.error(f"Command not found: {command[0]}")
            raise RuntimeError(f"{command[0]} is not installed.") from e
