# Django settings for seahub project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

db_selected = '@DB_SELECTED@'
if db_selected == 'mysql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME' : 'seahub-meta',
            'USER' : 'root',
            'PASSWORD': '@ROOT_PASSWD@',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME' : os.path.join(os.path.dirname(__file__), 'seahub.db'),
        }
    }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-CN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

ADMIN_MEDIA_PREFIX = '%sadmin/' %(MEDIA_URL)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'n*v0=jz-1rz@(4gx^tf%6^e7c&um@2)g-l=3_)t@19a69n1nv6'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'seahub.base.middleware.UseridMiddleware',
)

SITE_ROOT_URLCONF = 'seahub.urls'
ROOT_URLCONF = 'djblets.util.rooturl'
 
SITE_ROOT = '/'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'djblets.util.context_processors.siteRoot',
    'django.core.context_processors.request',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'registration',
#    'avatar',
    'seahub.base',
    'seahub.profile',
#    'seahub.contacts',
#    'seahub.group',
#    'seahub.share',
)

AUTHENTICATION_BACKENDS = (
    'seahub.base.accounts.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)

ACCOUNT_ACTIVATION_DAYS = 7

REGISTRATION_SEND_MAIL = True

try:
    import local_settings
except ImportError:
    pass
else:
  # Import any symbols that begin with A-Z. Append to lists any symbols that
  # begin with "EXTRA_".
    import re
    for attr in dir(local_settings):
        match = re.search('^EXTRA_(\w+)', attr)
        if match:
            name = match.group(1)
            value = getattr(local_settings, attr)
            try:
                globals()[name] += value
            except KeyError:
                globals()[name] = value
        elif re.search('^[A-Z]', attr):
            globals()[attr] = getattr(local_settings, attr)

#avatar
#AVATAR_STORAGE_DIR = 'avatars'

#AVATAR_GRAVATAR_BACKUP = False
#AVATAR_DEFAULT_URL = MEDIA_URL + '/avatars/default.png'

LOGIN_URL = SITE_ROOT + 'accounts/login'

# profile
AUTH_PROFILE_MODULE = "profile.UserProfile"

# This must be set to empty string when serving as the root url
FORCE_SCRIPT_NAME = ''