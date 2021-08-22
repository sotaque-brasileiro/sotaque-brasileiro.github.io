import requests
from django.conf import settings
from django.http import HttpResponse


def validate_recaptcha_token(token):
    """
    Validates the recaptcha token.
    """
    url = "https://www.google.com/recaptcha/api/siteverify"
    data = {"secret": settings.RECAPTCHA_SECRET_KEY, "response": token}
    response = requests.post(url, data=data)
    return response.json()
