import os
from distutils import dir_util
from pathlib import Path

import pytest
from click.testing import CliRunner, Result
from nrcli.cli import cli

CONFIG = """
---
core:
  raise_on_error: False

runner:
  plugin: threaded
  options:
    num_workers: 100

logging:
  enabled: True

inventory:
  plugin: SimpleInventory
  options:
    host_file: "examples/inventory/hosts.yaml"
    group_file: "examples/inventory/groups.yaml"
"""


def _run_cli_command(commands: list) -> Result:
    """Helper function to Run CLI command."""
    runner: CliRunner = CliRunner()
    return runner.invoke(cli, commands)


@pytest.fixture(scope="module")
def run_cli_command(datadir):
    """returns a Helpers object as a fixture."""
    os.chdir(datadir)
    return _run_cli_command


@pytest.fixture(scope="module")
def datadir(tmp_path_factory, request):
    """
    Search a folder with the same name of test module and, if available,
    copy all contents to a temporary directory for test data.
    """
    filename = request.module.__file__
    test_dir = Path(filename).parent / "data" / Path(filename).stem
    temp_path = tmp_path_factory.mktemp(test_dir.stem)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, str(temp_path))

    return temp_path
