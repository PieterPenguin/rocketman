import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False
SECRET_KEY = '7206kr526#233!&v4ntmnqht(b0+@pgf(_dc-)s%^x9keh05e0'  # @todo get a key from here https://miniwebtool.com/django-secret-key-generator/
ALLOWED_HOSTS = ['localhost', 'yourwebsite.com', '*']  # @todo add your website url in here
cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": 'PorfolioDaTabase',
        "USER": 'Pieter',
        "PASSWORD": 'xfHjB^F2p9s*zhqFT6cNx2',
        "HOST": 'localhost',
        "PORT": "",
    }
}


sentry_sdk.init(
    dsn="https://df3b7643493b46dd827c95d29e377c31@o4504093238886400.ingest.sentry.io/4504093242097664",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
try:
    from .local import *
except ImportError:
    pass
