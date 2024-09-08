from .base import *

DEBUG = False
ALLOWED_HOSTS = ['domain.com']
CSRF_TRUSTED_ORIGINS = ['https://domain.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

