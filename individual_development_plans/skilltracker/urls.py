from django.contrib import admin
from django.urls import path, include
from skilltracker.views import Index, EmployeeTasks, AddTask, Employees, EmployeeTask, UpdateTask

urlpatterns = [
    path('', Index.as_view(), name = 'main'),
    path('tasks/', EmployeeTasks.as_view(), name = 'tasks'),
    path('employees/', Employees.as_view(), name = 'employees'),
    path('add-task/', AddTask.as_view(), name = 'add-task'),
    path('task/<int:task_pk>', EmployeeTask.as_view(), name = 'task'),
    path('edit/<int:pk>', UpdateTask.as_view(), name = 'edit-task'),

]
