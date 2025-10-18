from django.contrib import admin
from .models import ShortURL

# Регистрируем модель в админке
admin.site.register(ShortURL)
