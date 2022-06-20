import click
from nornir_napalm.plugins.tasks import napalm_get
from nornir_apps.commands.common import add_common_options
from nornir_apps.hookspecs import hookimpl


@hookimpl
def add_subcommand(nornir_apps):
    """Add subcommand to nornir_apps"""

    @nornir_apps.command(name="napalm-get")
    @click.option(
        "-g",
        "--getters",
        help="list of getters to use",
        multiple=True,
        default=["facts"],
    )
    @add_common_options
    @click.pass_context
    def get_config(ctx, getters, **cli_options):
        """Retrieve device configuration using napalm getters"""
        runner = ctx.obj.runner
        output = runner.run(task=napalm_get, getters=getters)
        if cli_options.get("output") == "text":
            ctx.obj.console_printer(output)
        return output
