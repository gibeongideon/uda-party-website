from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME", default="darius_db"),
        "USER": config("DB_USER", default="daru"),
        "PASSWORD": config("DB_PASSWORD", default="password"),
        "HOST": "localhost",
        "PORT": "",
    }
}


# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://uda.co.vu'

