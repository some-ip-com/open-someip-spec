# Minimal makefile for Sphinx documentation
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = src
BUILDDIR      = $(SOURCEDIR)/_build

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

pdf: 
	@$(SPHINXBUILD) -M simplepdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
	@echo "Build finished. The PDF is in $(BUILDDIR)/simplepdf."

clean:
	rm -r $(BUILDDIR)
	rm -r $(SOURCEDIR)/images/drawsvg/__pycache__/
	rm -r $(SOURCEDIR)/scripts/__pycache__/
