import click

OUT_CHOICES = ("text", "yaml", "json")
COMMON_OPTIONS = [
    click.option("-o", "--output", default="text", type=click.Choice(OUT_CHOICES)),
]


def add_common_options(subcommand):
    """Setter options for CLI"""
    for decorator in reversed(COMMON_OPTIONS):
        subcommand = decorator(subcommand)
    return subcommand
