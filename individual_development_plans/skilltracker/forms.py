from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Tasks

class AddTaskForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = '__all__'

