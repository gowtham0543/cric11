from django.db import models
from .models import Player
# Create your models here.

class Leaderboard(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField()
