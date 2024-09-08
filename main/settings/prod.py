from .base import *

DEBUG = False
ALLOWED_HOSTS = ['agro-connect.shop']
CSRF_TRUSTED_ORIGINS = ['https://agro-connect.shop']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

