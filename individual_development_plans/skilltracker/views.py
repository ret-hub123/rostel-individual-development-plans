from http.client import HTTPResponse

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from skilltracker.forms import AddTaskForm
from skilltracker.models import Tasks


# Create your views here.

class Index(TemplateView):
    template_name = 'skilltracker/main.html'
    extra_context = {'title': "Главная страница"}


class Employee_Tasks(ListView):
    template_name = 'skilltracker/tasks.html'
    extra_context = {'title': "Мои задачи"}
    context_object_name = 'tasks'

    def get_queryset(self):
        return Tasks.objects.filter(employee = self.request.user)


class Employees(ListView):
    template_name = 'skilltracker/employees.html'
    extra_context = {'title': "Сотрудники"}
    context_object_name = 'employees'

    def get_queryset(self):
        return get_user_model().objects.filter(role = 'employee')



class AddTask(CreateView):
    form_class = AddTaskForm
    template_name = 'skilltracker/add_task.html'
    extra_context = {'title': "Форма добавления задачи"}
    success_url = reverse_lazy('main')







