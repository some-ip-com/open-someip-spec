#!/usr/bin/env python3
#
# check_drawsvg_names.py
# Verify that each drawsvg script saves its SVG under its own filename.
#
# The scripts in src/images/drawsvg/ are auto-generated. A copy/paste or
# generator slip can leave save_svg('canvas.svg') behind, which makes every
# affected script silently overwrite the same file when run directly.
#
# SPDX-License-Identifier: GPL-2.0-or-later
#

import re
import sys
from pathlib import Path

DRAW_SVG_DIR = Path(__file__).resolve().parent.parent / 'src' / 'images' / 'drawsvg'

# Matches e.g. d.save_svg('name.svg') or d.save_svg("name.svg")
SAVE_SVG_RE = re.compile(r"""save_svg\(\s*['"]([^'"]+)['"]""")


def check(directory: Path = DRAW_SVG_DIR) -> list[str]:
    problems = []

    scripts = sorted(directory.glob('*.py'))
    if not scripts:
        problems.append(f'No drawsvg scripts found in {directory}')
        return problems

    for script in scripts:
        expected = f'{script.stem}.svg'
        for lineno, line in enumerate(script.read_text(encoding='utf-8').splitlines(), 1):
            for match in SAVE_SVG_RE.finditer(line):
                found = match.group(1)
                if Path(found).name != expected:
                    problems.append(
                        f'{script}:{lineno}: save_svg({found!r}) does not match '
                        f'the script name, expected {expected!r}'
                    )

    return problems


def main() -> int:
    problems = check()

    if problems:
        print('drawsvg filename check failed:', file=sys.stderr)
        for problem in problems:
            print(f'  {problem}', file=sys.stderr)
        print(
            '\nEach script in src/images/drawsvg/ must save under its own '
            'filename, e.g. feat_req_someip_437.py -> feat_req_someip_437.svg',
            file=sys.stderr,
        )
        return 1

    print(f'drawsvg filename check passed for {len(list(DRAW_SVG_DIR.glob("*.py")))} scripts')
    return 0


if __name__ == '__main__':
    sys.exit(main())
