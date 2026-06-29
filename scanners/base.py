from abc import ABC, abstractmethod

from models.execution_context import ExecutionContext
from models.scan_result import ScanResult
from models.target import Target


class BaseScanner(ABC):
    """
    Base class for all scanners.
    """

    def __init__(
        self,
        target: Target,
        context: ExecutionContext,
    ):
        self.target = target
        self.context = context

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Scanner name.
        """
        pass

    @abstractmethod
    def run(self) -> ScanResult:
        """
        Execute scanner.
        """
        pass
