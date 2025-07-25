from http.client import HTTPResponse

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Case, When, Value, F
from datetime import date, timedelta

from skilltracker.forms import AddTaskForm,  TaskUpdateForm, AddCommentForm
from skilltracker.models import Tasks, Comments
from skilltracker.templatetags.custom_filters import days_left
from datetime import date, timedelta


# Create your views here.

class Index(ListView):
    template_name = 'skilltracker/main.html'
    extra_context = {'title': "Главная страница"}
    context_object_name = 'warning_tasks'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        today = date.today()
        if self.request.user.is_authenticated:
            return Tasks.objects.annotate(
                actual=Case(
                    When(deadline__lt=today, then=Value("death")),
                    When(deadline__lte=today + timedelta(days=3), then=Value("warning")),
                    default=Value("good"),
                )
            ).filter( Q(actual ='death') | Q(actual ='warning'), employee = self.request.user)
        else:
            return Tasks.objects.none()

class EmployeeTasks(ListView):
    template_name = 'skilltracker/tasks.html'
    extra_context = {'title': "Мои задачи"}
    context_object_name = 'tasks'

    def get_queryset(self):
        if self.request.user.role == 'employee':
            current_employee = self.request.user.id
        else:
            current_employee = self.kwargs.get('employee_id')

        return Tasks.objects.filter(employee_id = current_employee)

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

class TaskDetailUpdateView(UpdateView):
    pk_url_kwarg = 'task_pk'
    template_name = 'skilltracker/task.html'
    context_object_name = 'task'

    model = Tasks
    form_class = TaskUpdateForm
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):

        task = get_object_or_404(Tasks, pk=self.kwargs['task_pk'])
        if self.request.user.role != 'director' and self.request.user.id != task.employee_id:
            raise PermissionDenied('У вас нет доступа к этой задаче')


        context = super().get_context_data(**kwargs)
        context.update({
            'title': f'Задача # {task.title}',
            'comments': Comments.objects.filter(task_id=self.kwargs['task_pk']),
            'task_form': context.get('form')
        })
        return context

class AddComment(CreateView):
    form_class = AddCommentForm
    template_name = 'skilltracker/add_comment.html'
    extra_context = {'title': 'Форма добавления комментария'}

    def get_success_url(self):
        return reverse('task', kwargs={'task_pk': self.kwargs['task_pk']})


    def form_valid(self, form):
        form.instance.task_id = self.kwargs['task_pk']
        form.instance.user = self.request.user
        return super().form_valid(form)

class Employees(ListView):
    template_name = 'skilltracker/employees.html'
    extra_context = {'title': "Сотрудники"}
    context_object_name = 'employees'

    def get_queryset(self):
        return get_user_model().objects.filter(role = 'employee')



class AddTask(PermissionRequiredMixin, CreateView):
    form_class = AddTaskForm
    template_name = 'skilltracker/add_task.html'
    extra_context = {'title': "Форма добавления задачи"}
    success_url = reverse_lazy('main')
    permission_required = 'skilltracker.add_task'


class CompleteTaskView(DeleteView):
    model = Tasks
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        task = self.get_object()
        task.status = 'completed'
        task.progress = 100
        task.save()
        return redirect(self.get_success_url())

