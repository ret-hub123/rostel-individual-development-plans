from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegisterUserForm


# Create your views here.c

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}


class UsersCreate(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/registration.html'
    extra_context = {'title': "Регистрация сотрдника"}
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        role = form.cleaned_data['role']

        if role == 'employee':
            group = Group.objects.get(name='Employee')
        else:
            group = Group.objects.get(name='Director')
            user.is_staff = True
            user.save()

        user.groups.add(group)

        return super().form_valid(form)

