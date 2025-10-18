from django.db import models

class ShortURL(models.Model):
    original_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # <- auto_now_add fixes your error

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"
