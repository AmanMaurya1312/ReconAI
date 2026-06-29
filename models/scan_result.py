from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from models.target import Target


@dataclass(slots=True)
class ScanResult:
    """
    Standard result returned by every scanner.
    """

    scanner: str
    target: Target
    success: bool

    data: Any = None
    execution_time: float = 0.0

    output_file: Path | None = None

    errors: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def has_errors(self) -> bool:
        """
        Returns True if any errors were recorded.
        """
        return len(self.errors) > 0

    @property
    def item_count(self) -> int:
        """
        Returns the number of discovered items.
        """
        if isinstance(self.data, (list, tuple, set, dict)):
            return len(self.data)

        return 0
