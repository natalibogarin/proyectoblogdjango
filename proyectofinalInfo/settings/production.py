# production.py
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['myportfolio.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = 'https://myportfolio.com/static/'
MEDIA_URL = 'https://myportfolio.com/media/'