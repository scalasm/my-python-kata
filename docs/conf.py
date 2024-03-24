"""Sphinx configuration."""

project = "My Python Kata"
author = "Mario Scalas"
copyright = "2022, Mario Scalas"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
