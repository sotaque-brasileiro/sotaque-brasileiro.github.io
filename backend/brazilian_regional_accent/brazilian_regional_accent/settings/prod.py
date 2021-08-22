from os import getenv

from .base import *

RECAPTCHA_SITE_KEY = getenv("RECAPTCHA_SITE_KEY")
RECAPTCHA_SECRET_KEY = getenv("RECAPTCHA_SECRET_KEY")
SECRET_KEY = getenv("SECRET_KEY")

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",
    "http://127.0.0.1:8081",
]
