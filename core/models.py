from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Cliente(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
