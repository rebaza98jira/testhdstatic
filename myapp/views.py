from django.shortcuts import render
from .models import *
from django.views.generic import ListView

# Create your views here.


class ArtistasListView(ListView):
    model = Artista
    template_name = 'index.html'