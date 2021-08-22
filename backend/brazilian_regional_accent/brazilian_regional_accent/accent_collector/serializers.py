from rest_framework import serializers

from .models import (
    State,
    City,
    Gender,
    Sentence,
    Speaker,
    Record,
)


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ('url', 'name', 'abbreviation')


class CitySerializer(serializers.HyperlinkedModelSerializer):
    state = StateSerializer()

    class Meta:
        model = City
        fields = ('url', 'name', 'state', 'latitude', 'longitude')


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = ('url', 'name', 'radio_text')


class SentenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sentence
        fields = ('url', 'text')


class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    gender = GenderSerializer()
    birth_city = CitySerializer()
    current_city = CitySerializer()
    parents_original_city = CitySerializer()

    class Meta:
        model = Speaker
        fields = ('url', 'gender', 'age', 'profession', 'birth_city',
                  'current_city', 'years_on_current_city', 'parents_original_city')


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    sentence = SentenceSerializer()
    speaker = SpeakerSerializer()

    class Meta:
        model = Record
        fields = ('url', 'sentence', 'speaker', 'date', 'audio_file_path')
