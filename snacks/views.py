from django.db import models
from django.shortcuts import render
from .models import Snacks
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.
class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snacks

class DetalisView(DetailView):
    template_name='snack_detalis.html'
    model=Snacks