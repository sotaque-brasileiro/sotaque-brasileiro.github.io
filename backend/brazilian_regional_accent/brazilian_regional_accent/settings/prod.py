from os import getenv

from .base import *

DEBUG = False

# ReCaptcha
RECAPTCHA_SITE_KEY = getenv("RECAPTCHA_SITE_KEY")
RECAPTCHA_SECRET_KEY = getenv("RECAPTCHA_SECRET_KEY")
SECRET_KEY = getenv("SECRET_KEY")

# Google Cloud credentials
GCS_BUCKET_NAME = getenv("GCS_BUCKET_NAME")
GOOGLE_CLOUD_CREDENTIALS = getenv("GOOGLE_CLOUD_CREDENTIALS")

CORS_ALLOWED_ORIGINS = [
    "https://sotaque.gabriel-milan.com",
    "https://sotaque-brasileiro.github.io",
]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": getenv("DB_NAME"),
        "USER": getenv("DB_USER"),
        "PASSWORD": getenv("DB_PASSWORD"),
        "HOST": getenv("DB_HOST"),
        "PORT": getenv("DB_PORT"),
    }
}
