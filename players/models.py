from django.db import models
from countries.models import Country
from matches.models import Match
# Create your models here.

class Player(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name
