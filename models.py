from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(null=True, blank=True)
    bio = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
