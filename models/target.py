from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Target:
    """
    Represents a reconnaissance target.
    This object is shared across all scanners and agents.
    """

    domain: str
    scheme: str = "https"
    output_dir: Path = Path("output")
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate the target after initialization.
        """
        self.domain = self.domain.strip()

        if not self.domain:
            raise ValueError("Target domain cannot be empty.")
