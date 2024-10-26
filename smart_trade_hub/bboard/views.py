"""Модуль для хранения представлений (контроллеров) приложения bboard."""

from django.shortcuts import render

from .models import Advertisement


def index(request):
    """Представление для главной страницы."""
    advertisements = Advertisement.objects.all()
    return render(
        request, 'bboard/index.html', {'advertisements': advertisements}
    )
