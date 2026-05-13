# filepath: lorein-cli/tests/test_cli.py
from click.testing import CliRunner
import pytest
from app.main import cli

def test_cli_list_heartbeat_success():
    """Unit Test: Ensure list command parses correctly and prints status."""
    runner = CliRunner()
    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert "Engine Status:" in result.output or "Unable to connect" in result.output

def test_cli_parse_missing_option_fails():
    """Unit Test: Ensure parse command crashes if --text is omitted."""
    runner = CliRunner()
    result = runner.invoke(cli, ["parse"])
    assert result.exit_code != 0
    assert "Error: Missing option" in result.output

def test_integration_crud_create_template_fails():
    """TDD Integration: Must clear successfully with the structural mock."""
    runner = CliRunner()
    result = runner.invoke(cli, ["template", "create", "audit-expert"])
    assert result.exit_code == 0
    assert "CRUD Action: Registering template" in result.output

def test_integration_pydantic_persistence_fails():
    """TDD Integration: Must detect validation error on malformed layout."""
    runner = CliRunner()
    result = runner.invoke(cli, ["parse", "--text", "{{INVALID FIELD}}"])
    assert result.exit_code == 0
    assert "SchemaValidationError" in result.output
