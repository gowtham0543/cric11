from django.db import models
from players.models import Player

# Create your models here.

class Match(models.Model):
    country_one = models.ForeignKey(Country, on_delete = models.SET_NULL, null=True,blank=True,related_name='country_one')
    country_two = models.ForeignKey(Country, on_delete = models.SET_NULL, null=True,blank=True,related_name='country_two')
    datetime = models.DateTimeField(null=True,blank=True)
    stadium = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.country_one
    