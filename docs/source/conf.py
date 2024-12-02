# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os 

project = 'study note'
copyright = '2024, Shaofeng'
author = 'Shaofeng'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# -- ReadTheDoc requirements and local template generation---------------------
# code borrowed from https://github.com/mysecureshell/mysecureshell/blob/master/doc/source/conf.py

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    # overrides the default css file to get a larger width
    # borrowed from https://blog.deimos.fr/2014/10/02/sphinxdoc-and-readthedocs-theme-tricks-2/ & https://cloud.tencent.com/developer/ask/sof/110614
    def setup(app):
        app.add_css_file('theme_overrides.css')
else:
    html_theme = 'sphinx_rtd_theme'