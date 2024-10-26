"""Настройки админ-панели для приложения bboard."""

from django.contrib import admin

from .models import Advertisement, Rubric


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """Настройки админ-панели для модели Advertisement."""

    list_display = (
        'title',
        'content',
        'rubric',
        'price',
        'published',
    )
    list_filter = ('published', 'rubric')
    search_fields = ('title', 'content')


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    """Настройки админ-панели для модели Rubric."""

    list_display = ('name',)
    search_fields = ('name',)
