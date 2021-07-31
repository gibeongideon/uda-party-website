from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q1bz++yt+2!lb%!ds+ju+s&%3e2o1dr8dras25(#7$-og&3(d^'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

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

PAYPAL_RECEIVER_EMAIL ="darius@daruspin.com"

PAYPAL_TEST = True


###USA/CANADA&UKssss

PAYPAL_WPP_USER ="sb-h2ded6675419_api1.business.example.com"

PAYPAL_WPP_PASSWORD = "DFXXXTJPDKBFA5KG"

PAYPAL_WPP_SIGNATURE = "AM1aGgn2bz5QbLwfJWgM8rQPCVdfAjz3hKc8w9Pa8XdIFnHt-9r143O2"


# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://localhost:8000/'

