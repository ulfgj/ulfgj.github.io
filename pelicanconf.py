import datetime

AUTHOR = 'ulf gjerdingen'
SITENAME = 'ulf.gjerdingen'
TAGLINE = '...'
SITEDESCRIPTION = "c'est le moi..."
SITEURL = ""
CURRENT_YEAR = datetime.date.today().year

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

TIMEZONE = 'Europe/Stockholm'
DEFAULT_LANG = 'en'

# URL Settings to match Jekyll 1:1
ARTICLE_URL = '{date:%Y-%m-%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y-%m-%d}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

# Disable unused archives
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

# Pagination
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page{number}/', '{base_name}/page{number}/index.html'),
)

# Derive slug and date from filename when available
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

# Feeds (disabled for local dev)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None

# Theme
THEME = 'themes/lanyon'

# Direct Templates
DIRECT_TEMPLATES = ['index', '404']
PAGINATED_TEMPLATES = {'index': None}

# Static Files
STATIC_PATHS = ['images', 'public', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['external_links']

# Markdown Configuration
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Social Links (from Jekyll _data/social.yml)
SOCIAL = [
    {
        'name': 'facebook',
        'url': 'http://www.facebook.com/ulf.gj',
        'image': '/images/facebook.png',
        'image_white': 'images/facebook_white.png',
        'row': 1,
    },
    {
        'name': 'twitter',
        'url': 'http://twitter.com/ulfgj',
        'image': '/images/twitter.png',
        'image_white': 'images/twitter_white.png',
        'row': 1,
    },
    {
        'name': 'github',
        'url': 'http://github.com/ulfgj',
        'image': '/images/github.png',
        'image_white': 'images/github_white.png',
        'row': 1,
    },
    {
        'name': 'linkedIn',
        'url': 'https://www.linkedin.com/in/ulf-gjerdingen-8a6b5189',
        'image': '/images/linkedin.png',
        'image_white': 'images/linkedin_white.png',
        'row': 1,
    },
    {
        'name': 'youtube',
        'url': 'http://www.youtube.com/user/ulfgj',
        'image': '/images/youtube.png',
        'image_white': 'images/youtube_white.png',
        'row': 2,
    },
    {
        'name': 'deviantart',
        'url': 'http://ulfdotgj.deviantart.com/',
        'image': '/images/deviantart.png',
        'image_white': 'images/deviantart_white.png',
        'row': 2,
    },
    {
        'name': 'pinterest',
        'url': 'http://www.pinterest.com/ugjerdingen/',
        'image': '/images/pinterest.png',
        'image_white': 'images/pinterest_white.png',
        'row': 2,
    },
    {
        'name': 'rss',
        'url': '/atom.xml',
        'image': '/images/rss.png',
        'image_white': 'images/rss_white.png',
        'row': 2,
    },
    {
        'name': 'spotify',
        'url': 'https://open.spotify.com/artist/4NlQ3LwcyZpB9UQAlKUI4a',
        'image': '/images/spotify.png',
        'image_white': 'images/spotify_white.png',
        'row': 3,
    },
]
