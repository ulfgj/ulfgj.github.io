import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# Production settings
SITEURL = 'https://ulfgj.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'atom.xml'
FEED_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True
