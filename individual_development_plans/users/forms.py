from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль")

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин")
    password1 = forms.CharField(label="Пароль")
    password2 = forms.CharField(label="Повтор пароля")

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'role']

    def clean_email(self):
        email = self.clean_email('email')
        if get_user_model().objects.filter(email = email).exists():
            return forms.ValidationError('Такой E-mail уже исподьзуется')
        return email