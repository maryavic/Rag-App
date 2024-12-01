# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Rag_App'
copyright = '2024, Maryam Benaida'
author = 'Maryam Benaida'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

extensions = [
    "sphinx.ext.autodoc",        # Automatically document your code
    "sphinx.ext.napoleon",       # Support for NumPy/Google-style docstrings
    "sphinx.ext.viewcode",       # Link to source code in the docs
]
