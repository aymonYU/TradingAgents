import questionary
from typing import List
from cli.models import AnalystType
from rich.console import Console

console = Console()

def get_ticker() -> str:
    """Prompt the user to enter a ticker symbol."""
    ticker = questionary.text(
        "Enter the ticker symbol to analyze:",
        default="NVDA",
        validate=lambda x: len(x.strip()) > 0 or "Please enter a valid ticker symbol.",
        style=questionary.Style([
            ("text", "fg:green"),
            ("highlighted", "noinherit"),
        ]),
    ).ask()

    if not ticker:
        console.print("\n[red]No ticker symbol provided. Exiting...[/red]")
        exit(1)

    return ticker.strip().upper()

def validate_date(date_str: str) -> bool:
    """Validate date format YYYY-MM-DD."""
    try:
        from datetime import datetime
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def get_analysis_date() -> str:
    """Get analysis date from user."""
    date_str = questionary.text(
        "Enter the analysis date (YYYY-MM-DD):",
        default="2024-05-10",
        validate=lambda x: validate_date(x) or "Please enter a valid date in YYYY-MM-DD format",
        style=questionary.Style([
            ("text", "fg:green"),
            ("highlighted", "noinherit"),
        ]),
    ).ask()

    if not date_str:
        console.print("\n[red]No date provided. Exiting...[/red]")
        exit(1)

    return date_str.strip()

# Fixed analyst configuration - no need for selection
DEFAULT_ANALYSTS = [
    AnalystType.MARKET,
    AnalystType.SOCIAL,
    AnalystType.NEWS,
    AnalystType.FUNDAMENTALS,
]

# Fixed research depth - no need for selection
DEFAULT_RESEARCH_DEPTH = 3
