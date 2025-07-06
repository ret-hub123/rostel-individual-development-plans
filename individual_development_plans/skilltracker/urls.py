from django.contrib import admin
from django.urls import path, include
from skilltracker.views import Index, Employee_Tasks, AddTask, Employees

urlpatterns = [
    path('', Index.as_view(), name = 'main'),
    path('tasks/', Employee_Tasks.as_view(), name = 'tasks'),
    path('employees/', Employees.as_view(), name = 'employees'),
    path('add-task/', AddTask.as_view(), name = 'add-task'),

]
