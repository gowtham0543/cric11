from django.db import models
from .models import Country
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    player = models.CharField(max_length=255)

    def __str__(self):
        return self.name
