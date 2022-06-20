import importlib
import sys

import pluggy

from . import hookspecs

DEFAULT_PLUGINS = (
    "nrcli.commands.napalm_configure_cmd",
    "nrcli.commands.napalm_validate_cmd",
    "nrcli.commands.napalm_ping_cmd",
    "nrcli.commands.napalm_get_cmd",
)

plugin_manager = pluggy.PluginManager("nrcli")
plugin_manager.add_hookspecs(hookspecs)

if not hasattr(sys, "_called_from_test"):
    plugin_manager.load_setuptools_entrypoints("nrcli")

# Load default plugins
for plugin in DEFAULT_PLUGINS:
    mod = importlib.import_module(plugin)
    plugin_manager.register(mod, plugin)
