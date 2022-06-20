# -*- coding: utf-8 -*-
from pluggy import HookimplMarker, HookspecMarker

hookspec = HookspecMarker("nrcli")
hookimpl = HookimplMarker("nrcli")


@hookspec
def add_subcommand(nrcli):
    """Subcommands for NRCLI command"""
