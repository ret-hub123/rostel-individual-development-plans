
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django import forms
from django.urls import reverse


class User(AbstractUser):
    ROLE_CHOICES = [
        ('director', 'Director'),
        ('employee', 'Employee'),
    ]
    role = models.CharField(choices=ROLE_CHOICES, default='director')
    photo_profile = models.ImageField(upload_to = 'image_for_users/', default = None, blank = True, null = True)

    def __str__(self):
        return f"{self.username} ({self.role})"

    def get_tasks_employee(self):
        return reverse('employee-tasks', kwargs={'employee_id': self.id})









