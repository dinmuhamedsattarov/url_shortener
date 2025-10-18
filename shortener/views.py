from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL
import string, random

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def home(request):
    short_url = None  # always start empty for a clean page

    if request.method == "POST":
        original_url = request.POST.get("original_url")
        if original_url:
            # get_or_create ensures no duplicates in DB
            short_url, created = ShortURL.objects.get_or_create(original_url=original_url)
            if not short_url.short_code:
                short_url.short_code = generate_short_code()
                short_url.save()
            # Only pass the short_code, don't append "?short=..."
            short_url_link = request.build_absolute_uri(f"/{short_url.short_code}")
            return render(request, "index.html", {"short_url_link": short_url_link})

    # GET requests or refresh: show empty page
    return render(request, "index.html", {"short_url_link": None})

def redirect_url(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(short_url.original_url)
