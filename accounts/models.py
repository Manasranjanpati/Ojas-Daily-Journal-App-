from django.db import models
from django.contrib.auth.models import AbstractUser


class OjasCustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    phonenumber = models.CharField(max_length=100)
