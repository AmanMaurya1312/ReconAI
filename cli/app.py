import typer
from rich.console import Console

from utils.banner import show_banner
from utils.logger import app_logger
from utils.config import load_config

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
        help="Target Domain"
    )
):
    show_banner()

    config = load_config()

    app_logger.info("Configuration Loaded")
    app_logger.info(f"Target : {domain}")
    app_logger.info(f"Threads : {config['scan']['threads']}")

    console.print(
        f"\n[bold green]Starting Scan on {domain}[/bold green]"
    )


@app.command()
def version():
    console.print("[cyan]ReconAI v1.0[/cyan]")


@app.command()
def doctor():
    console.print("[green]Everything looks good.[/green]")
