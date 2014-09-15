#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Leonardo Uieda'
SITENAME = u'Geof\xedsica 1'
SITESUBTITLE = u'Geologia - Universidade do Estado do Rio de Janeiro'
SITEURL = ''
RELATIVE_URLS = True

TIMEZONE = u'America/Sao_Paulo'
DEFAULT_LANG = u'pt'

PATH = 'lessons'
ARTICLE_URL = 'lessons/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'lessons/{category}/{slug}.html'
PAGE_PATHS = ['pages']

STATIC_PATHS = ['images', 'notebooks']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
SUMMARY_MAX_LENGTH = 50

PLUGIN_PATHS = [os.path.abspath('../pelican-plugins')]
PLUGINS = ['summary',
           'better_figures_and_images',
           'html_rst_directive',
           'latex',
           ]
RESPONSIVE_IMAGES = False
FIGURE_NUMBERS = True

THEME = 'theme'

INTERNALLINKS = [
    ['Sobre', 'index.html'],
    ['Gravimetria', 'category/gravimetria.html'],
    ['Magnetometria', 'category/magnetometria.html'],
    ]
EXTERNALLINKS = []


# This goes at the footer of the site
COPYRIGHT_NOTICE = """
<a rel="license"
 href="http://creativecommons.org/licenses/by/4.0/deed.en_US"
><img alt="Creative Commons License" style="border-width:0"
 src="http://i.creativecommons.org/l/by/4.0/88x31.png"
/></a><br />
This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US"
>Creative Commons Attribution 4.0 International License</a>.
"""
