from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class Account(AbstractUser):
    email = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
