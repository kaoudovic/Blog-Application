from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import ListView
from .models import Entry

class HomeView(ListView):
    model =Entry
    template_name = 'entries/index.html'


