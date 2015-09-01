"""
WSGI config for freefood project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freefood.settings")

application = get_wsgi_application()

#this is after I made changes to satisfy heroku
from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(application)
