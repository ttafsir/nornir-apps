import importlib
import sys

import pluggy

from . import hookspecs

DEFAULT_PLUGINS = (
    "nornir_apps.commands.napalm_configure_cmd",
    "nornir_apps.commands.napalm_validate_cmd",
    "nornir_apps.commands.napalm_ping_cmd",
    "nornir_apps.commands.napalm_get_cmd",
)

plugin_manager = pluggy.PluginManager("nornir_apps")
plugin_manager.add_hookspecs(hookspecs)

if not hasattr(sys, "_called_from_test"):
    plugin_manager.load_setuptools_entrypoints("nornir_apps")

# Load default plugins
for plugin in DEFAULT_PLUGINS:
    mod = importlib.import_module(plugin)
    plugin_manager.register(mod, plugin)
