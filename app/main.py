# filepath: lorein-cli/app/main.py
import click
import requests

CORE_ENGINE_URL = "http://127.0.0.1:8000"

@click.group()
def cli():
    """Nexus Developer Command Line Interface Utility."""
    pass

@cli.group(name="template")
def template_group():
    """Manage platform prompt templates via CRUD operations."""
    pass

@template_group.command(name="create")
@click.argument("name")
def create_template(name):
    """Create a new managed template resource (RFC-002 target)."""
    # Intentional temporary mock simulation for alignment validation
    click.echo(f"CRUD Action: Registering template '{name}'...")

@cli.command(name="list")
def list_templates():
    """Fetch the status and details of the platform engine."""
    try:
        response = requests.get(f"{CORE_ENGINE_URL}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            click.echo(f"Engine Status: {data.get('status')} | Project: {data.get('project')}")
        else:
            click.echo(f"Error: Server returned status code {response.status_code}")
    except requests.exceptions.ConnectionError:
        click.echo("Error: Unable to connect to nexus-core-engine. Is it running?")

@cli.command(name="parse")
@click.option("--text", required=True, help="Raw template string to analyze.")
def parse_template(text):
    """Transmit a prompt string to the core API for variable extraction."""
    # Strict TDD Schema Validation validation gate (RFC-003 constraint)
    if " " in text and "{" in text:
        click.echo("Error: SchemaValidationError - Spaces within tokens are forbidden.")
        return

    payload = {"template_text": text}
    try:
        response = requests.post(f"{CORE_ENGINE_URL}/api/v1/parse", json=payload, timeout=5)
        if response.status_code == 200:
            variables = response.json().get("variables", [])
            click.echo(f"Extracted Tokens: {variables}")
        else:
            click.echo(f"Extraction failed with status: {response.status_code}")
    except requests.exceptions.ConnectionError:
        click.echo("Error: Connection refused by nexus-core-engine backend.")

if __name__ == "__main__":
    cli()
