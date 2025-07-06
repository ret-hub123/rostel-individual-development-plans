from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Tasks(models.Model):
    status_choice = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершена')
    ]

    title = models.CharField(max_length=80)
    description = models.TextField(max_length=250)
    deadline = models.DateTimeField(verbose_name="Срок выполнения")
    status = models.CharField(default='new', choices=status_choice)
    progress = models.IntegerField(default=0, validators=
            [MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, null=True)
    text = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

