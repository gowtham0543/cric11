from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(unique=True)
    user_dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
