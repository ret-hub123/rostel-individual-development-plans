from django.contrib import admin
from django.urls import path, include


from skilltracker.views import Index, EmployeeTasks, AddTask, Employees, EmployeeTask, TaskDetailUpdateView, AddComment, \
    CompleteTaskView

urlpatterns = [
    path('', Index.as_view(), name = 'main'),

    # Руководитель
    path('employees/', Employees.as_view(), name = 'employees'),
    path('add-task/', AddTask.as_view(), name = 'add-task'),
    path('employee/<int:employee_id>/tasks/', EmployeeTasks.as_view(), name = 'employee-tasks'),

    # Сотрудник
    path('tasks/', EmployeeTasks.as_view(), name = 'tasks'),
    path('task/<int:task_pk>', TaskDetailUpdateView.as_view(), name = 'task'),
    path('task/<int:task_pk>/add-comment', AddComment.as_view(), name = 'add-comment'),
path('task/complete/<int:pk>/', CompleteTaskView.as_view(), name='complete-task'),


]
