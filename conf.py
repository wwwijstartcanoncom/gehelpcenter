# Configuration file for the Sphinx documentation builder.
 
import os
import sys
 
# -- Path setup --------------------------------------------------------------
 
# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))
# sys.path.insert(0, os.path.abspath('.'))
 
# -- Project information -----------------------------------------------------
 
project = 'Garmin Express Setup Guide'
copyright = '2025, Garmin'
author = 'Garmin'
 
# The full version, including alpha/beta/rc tags
release = '1.0.0'
 
# -- General configuration ---------------------------------------------------
 
extensions = []
 
templates_path = ['_templates']
 
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
 
# -- Options for HTML output -------------------------------------------------
 
# Title shown in the browser tab and top of HTML pages
html_title = "Garmin Express – Install & Use Guide"
 
# Optional short title (e.g., for nav bar)
html_short_title = "Garmin Express Setup"
 
# Favicon (make sure favicon.ico exists in your project root or _static)
html_favicon = 'favicon.ico'
 
# Choose a theme
# html_theme = 'sphinx_rtd_theme'  # Uncomment to use the Read the Docs theme
# html_theme = 'alabaster'         # Or use default Sphinx theme
 
# Hide "View page source"
html_show_sourcelink = False
 
# Allow raw HTML blocks in .rst files (if using .. raw:: html)
html_allow_unsafe = True
 
# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}
 
# Paths that contain custom static files (e.g., style sheets, images)
# html_static_path = ['_static']  # Uncomment and add assets if needed
 
# Add any paths that contain templates here, relative to this directory
 
