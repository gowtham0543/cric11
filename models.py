from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    color = models.CharField(max_length=255)
    flag = models.ImageField(max_length=255)

    def __str__(self):
        return self.name

