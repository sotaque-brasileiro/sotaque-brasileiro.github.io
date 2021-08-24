from os import getenv

from .base import *

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
    "http://localhost:8081",
    "http://127.0.0.1:8081",
]
