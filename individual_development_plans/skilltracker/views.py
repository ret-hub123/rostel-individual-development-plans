from http.client import HTTPResponse

from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Index(TemplateView):
    template_name = 'skilltracker/main.html'
    extra_context = {'title': "Главная страница"}

