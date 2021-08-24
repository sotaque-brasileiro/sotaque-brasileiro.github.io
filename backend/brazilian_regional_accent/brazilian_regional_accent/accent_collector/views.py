import os
import uuid
import datetime

import pytz
from minio import Minio
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views, viewsets
from rest_framework import permissions
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import (
    State,
    City,
    Gender,
    Sentence,
    Speaker,
    Record,
)
from .serializers import (
    StateSerializer,
    CitySerializer,
    GenderSerializer,
    SentenceSerializer,
    SpeakerSerializer,
    RecordSerializer,
)
from .utils import validate_recaptcha_token

# TODO: remove later
import loguru


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all().order_by("abbreviation")
    serializer_class = StateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by("name")
    serializer_class = CitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all().order_by("name")
    serializer_class = GenderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SentenceViewSet(viewsets.ModelViewSet):
    queryset = Sentence.objects.all().order_by("text")
    serializer_class = SentenceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all().order_by("age")
    serializer_class = SpeakerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by("id")
    serializer_class = RecordSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class NewRecordViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        loguru.logger.info(f"Request data: {request.data}")
        if not "recaptcha_token" in request.data:
            return Response(
                {"error": "O token do reCaptcha é obrigatório!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Validate recaptcha token
        validation = validate_recaptcha_token(request.data["recaptcha_token"])
        if not validation["success"]:
            return Response(
                {"error": "O token do reCaptcha é inválido!"},
                status=status.HTTP_403_FORBIDDEN,
            )
        try:
            # Validate gender
            queryset = Gender.objects.all()
            gender = queryset.filter(radio_text=request.data["gender"]).first()
            if gender is None:
                return Response(
                    {"error": f"Gênero desconhecido: {gender}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Validate age
            try:
                age = int(request.data["age"])
            except:
                return Response(
                    {"error": f"Idade {request.data['age']} não é um número"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Get profession
            profession = request.data["profession"]
            # Validate birth_city
            city, state = request.data["birth_city"].split("/")
            birth_state = State.objects.filter(abbreviation=state).first()
            if birth_state is None:
                return Response(
                    {"error": f"Estado desconhecido: {state}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            birth_city = City.objects.filter(name=city, state=birth_state).first()
            if birth_city is None:
                return Response(
                    {"error": f"Cidade {city} desconhecida no estado {state}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Validate current_city
            city, state = request.data["current_city"].split("/")
            current_state = State.objects.filter(abbreviation=state).first()
            if current_state is None:
                return Response(
                    {"error": f"Estado desconhecido: {state}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            current_city = City.objects.filter(name=city, state=current_state).first()
            if current_city is None:
                return Response(
                    {"error": f"Cidade {city} desconhecida no estado {state}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Validate parents_original_city
            city, state = request.data["parents_original_city"].split("/")
            parents_original_state = State.objects.filter(abbreviation=state).first()
            if parents_original_state is None:
                return Response(
                    {"error": f"Estado desconhecido: {state}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            parents_original_city = City.objects.filter(
                name=city, state=parents_original_state
            ).first()
            if parents_original_city is None:
                return Response(
                    {"error": f"Cidade {city} desconhecida no estado {state}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Validate years_on_current_city
            try:
                years_on_current_city = int(request.data["years_on_current_city"])
            except:
                return Response(
                    {
                        "error": f"Anos na cidade atual {request.data['years_on_current_city']} não é um número"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Build Speaker
            speaker = Speaker(
                gender=gender,
                age=age,
                profession=profession,
                birth_city=birth_city,
                current_city=current_city,
                years_on_current_city=years_on_current_city,
                parents_original_city=parents_original_city,
            )
            # Validate sentence
            sentence = Sentence.objects.filter(text=request.data["sentence"]).first()
            if sentence is None:
                return Response(
                    {"error": f"Frase desconhecida: {request.data['sentence']}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Upload audio to MinIO
            minio_client = Minio(
                settings.MINIO_ENDPOINT,
                access_key=settings.MINIO_ACCESS_KEY,
                secret_key=settings.MINIO_SECRET_KEY,
            )
            audio_id = str(uuid.uuid4())
            tmp_filename = f"/tmp/{audio_id}.wav"
            audio_blob: InMemoryUploadedFile = request.data["audio_blob"]
            with open(tmp_filename, "wb") as f:
                f.write(audio_blob.read())
            minio_client.fput_object(
                settings.MINIO_BUCKET_NAME,
                f"accent/{audio_id}.wav",
                tmp_filename,
                content_type="audio/wav",
            )
            # Delete temporary file
            os.remove(tmp_filename)
            # Build Record
            record = Record(
                speaker=speaker,
                sentence=sentence,
                date=datetime.datetime.now(tz=pytz.timezone(settings.TZINFO)),
                audio_file_path=f"accent/{audio_id}.wav",
            )
            speaker.save()
            record.save()
        except KeyError:
            return Response(
                {"error": "Faltam parâmetros"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return views.Response({"status": "ok"})
