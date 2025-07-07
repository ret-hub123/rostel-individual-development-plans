from http.client import HTTPResponse

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView

from skilltracker.forms import AddTaskForm
from skilltracker.models import Tasks


# Create your views here.

class Index(TemplateView):
    template_name = 'skilltracker/main.html'
    extra_context = {'title': "Главная страница"}


class EmployeeTasks(ListView):
    template_name = 'skilltracker/tasks.html'
    extra_context = {'title': "Мои задачи"}
    context_object_name = 'tasks'

    def get_queryset(self):
        return Tasks.objects.filter(employee = self.request.user)

class EmployeeTask(DetailView):
    template_name = 'skilltracker/task.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Задача {get_object_or_404(Tasks, pk = self.kwargs['task_pk']).title}'
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Tasks, pk = self.kwargs['task_pk'])

"""class UpdateTask(UpdateView):
    model = Tasks
    fields = ['status', 'progress']
    template_name = 'skilltracker/add_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование задачи {self.kwargs['pk']}'
        return context

class EmployeeTask(DetailView):
    template_name = 'skilltracker/task.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Задача {get_object_or_404(Tasks, pk = self.kwargs['task_pk']).title}'
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Tasks, pk = self.kwargs['task_pk'])"""

class TaskDetailUpdateView(UpdateView, DetailView):
    pk_url_kwarg = 'task_pk'
    template_name = 'skilltracker/task.html'
    context_object_name = 'task'

    model = Tasks
    fields = ['status', 'progress']
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Задача {get_object_or_404(Tasks, pk = self.kwargs['task_pk']).title}'
        return context



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







