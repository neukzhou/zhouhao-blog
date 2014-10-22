#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'ZhouHao'
SITENAME = '一个博客'
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    ('Liupy525\'s Blog', 'www.liupeiyang.com'),
    ('静雨流风', 'http://jiayidong.com'),
    ('lizherui的程序世界', 'http://www.lizherui.com/'),
    )

# Social widget

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme'
BOOTSTRAP_THEME = 'cosmo'


USE_FOLDER_AS_CATEGORY = True

STATIC_PATHS = ['static/img','static/extra',]

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'





DUOSHUO_SITENAME = "neuk"


PLUGIN_PATH = 'plugins'
PLUGINS = ["sitemap", "summary", "neighbors","render_math",]

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}