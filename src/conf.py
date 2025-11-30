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
version = "16-06"

needs_id_regex = "^[A-Za-z0-9_]"
needs_title_from_content = False
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

needs_extra_options = ["level","reqtype","security","safety","satisfies"]

needs_extra_links = [
    {
        "option": "heading",
        "incoming": "spans_entries",
        "outgoing": "heading",
        "copy": False,
        "color": "#00AA00"
    }
]

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

def setup(app: Sphinx, *args, **kwargs):
    app.add_directive('bitfield_directive', BitfieldDirective)
    app.add_directive('drawsvg_directive', DrawSvgDirective)
    app.add_css_file('./css/custom.css')
