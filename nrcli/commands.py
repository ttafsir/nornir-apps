import click
from nornir.core.task import Task
from nornir_napalm.plugins.tasks import (
    napalm_configure,
    napalm_get,
    napalm_ping,
    napalm_validate,
)

from .commands.common import common_options


@click.command(name="napalm-validate")
@click.option(
    "-s",
    "--src",
    help="file to use as validation source",
    required=True,
    type=click.Path(exists=True),
)
@click.option("-d", "--data", help="data to validate device's state")
@click.pass_context
def validate(ctx, src, data, task: Task = napalm_validate, **cli_options):
    """Validate device compliance using napalm_validate"""
    runner = ctx.obj.runner
    output = runner.run(task=task, src=src, validation_source=data)
    if cli_options.get("output") == "text":
        ctx.obj.console_printer(output)
    return output


@click.command(name="napalm-get")
@click.option(
    "-g",
    "--getters",
    help="list of getters to use",
    multiple=True,
    default=["facts"],
)
@common_options
@click.pass_context
def get_config(ctx, getters, task: Task = napalm_get, **cli_options):
    """Retrieve device configuration using napalm getters"""
    runner = ctx.obj.runner
    output = runner.run(task=task, getters=getters)
    if cli_options.get("output") == "text":
        ctx.obj.console_printer(output)
    return output


@click.command(name="napalm-configure")
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
@common_options
@click.pass_context
def set_config(
    ctx, dry_run, replace, commit_message, task: Task = napalm_configure, **cli_options
):
    """Retrieve device configuration"""
    runner = ctx.obj.runner
    output = runner.run(
        task=task, dry_run=dry_run, replace=replace, commit_message=commit_message
    )
    if cli_options.get("output") == "text":
        ctx.obj.console_printer(output)
    return output


@click.command(name="napalm-ping")
@click.option(
    "-d", "--dest", help="Host or IP Address of the destination", required=True
)
@click.option("-s", "--source", help="Source address of echo request")
@click.option("--ttl", default=255, help="Max number of hops")
@click.option(
    "-t", "--timeout", default=2, help="Max seconds to wait after sending final packet"
)
@click.option("-z", "--size", default=100, help="Size of request in bytes")
@click.option("-c", "--count", default=5, help="Number of ping request to send")
@click.option("--vrf", help="Name of vrf")
@common_options
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
    task: Task = napalm_ping,
    **cli_options,
):
    """Ping device"""
    runner = ctx.obj.runner
    output = runner.run(
        task=task,
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
