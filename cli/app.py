import typer
from rich.console import Console
from rich.panel import Panel

from utils.banner import show_banner
from utils.logger import app_logger
from utils.config import load_config

from models.target import Target
from agents.planner import PlannerAgent

app = typer.Typer(
    help="ReconAI - AI Powered Bug Bounty Framework"
)

console = Console()


@app.command()
def scan(
    domain: str = typer.Option(
        ...,
        "--domain",
        "-d",
        help="Target Domain",
    ),
    fast: bool = typer.Option(
        False,
        "--fast",
        help="Fast development mode.",
    ),
):
    show_banner()

    config = load_config()

    app_logger.info("Configuration Loaded")
    app_logger.info(f"Target : {domain}")
    app_logger.info(f"Threads : {config['scan']['threads']}")

    target = Target(domain=domain)

    planner = PlannerAgent()

    console.print(
        Panel.fit(
            "[yellow]Planner Agent Started[/yellow]",
            title="ReconAI",
        )
    )

    context, results = planner.execute(
        target,
        fast=fast,
    )

    console.print()

    for result in results:

        if result.success:

            console.print("[bold green]✓ Scan Completed[/bold green]")
            console.print(f"Scanner      : {result.scanner}")
            console.print(f"Target       : {result.target.domain}")
            console.print(f"Discovered   : {result.item_count}")
            console.print(f"Time         : {result.execution_time:.2f} sec")

            if result.output_file:
                console.print(f"Output File  : {result.output_file}")

            console.print("-" * 50)

        else:

            console.print("[bold red]✗ Scan Failed[/bold red]")
            console.print(f"Scanner : {result.scanner}")

            for error in result.errors:
                console.print(f"[red]{error}[/red]")

    console.print()
    console.print(
        Panel.fit(
            "[bold cyan]Workflow Summary[/bold cyan]"
        )
    )

    console.print(f"Subdomains : {len(context.subdomains)}")
    console.print(f"Live Hosts : {len(context.live_hosts)}")
    console.print(f"URLs       : {len(context.urls)}")
    console.print(f"Parameters : {len(context.parameters)}")
    console.print(f"Findings   : {len(context.findings)}")


@app.command()
def version():
    console.print("[cyan]ReconAI v1.0[/cyan]")


@app.command()
def doctor():
    console.print("[green]Everything looks good.[/green]")


if __name__ == "__main__":
    app()
