from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="gym.home"),
    path('contact/', views.contact, name="gym.contact"),
    path('trainer/', views.trainer, name = "gym.trainer"),
    path('whyus/', views.why, name = 'gym.why'),
]