import os
import sys
import datetime
import subprocess
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from typing import TYPE_CHECKING
from pathlib import Path

base_path = Path(__file__).parents[1].as_posix()
sys.path.append(base_path)
from src.scripts.bitfield import BitfieldDirective
from src.scripts.drawSVG import DrawSvgDirective

extensions = [
    "sphinx_needs",
    "sphinxcontrib.plantuml",
    "sphinx_simplepdf",
]

project = "Open SOME/IP Specification"
copyright = "SOME/IP"
author = "SOME/IP authors"
version = "25-12"

needs_id_regex = "^[A-Za-z0-9_]"
needs_title_from_content = False
# We want to generate a JSON file
needs_build_json = True

# We do not want to use the title for the needs:
needs_title_optional = True

# The rendering of refernces to needs shall only show the need_id:
needs_role_need_template = "{id}"

needs_types = [
    {
        "directive": "requirement",
        "title": "Requirement",
        "prefix": "RE_",
        "color": "#BFD8D2",
        "style": "node",
    },
    {
        "directive": "information",
        "title": "Information",
        "prefix": "INFO_",
        "color": "#BFD8D2",
        "style": "node",
    },
    {
        "directive": "story",
        "title": "User Story",
        "prefix": "US_",
        "color": "#BFD8D2",
        "style": "node",
    },
    {
        "directive": "spec",
        "title": "Specification",
        "prefix": "SP_",
        "color": "#FEDCD2",
        "style": "node",
    },
    {
        "directive": "impl",
        "title": "Implementation",
        "prefix": "IM_",
        "color": "#DF744A",
        "style": "node",
    },
    {
        "directive": "test",
        "title": "Test Case",
        "prefix": "TC_",
        "color": "#DCB239",
        "style": "node",
    },
    {
        "directive": "heading",
        "title": "Heading",
        "prefix": "HEAD_",
        "color": "#DCB239",
        "style": "title"
    },
    {
        "directive": "feat_req",
        "title": "feat_req",
        "prefix": "feat_req_",
        "color": "#BFD8D2",
        "style": "node"
    },
]

needs_import_keys = {"key": "needs_test.json"}

needs_json_remove_defaults = True


needs_extra_options = [
    {
        "name": "reqtype",
        "description": "type",
        "schema": {
            "type": "string",
            "enum": ["Information", "Requirement",]
        },
    },
    {
        "name": "security",
        "description": "security relevant",
        "schema": {
            "type": "string",
            "enum": ["TBD", "NO", "YES"]
        },
    },
    {
        "name": "safety",
        "description": "safety level",
        "schema": {
            "type": "string",
            "enum": ["TBD", "QM", "ASIL-A", "ASIL-B", "ASIL-C", "ASIL-D"]
        },
    },
    {
        "name": "h",
        "description": "heading level",
        "schema": {
            "type": "integer",
            "minimum": 1,
            "maximum": 6,
        },
    },
]

needs_extra_links = [
    {
        "option": "heading",
        "incoming": "spans_entries",
        "outgoing": "heading",
        "copy": False,
        "color": "#00AA00"
    },
    {
        "option": "satisfies",
        "incoming": "satisfied by",
        "outgoing": "satisfies",
        "copy": False,
        "color": "#00AA00"
    }
]

# We could the settings manually in the files, but here it is global set for all.
# We do want to seperate the authoring from the rendering.
needs_global_options = {
   "hide": {
      "predicates": [
         ("type == 'heading'", True),
      ]
   },
   "collapse": {
      "predicates": [
         ("type == 'feat_req'", True),
      ]
   },
   "template": {
      "predicates": [
         ("type == 'feat_req'", "feat_req_template"),
      ]
   },
   "heading": {
      "predicates": [
         (
            "type == 'heading'",
            "[[copy('id', filter='\"heading\" == type and current_need[\"id\"] != id and current_need[\"sections\"][:-1] == sections and current_need[\"docname\"] == docname and current_need[\"doctype\"] == doctype')]]"
         ),
      ],
      "default": "[[copy('id', filter='\"heading\" == type and current_need[\"sections\"] == sections and current_need[\"docname\"] == docname and current_need[\"doctype\"] == doctype')]]"
   },
   "title": {
      "predicates": [
         (
            "type == 'heading'",
            "[[copy('section_name')]]"
         ),
      ]
   },
   "h": {
      "predicates": [
         (
            "type == 'heading'",
            "[[sections_level()]]"
         ),
      ]
   },
}

# enable to set title in globals:
import sphinx_needs.data as sphinx_needs_data
sphinx_needs_data.NeedsCoreFields["title"]["allow_default"] = True

def sections_level(app, need, needs, *args, **kwargs):
    len_sections: int = len(need["sections"])
    return len_sections

needs_css = 'blank.css'

html_static_path = ['_static']
html_css_files = [
    'css/custom.css'
]

simplepdf_file_name = 'open_someip_specification.pdf'
simplepdf_vars = {
    'primary': '#0b72b5',
    'secondary': '#000000',
    'cover': '#ffffff',
    'white': '#ffffff',
    'links': '#0b72b5',
    'cover-bg': '',
    'cover-overlay': 'rgba(0, 132, 255, 1.0)',
    'top-left-content': 'counter(page)',
    'bottom-center-content': f'"Build: {datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day} - {version}"',
    'bottom-right-content': 'counter(page)',
}

exclude_patterns = ['tables/*.rst']

plantuml_output_format = "svg"
plantuml_latex_output_format = "svg"

jar_path=Path(Path(__file__).parents[1].as_posix(),'tools','plantuml.jar')
plantuml = f'java -jar {jar_path}'

from sphinx_needs.api import add_dynamic_function

def setup(app: Sphinx, *args, **kwargs):
    app.add_directive('bitfield_directive', BitfieldDirective)
    app.add_directive('drawsvg_directive', DrawSvgDirective)
    app.add_css_file('./css/custom.css')
    add_dynamic_function(app, sections_level)
