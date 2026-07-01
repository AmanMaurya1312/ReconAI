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

    def add_subdomains(self, items: list[str]) -> None:
        self.subdomains = sorted(set(self.subdomains + items))

    def add_live_hosts(self, items: list[str]) -> None:
        self.live_hosts = sorted(set(self.live_hosts + items))

    def add_urls(self, items: list[str]) -> None:
        self.urls = sorted(set(self.urls + items))

    def add_parameters(self, items: list[str]) -> None:
        self.parameters = sorted(set(self.parameters + items))

    def add_javascript_files(self, items: list[str]) -> None:
        self.javascript_files = sorted(set(self.javascript_files + items))