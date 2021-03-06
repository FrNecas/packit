# MIT License
#
# Copyright (c) 2018-2019 Red Hat, Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest

from packit.cli.build import build
from packit.cli.create_update import create_update
from packit.cli.packit_base import packit_base
from packit.cli.packit_base import version as cli_version
from packit.cli.update import update
from tests.spellbook import call_packit


def test_base_help():
    result = call_packit(parameters=["--help"])
    assert result.exit_code == 0
    assert "Usage: packit [OPTIONS] COMMAND [ARGS]..." in result.output


def test_base_version_direct():
    # This test requires packit on pythonpath
    result = call_packit(cli_version)
    assert result.exit_code == 0


def test_base_version():
    # This test requires packit on pythonpath
    result = call_packit(parameters=["version"])
    assert result.exit_code == 0
    # TODO: figure out the correct version getter:
    # version = get_version(root="../..", relative_to=__file__)
    # name_ver = get_distribution(__name__).version
    # packit_ver = get_distribution("packit").version
    # packitos_ver = get_distribution("packitos").version
    # assert version in result.output


@pytest.mark.parametrize("cmd_function", [update, build, create_update])
def test_base_subcommand_direct(cmd_function):
    result = call_packit(cmd_function, parameters=["--help"])
    assert result.exit_code == 0


@pytest.mark.parametrize("subcommand", ["propose-update", "build", "create-update"])
def test_base_subcommand_help(subcommand):
    result = call_packit(packit_base, parameters=[subcommand, "--help"])
    assert result.exit_code == 0
    assert f"Usage: packit {subcommand} [OPTIONS]" in result.output
