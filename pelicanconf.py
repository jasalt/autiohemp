#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aution Hampputila'
SITENAME = 'Aution Hampputila'
SITEURL = ''
THEME = 'theme-nest'
NEST_HEADER_IMAGES = 'images/background.jpg'

NEST_INDEX_HEAD_TITLE = u'Homepage'
NEST_INDEX_HEADER_TITLE = u'My Awesome Blog'
NEST_INDEX_HEADER_SUBTITLE = u'Smashing The Stack For Fun And Profit'

PATH = 'content'

TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = 'fi'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static files
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/logo.svg': {'path': 'logo.svg'}
}
