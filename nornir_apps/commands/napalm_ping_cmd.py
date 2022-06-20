import click
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_apps.commands.common import add_common_options
from nornir_apps.hookspecs import hookimpl


@hookimpl
def add_subcommand(nornir_apps):
    """Add subcommand to nornir_apps"""

    @nornir_apps.command(name="napalm-ping")
    @click.option(
        "-d", "--dest", help="Host or IP Address of the destination", required=True
    )
    @click.option("-s", "--source", help="Source address of echo request")
    @click.option("--ttl", default=255, help="Max number of hops")
    @click.option(
        "-t",
        "--timeout",
        default=2,
        help="Max seconds to wait after sending final packet",
    )
    @click.option("-z", "--size", default=100, help="Size of request in bytes")
    @click.option("-c", "--count", default=5, help="Number of ping request to send")
    @click.option("--vrf", help="Name of vrf")
    @add_common_options
    @click.pass_context
    def ping(
        ctx,
        dest,
        source,
        ttl,
        timeout,
        size,
        count,
        vrf,
        **cli_options,
    ):
        """Ping device"""
        runner = ctx.obj.runner
        output = runner.run(
            task=napalm_ping,
            dest=dest,
            source=source or "",
            ttl=ttl,
            timeout=timeout,
            size=size,
            count=count,
            vrf=vrf,
        )
        if cli_options.get("output") == "text":
            ctx.obj.console_printer(output)
        return output
