# build.ps1
# Build script for Windows
#
# Copyright 2025 Andreas Wambold
#
# SPDX-License-Identifier: GPL-2.0-or-later
#

$SPHINXBUILD = "sphinx-build"
$SOURCEDIR = "src"
$BUILDDIR = "$SOURCEDIR/_build"
$FIGURESDIR = "$SOURCEDIR/figures"
$PUMLSRCDIR = "$SOURCEDIR/plantuml"

function Help {
    & $SPHINXBUILD -M help $SOURCEDIR $BUILDDIR
}

function Html {
    & $SPHINXBUILD -M html $SOURCEDIR $BUILDDIR
    Write-Host "Build finished. The HTML pages are in $BUILDDIR/html."
}

function Pdf {
    & $SPHINXBUILD -M simplepdf $SOURCEDIR $BUILDDIR
    Write-Host "Build finished. The PDF is in $BUILDDIR/pdf."
}

if ($args.Count -gt 0) {
    Invoke-Expression $args[0]
}
