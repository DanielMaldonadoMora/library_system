from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    status= models.CharField(max_length=255, null=True)

    def __str__(self):
       return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []