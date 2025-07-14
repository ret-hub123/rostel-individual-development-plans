from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth import get_user_model

from users.models import User
from .models import Tasks, Comments


class AddTaskForm(forms.ModelForm):
    employee = forms.ModelChoiceField(
        queryset = get_user_model().objects.filter(role = 'employee'),
        label="Выберите сотрудника",
        widget=forms.Select(attrs={'class': 'form-input-employee'}),
    )

    deadline = forms.DateField(
        label='Срок выполнения',
        widget=forms.DateInput(attrs={'class': 'form-input-deadline'}),
    )

    class Meta:
        model = Tasks
        fields = ['title', 'description', 'deadline', 'employee']

        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'employee': 'Выберите сотрудника'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input-area'})
        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['status', 'progress']

        widgets = {
        'status': forms.Select(attrs={'class': 'form-input'}),
        'progress': forms.TextInput(attrs={'class': 'form-input'})
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-input'})
        }



