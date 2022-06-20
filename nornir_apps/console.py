import json

from nornir.core.task import AggregatedResult, MultiResult, Result
from rich.console import Console
from rich.theme import Theme
from rich.traceback import install

# Install rich traceback as default traceback handler
install(show_locals=True, max_frames=10)


console_theme = Theme({"info": "cyan", "warning": "magenta", "danger": "bold red"})
console = Console(theme=console_theme)


def _dump_result(result: Result):
    return {
        result.host.name: {
            "json": result.result,
            "stdout": getattr(result, "stdout") or json.dumps(result.result),
            "failed": result.failed,
        }
    }


def print_result(result: Result) -> None:
    """Print to console"""
    output = {}
    if isinstance(result, AggregatedResult):
        for _, data in sorted(result.items()):
            output |= _dump_result(data)  # update output dict via union op
    elif isinstance(result, MultiResult):
        output = _dump_result(result)
    else:
        output = result
    console.print_json(data=output)
