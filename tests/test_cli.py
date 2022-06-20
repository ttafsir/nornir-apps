from click.testing import CliRunner, Result
from nrcli.cli import cli
from nrcli.plugins import DEFAULT_PLUGINS
from nrcli.version import __version__


class TestCli:
    """Test general functionality of the CLI"""

    def test_entrypoint(self):
        """
        Is entrypoint script installed? (setup.py)
        """
        runner: CliRunner = CliRunner()
        result: Result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0

    def test_version_displays_library_version(self):
        """
        Arrange/Act: Run the `version` subcommand.
        Assert: The output matches the library version.
        """
        runner: CliRunner = CliRunner()
        result: Result = runner.invoke(cli, ["--version"])
        assert (
            __version__ in result.output.strip()
        ), "Version number should match library version."

    def test_default_plugins_are_not_listed_by_default(self):
        """
        Arrange/Act: Run the `plugins` command without the `--all` flag.
        Assert: None of the default plugins should be present in the output.
        """
        runner: CliRunner = CliRunner()
        result: Result = runner.invoke(cli, ["plugins"])
        assert all(plugin not in result.output for plugin in DEFAULT_PLUGINS)

    def test_default_plugins_are_listed_w_all_flag(self):
        """
        Arrange/Act: Run the `plugins` command without the `--all` flag.
        Assert: None of the default plugins should be present in the output.
        """
        runner: CliRunner = CliRunner()
        result: Result = runner.invoke(cli, ["plugins", "--all"])
        assert all(plugin in result.output for plugin in DEFAULT_PLUGINS)
