from termios import N_MOUSE
from django.urls import path 
from . import views

urlpatterns = [
    path('home/',views.ScraperCreateView.as_view(),name='home'),

]


