import os
from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['https://medicsearch.herokuapp.com/']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,  'db.sqlite3'),
    }
}