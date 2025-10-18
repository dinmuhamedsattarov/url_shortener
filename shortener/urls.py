from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Homepage / form
    path("<str:short_code>", views.redirect_url, name="redirect"),  # Redirect short URLs
]
