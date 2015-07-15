"""
Django settings for pytutorial project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(__file__)
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates")

BASE_ROOT = os.path.abspath(os.path.join(os.path.split(__file__)[0], '..'))
STATIC_ROOT = os.path.join(BASE_ROOT, 'stream_twitter/static/')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*m&(&5!c^7j^7s$33u(bt567k!q0)@&p1io_w($ec+g66zr!0@'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.environ.get("DEBUG", "on") == "on"
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, "fixtures")
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'stream_twitter',
    'stream_django',
    'pytutorial',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

ROOT_URLCONF = 'pytutorial.urls'

WSGI_APPLICATION = 'pytutorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {'default': dj_database_url.config()}

if not DATABASES.get('default'):
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

STREAM_NEWS_FEEDS = dict(flat='flat')

LOGIN_URL = '/registration/login'
USE_AUTH = bool(os.environ.get('USE_AUTH'))
#USE_AUTH = True
#ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False
#ACCOUNT_AUTHENTICATION_METHOD = "username"
#ACCOUNT_EMAIL_VERIFICATION = "none"
SITE_ID = int(os.environ.get('SITE_ID', 1))
#LOGIN_REDIRECT_URL = '/tweet'
#LOGOUT_REDIRECT_URL = '/'
#ACCOUNT_LOGOUT_ON_GET = True
#ACCOUNT_EMAIL_REQUIRED = False
#SOCIALACCOUNT_EMAIL_REQUIRED = False
#SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
#ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

DEMO_USERNAME = 'marymeakin'
DEMO_PASSWORD = '1234'

AUTH_PROFILE_MODULE = 'stream_twitter.UserProfile'

# add your api keys from https://getstream.io/dashboard/
# you do not need this if you are running on Heroku
# and using getstream add-on
STREAM_API_KEY = '7ywyvxkwaebz'
STREAM_API_SECRET = 'qc8usapch36tmpk7cfap6j63aud343m2e5ffnbzzsj74spqsadtzsqkjz7maj4t9'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

ROLLBAR_ACCESS_TOKEN = os.environ.get('ROLLBAR_ACCESS_TOKEN')

if ROLLBAR_ACCESS_TOKEN is not None:
    MIDDLEWARE_CLASSES += ('rollbar.contrib.django.middleware.RollbarNotifierMiddleware',)
    ROLLBAR = {
        'access_token': ROLLBAR_ACCESS_TOKEN,
        'environment': 'development' if DEBUG else 'production',
        'branch': 'master',
        'root': BASE_DIR,
    }
