#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Antennenkind'
SITENAME = 'Gate Status'
SITEURL = 'http://gatestatus.der-beweis.de'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

THEME = 'themes/pelican-mockingbird'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
        ('FreifunkMainz', 'https://twitter.com/freifunkmainz'),
        ('FreifunkWi', 'https://twitter.com/freifunkwi'),
        ('GitHub', 'https://github.com/Freifunk-Mainz')
    )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
