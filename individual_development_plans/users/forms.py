from email.policy import default

from django import forms
from users.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input-pass'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']



class RegisterUserForm(UserCreationForm):

    password1 = forms.CharField(
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-input-pass'}),
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-input-pass'}),
    )
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        initial=User.ROLE_CHOICES[1],
        label="Укажите роль",
        widget=forms.Select(attrs={'class': 'form-input-role'}),
    )
    photo_profile = forms.ImageField(

        label="Фото профиля",
        widget=forms.FileInput(attrs={'class': 'form-input-photo'}),
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'role', 'first_name', 'last_name', 'email', 'photo_profile']

        labels = {
            'username': 'Логин',
            'email': 'Почта',
            'photo_profile': 'Фото пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),

        }


    def clean_email(self, **kwargs):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email = email).exists():
            return forms.ValidationError('Такой E-mail уже исподьзуется')
        return email