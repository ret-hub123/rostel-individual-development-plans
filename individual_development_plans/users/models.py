
from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class User(AbstractUser):
    ROLE_CHOICES = [
        ('director', 'Director'),
        ('employee', 'Employee'),
    ]
    role = models.CharField(choices=ROLE_CHOICES, default='director')
    photo_profile = models.ImageField(upload_to = 'image_for_users/', default = None, blank = True, null = True)

    def __str__(self):
        return f"{self.username} ({self.role})"







