from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Feedback(models.Model):
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    surname = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    feedback = models.TextField()
    rating = models.PositiveIntegerField()


