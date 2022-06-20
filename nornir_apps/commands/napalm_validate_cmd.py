import click
from nornir_napalm.plugins.tasks import napalm_validate
from nornir_apps.commands.common import add_common_options
from nornir_apps.hookspecs import hookimpl


@hookimpl
def add_subcommand(nornir_apps):
    """Add subcommand to nornir_apps"""

    @nornir_apps.command(name="napalm-validate")
    @click.option(
        "-s",
        "--src",
        help="file to use as validation source",
        required=True,
        type=click.Path(exists=True),
    )
    @click.option("-d", "--data", help="data to validate device's state")
    @add_common_options
    @click.pass_context
    def validate(ctx, src, data, **cli_options):
        """Validate device compliance using napalm_validate"""
        runner = ctx.obj.runner
        output = runner.run(task=napalm_validate, src=src, validation_source=data)
        if cli_options.get("output") == "text":
            ctx.obj.console_printer(output)
        return output
