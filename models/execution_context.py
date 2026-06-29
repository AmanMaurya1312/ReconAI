from dataclasses import dataclass, field


@dataclass
class ExecutionContext:
    """
    Shared execution state for the entire workflow.
    """

    target: str

    subdomains: list[str] = field(default_factory=list)
    live_hosts: list[str] = field(default_factory=list)
    urls: list[str] = field(default_factory=list)
    parameters: list[str] = field(default_factory=list)
    javascript_files: list[str] = field(default_factory=list)
    secrets: list[str] = field(default_factory=list)
    findings: list[dict] = field(default_factory=list)
