
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('director', 'Director'),
        ('employee', 'Employee'),
    ]
    role = models.CharField(choices=ROLE_CHOICES, default='director')

    def __str__(self):
        return f"{self.username} ({self.role})"







