# -*- coding: utf-8 -*-
from pluggy import HookimplMarker, HookspecMarker

hookspec = HookspecMarker("nornir_apps")
hookimpl = HookimplMarker("nornir_apps")


@hookspec
def add_subcommand(nornir_apps):
    """Subcommands for nornir_apps command"""
