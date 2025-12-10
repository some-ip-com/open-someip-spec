#!/bin/bash

# setup.sh
# Setup environment script for Linux, macOS, etc.
#
# Copyright 2025 Dr. Lars Völker
#
# SPDX-License-Identifier: GPL-2.0-or-later
#

# deactivate, if in venv
deactivate 2>/dev/null

# create virtual environment
python -m venv .venv

# activate virtual environment
source .venv/bin/activate

# update pip packages
pip install pip -U

# install requirements
pip install -r ./requirements.txt


### WORKAROUND
# lets clone sphinx-simplepdf until there is a new release
# we are cloning a local fork to ensure full control
git clone https://github.com/some-ip-com/sphinx-simplepdf.git

# install sphinx-simplepdf local version
pip install -e sphinx-simplepdf
