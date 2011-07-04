# setup.ps1
# Setup environment script for Windows
#
# Copyright 2025 Andreas Wambold
#
# SPDX-License-Identifier: GPL-2.0-or-later
#

# create virtual environment
python -m venv .venv

# activate virtual environment
& ".\.venv\Scripts\Activate.ps1"

# update pip packages
pip install --upgrade pip

# install requirements
pip install -r ./requirements.txt
