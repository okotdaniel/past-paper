from django.urls import path 
from papers.views import HomeView

urlpatterns = [
    path('',  HomeView, name="home ")
]