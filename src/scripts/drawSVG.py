# bitfield.py
#
# SPDX-License-Identifier: GPL-2.0-or-later
#

import os
import subprocess
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from typing import TYPE_CHECKING
from sphinx.environment import BuildEnvironment
from sphinx_needs.data import NeedsInfoType, SphinxNeedsData
from pathlib import Path
import drawsvg
import importlib.util


def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))


class DrawSvgDirective(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'alt': directives.unchanged,
                   'height': directives.nonnegative_int,
                   'width': directives.nonnegative_int,
                   'scale': directives.nonnegative_int,
                   'align': align,
                   }
    has_content = False

    def run(self):
        base_path = Path(__file__).parent.parent.resolve()

        try:
            reference = self.arguments[0]
            visualization_path = Path(base_path, reference).as_posix()
            assert os.path.exists(
                visualization_path), f'Provided visualization does not exist {reference}'

            ret = load_and_run_function(visualization_path, 'build_drawing')
            html = ret.as_svg()

            node = nodes.raw('', html, format='html')
            return [node]
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise


def load_and_run_function(python_file_path, function_name):
    python_file_path = Path(python_file_path).resolve()
    module_name = python_file_path.stem

    spec = importlib.util.spec_from_file_location(
        module_name, str(python_file_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    func = getattr(module, function_name)
    return func()  # no arguments
