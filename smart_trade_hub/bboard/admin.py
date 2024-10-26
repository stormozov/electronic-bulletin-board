"""Настройки админ-панели для модели Advertisement."""

from django.contrib import admin

from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """Настройки админ-панели для модели Advertisement."""

    list_display = (
        'title',
        'content',
        'price',
        'published',
    )
    list_filter = ('published',)
    search_fields = ('title', 'content')
