from typing import Tuple

import click
from nornir import InitNornir

from nornir_apps.console import print_result
from nornir_apps.plugins import DEFAULT_PLUGINS
from nornir_apps.plugins import plugin_manager as pm
from nornir_apps.version import __version__


class Config:
    def __init__(self):
        self.verbosity = 0
        self.logger = None
        self.debug = None


PASS_CTX = click.make_pass_decorator(Config, ensure=True)


def _parse_filter(expression: str) -> Tuple[Tuple]:
    return tuple(tuple(exp.split("=")) for exp in expression.split(","))


@click.command()
@click.option("--all", help="Include default plugins", is_flag=True)
def plugins(all):
    """List available plugins"""
    all_plugins = pm.get_plugins()
    plugin_list = [
        {
            "name": plugin.__name__,
            "hooks": [hook.name for hook in pm.get_hookcallers(plugin)],
        }
        for plugin in all_plugins
        if plugin.__name__ not in DEFAULT_PLUGINS
    ]
    if all:
        plugin_list.extend(
            [
                {
                    "name": plugin.__name__,
                    "hooks": [hook.name for hook in pm.get_hookcallers(plugin)],
                }
                for plugin in all_plugins
                if plugin.__name__ in DEFAULT_PLUGINS
            ]
        )
    print_result(plugin_list)


@click.group()
@click.option(
    "-i",
    "--init-file",
    help="nornir initialization file",
    default="config.yaml",
    type=click.Path(exists=True),
)
@click.option(
    "-h",
    "--host-filter",
    help="Nornir simple filter to select host or host groups. Ex: -f 'platform=ios'",
)
@click.version_option(version=__version__)
@PASS_CTX
def cli(ctx, init_file, host_filter):
    """Simple Nornir CLI runner"""
    runner = InitNornir(config_file=init_file)
    if host_filter:
        filter_exps = _parse_filter(host_filter)

        # if our list contains a single tuple, and we have a single value
        # we assume that to be the hostname. Otherwise, key=value pairs
        # are passed as kwargs to the filter.
        if len(filter_exps) == 1 and len(filter_exps[0]) == 1:
            runner = runner.filter(name=filter_exps[0][0])
        elif len(filter_exps) == 1 or len(filter_exps) > 1:
            runner = runner.filter(**dict(filter_exps))

    ctx.runner = runner
    ctx.console_printer = print_result


cli.add_command(plugins)
# Register sub command plugins
pm.hook.add_subcommand(nornir_apps=cli)
