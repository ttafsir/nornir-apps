import os

from click.testing import Result
from nrcli.plugins import DEFAULT_PLUGINS
from nrcli.version import __version__


class TestCli:
    """Test general functionality of the CLI"""

    def test_entrypoint(self, run_cli_command):
        """
        Is entrypoint script installed? (setup.py)
        """
        result: Result = run_cli_command(["--help"])
        assert result.exit_code == 0

    def test_version_displays_library_version(self, run_cli_command):
        """
        Arrange/Act: Run the `version` subcommand.
        Assert: The output matches the library version.
        """
        result: Result = run_cli_command(["--version"])
        assert (
            __version__ in result.output.strip()
        ), "Version number should match library version."

    def test_default_plugins_are_not_listed_by_default(self, run_cli_command):
        """
        Arrange/Act: Run the `plugins` command without the `--all` flag.
        Assert: None of the default plugins should be present in the output.
        """
        result: Result = run_cli_command(["plugins"])
        assert all(
            plugin not in result.output for plugin in DEFAULT_PLUGINS
        ), result.output

    def test_default_plugins_are_listed_w_all_flag(self, run_cli_command):
        """
        Arrange/Act: Run the `plugins` command with the `--all` flag.
        Assert: All plugins should be present in the output.
        """
        result: Result = run_cli_command(["plugins", "--all"])
        assert result.exit_code == 0
        assert all(
            plugin in result.output for plugin in DEFAULT_PLUGINS
        ), result.exc_info
