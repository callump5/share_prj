from base import *
from aws_login import *
AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}