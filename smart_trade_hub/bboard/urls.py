"""Настройки URL-адресов для приложения bboard."""
from django.urls import path

from .views import index

urlpatterns = [
    path('', index, name='index'),
]
