from os import getenv

from .base import *

DEBUG = False

# ReCaptcha
RECAPTCHA_SITE_KEY = getenv("RECAPTCHA_SITE_KEY")
RECAPTCHA_SECRET_KEY = getenv("RECAPTCHA_SECRET_KEY")
SECRET_KEY = getenv("SECRET_KEY")

# MinIO
MINIO_ENDPOINT = getenv("MINIO_ENDPOINT")
MINIO_ACCESS_KEY = getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = getenv("MINIO_SECRET_KEY")
MINIO_BUCKET_NAME = getenv("MINIO_BUCKET_NAME")

CORS_ALLOWED_ORIGINS = [
    "https://sotaque.gabriel-milan.com",
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
