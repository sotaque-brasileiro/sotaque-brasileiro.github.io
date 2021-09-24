import os
import json
import base64

import requests
from django.conf import settings
from django.http import HttpResponse
from google.oauth2 import service_account
from google.cloud import storage


def validate_recaptcha_token(token):
    """
    Validates the recaptcha token.
    """
    url = "https://www.google.com/recaptcha/api/siteverify"
    data = {"secret": settings.RECAPTCHA_SECRET_KEY, "response": token}
    response = requests.post(url, data=data)
    return response.json()


def get_credentials_from_env() -> service_account.Credentials:
    """Gets credentials from env vars"""
    env: str = settings.GOOGLE_CLOUD_CREDENTIALS
    if env == "":
        raise ValueError(
            f"GOOGLE_CLOUD_CREDENTIALS env var not set!")
    info: dict = json.loads(base64.b64decode(env))
    return service_account.Credentials.from_service_account_info(info)


def get_gcs_client() -> storage.Client:
    """
    Returns a Google Cloud Storage client.
    """
    credentials = get_credentials_from_env()
    return storage.Client(credentials=credentials)


def upload_audio_to_gcs(bucket_name, object_name, file_path, content_type) -> str:
    """
    Uploads an audio file to Google Cloud Storage.
    """
    client = get_gcs_client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(file_path, content_type=content_type)
    return blob.name
