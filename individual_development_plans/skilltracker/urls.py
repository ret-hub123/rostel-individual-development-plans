from django.contrib import admin
from django.urls import path, include
from skilltracker.views import Index, EmployeeTasks, AddTask, Employees, EmployeeTask,TaskDetailUpdateView

urlpatterns = [
    path('', Index.as_view(), name = 'main'),

    # Руководитель
    path('employees/', Employees.as_view(), name = 'employees'),
    path('add-task/', AddTask.as_view(), name = 'add-task'),

    # Сотрудник
    path('tasks/', EmployeeTasks.as_view(), name = 'tasks'),
    path('task/<int:task_pk>', TaskDetailUpdateView.as_view(), name = 'task'),


]
