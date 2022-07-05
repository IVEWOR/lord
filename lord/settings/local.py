import os
from pathlib import Path

from lord.settings.base import INSTALLED_APPS

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = "django-insecure-5*5pj!v@-4g$lvia#hl&1o8^a%(@+6g8z_^*hp#_9me)adewp%"

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "localhost"
    # ...
]

INSTALLED_APPS += ["debug_toolbar"]

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static assets
STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
]

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
