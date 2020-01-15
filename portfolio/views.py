from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        "active_page": "index"
    }
    return render(request, "portfolio/index.html", context)
