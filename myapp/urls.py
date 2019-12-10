from django.urls import path
from .views import *


urlpatterns = [
    path('artistas/', ArtistasListView.as_view(), name='artistasListas')
]  

