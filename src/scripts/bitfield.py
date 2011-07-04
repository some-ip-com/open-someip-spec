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
import json
from bit_field import render, jsonml_stringify


def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))


class BitfieldDirective(SphinxDirective):
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

            with open(visualization_path) as json_data:
                json_payload = json.load(json_data)
                json_data.close()

            jsonml = render(json_payload['payload'], **json_payload['config'])
            html = jsonml_stringify(jsonml)

            node = nodes.raw('', html, format='html')
            return [node]
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise
