from django.db import models


class State(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=2)

    def __str__(self):
        return f"State {self.name} ({self.abbreviation})"


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    is_capital = models.BooleanField(default=None)

    def __str__(self):
        return f"City {self.name} ({self.state.abbreviation})"


class Gender(models.Model):
    name = models.CharField(max_length=100)
    radio_text = models.CharField(max_length=255)

    def __str__(self):
        return f"Gender {self.name}"


class Sentence(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Speaker(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    age = models.IntegerField()
    profession = models.CharField(max_length=255, default="")
    birth_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="birth_city"
    )
    current_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="current_city"
    )
    years_on_current_city = models.IntegerField()
    parents_original_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="parents_original_city"
    )

    def __str__(self):
        return f"Speaker (age={self.age}, birth_city={self.birth_city}, current_city={self.current_city})"


class Record(models.Model):
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    date = models.DateTimeField()
    audio_file_path = models.CharField(max_length=1023)

    def __str__(self):
        return f"Record (sentence={self.sentence}, speaker={self.speaker}, date={self.date})"
