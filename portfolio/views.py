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


def portraits(request):
    portraits_dir = "portfolio/static/portfolio/img/portraits/"
    portraits_images = sorted(os.listdir(portraits_dir), reverse=True)
    context = {
        "active_page": "portfolio",
        "portraits_images": portraits_images,
    }
    return render(request, "portfolio/portraits.html.j2", context)


def clients(request):
    client_list = [
        "UP CLUB FOR THE ENVIRONMENT AND TOURISM",
        "UP SIGMA ALPHA NU SORORITY",
        "UP DILIMAN RESERVE OFFICERS' TRAINING CORPS",
        "UP DILIMAN CORPS OF SPONSORS",
        "UP PHI DELTA ALPHA SORORITY",
    ]
    cover_list = [
        "ecotour2019.jpg",
        "upsan2019.jpg",
        "uprotc2019.jpg",
        "upcos2019.jpg",
        "uppda2019.jpg",
    ]
    percent_centery = ["45%", "45%", "15%", "45%", "40%"]
    context = {
        "active_page": "clients",
        "cards": zip(client_list, cover_list, percent_centery),
    }
    return render(request, "portfolio/clients.html.j2", context)
