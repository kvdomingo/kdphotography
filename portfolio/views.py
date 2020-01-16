import os
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    latest_dir = "portfolio/static/portfolio/img/latest/"
    latest_images = sorted(os.listdir(latest_dir), reverse=True)
    context = {
        "active_page": "index",
        "latest_images": latest_images,
    }
    return render(request, "portfolio/index.html.j2", context)
