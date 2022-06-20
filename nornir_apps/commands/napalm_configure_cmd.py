import click
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_apps.commands.common import add_common_options
from nornir_apps.hookspecs import hookimpl


@hookimpl
def add_subcommand(nornir_apps):
    """Add subcommand to nornir_apps"""

    @nornir_apps.command(name="napalm-configure")
    @click.option("--dry-run", is_flag=True, default=False)
    @click.option("-c", "--config", help="config to load into the device")
    @click.option(
        "-r",
        "--replace",
        help="whether to replace or merge the configuration",
        is_flag=True,
        default=False,
    )
    @click.option("-m", "--commit-message", help="commit_message")
    @add_common_options
    @click.pass_context
    def configure(ctx, dry_run, replace, commit_message, **cli_options):
        """Retrieve device configuration"""
        runner = ctx.obj.runner
        output = runner.run(
            task=napalm_configure,
            dry_run=dry_run,
            replace=replace,
            commit_message=commit_message,
        )
        if cli_options.get("output") == "text":
            ctx.obj.console_printer(output)
        return output
