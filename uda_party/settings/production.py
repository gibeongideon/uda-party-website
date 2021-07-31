from .base import *

DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q1bz++yt+2!lb%!ds+ju+s&%3e2o1dr8dras25(#7$-og&3(d^'

try:
    from .local import *
except ImportError:
    pass

ALLOWED_HOSTS = ['*'] 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": config("DB_NAME", default="darius_dev"),
#         "USER": config("DB_USER", default="darius"),
#         "PASSWORD": config("DB_PASSWORD", default="darius!passcode"),
#         "HOST": "localhost",
#         "PORT": "",
#     }
# }




# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash

BASE_URL = 'http://uda-party.ga'


