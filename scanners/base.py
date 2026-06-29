from abc import ABC, abstractmethod

from models.scan_result import ScanResult
from models.target import Target


class BaseScanner(ABC):
    """
    Base class for all scanners.
    """

    def __init__(self, target: Target):
        self.target = target

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
