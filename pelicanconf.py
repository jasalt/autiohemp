#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aution Hampputila'
SITENAME = 'Aution Hampputila'
SITEURL = ''
THEME = 'theme-nest'
NEST_HEADER_IMAGES = 'images/background.jpg'

NEST_INDEX_HEAD_TITLE = u'Homepage'
NEST_INDEX_HEADER_TITLE = u'Aution Hampputila'
NEST_INDEX_HEADER_SUBTITLE = u'Kotimaista superfoodia suoraan tuottajalta'

DISPLAY_PAGES_ON_MENU = ('kaytto.md')
DISPLAY_CATEGORIES_ON_MENU = False

PATH = 'content'

TIMEZONE = 'Europe/Helsinki'
DEFAULT_LANG = 'fi'
LOCALE = 'fi_FI'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
NEST_LINKS_COLUMN_TITLE = u'Linkit'
LINKS = (('Tommin kotisivu', 'http://tommi.saltio.la'),
         ('Sivuston toteutti Saltiola Code', 'http://saltio.la'),
         )

NEST_HEADER_IMAGES = "background.jpg"

GUIDES_CATEGORY_SUBTITLE = "Miten käyttää hampunsiemeniä?"
# TODO add different categories CATEGORY_SUBTITLES {''}

# Social widget
NEST_SOCIAL_COLUMN_TITLE = u'Yhteystiedot'
SOCIAL = (
    ('Puh. +358407479512', 'tel:+358407479512'),
    ('info@autiohemp.com', 'mailto:info@autiohemp.com'),
    ('Aution Hampputila Facebookissa', 'https://www.facebook.com/Aution-Hampputila-880717715368664/'),
    ('@autiohemp Twitterissä', 'https://twitter.com/autiohemp'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static files
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico',
                'extra/logo.svg', 'extra/CNAME', 'documents']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/logo.svg': {'path': 'logo.svg'}
}
