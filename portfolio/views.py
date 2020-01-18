import os
from django.shortcuts import render
from django.http import HttpResponse
from boto3 import client
from dotenv import load_dotenv


load_dotenv()
if os.environ["FILESYSTEM_SYS"] == "AWS":
    conn = client("s3")


def file_handler(directory):
    if os.environ["FILESYSTEM_SYS"] == "local":
        return os.listdir(directory)
    elif os.environ["FILESYSTEM_SYS"] == "AWS":
        conn_result = conn.list_objects(Bucket=os.environ["S3_BUCKET_NAME"], Prefix=directory)
        return [key["Key"] for key in conn_result["Contents"]]


def index(request):
    latest_dir_static = "portfolio/media-private/latest/"
    latest_dir = "portfolio/static/" + latest_dir_static
    latest_images = [latest_dir_static + f for f in sorted(file_handler(latest_dir), reverse=True)]
    context = {
        "active_page": "index",
        "image_src": latest_images,
        "html_title": "Latest",
    }
    return render(request, "portfolio/gallery_template.html.j2", context)


def portfolio(request, subpage):
    img_dir_static = f"portfolio/media-private/{subpage}/"
    img_dir = "portfolio/static/" + img_dir_static
    img_src = [img_dir_static + f for f in sorted(file_handler(img_dir), reverse=True)]
    context = {
        "active_page": "portfolio",
        "image_src": img_src,
        "html_title": "Portraits",
    }
    return render(request, "portfolio/gallery_template.html.j2", context)


def clients_landing(request):
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
    percent_centery = [
        "45%",
        "45%",
        "15%",
        "45%",
        "40%"
    ]
    url_list = [
        "upecotour",
        "upsan",
        "uprotc",
        "upcos",
        "uppda",
    ]
    context = {
        "active_page": "clients",
        "cards": zip(client_list, cover_list, percent_centery, url_list),
    }
    return render(request, "portfolio/clients.html.j2", context)


def clients(request, subpage):
    img_dir_static = f"portfolio/media-private/clients-{subpage}/"
    img_dir = "portfolio/static/" + img_dir_static
    img_src = [img_dir_static + f for f in sorted(file_handler(img_dir), reverse=True)]
    context = {
        "active_page": "clients",
        "image_src": img_src,
        "html_title": "Clients",
    }
    return render(request, "portfolio/gallery_template.html.j2", context)


def samoetikerffa(request):
    context = {
        "html_title": "#samoetikerffa",
        "active_page": "contests"
    }
    return render(request, "portfolio/construction.html.j2", context)


def shorts(request):
    context = {
        "html_title": "Short Films",
        "active_page": "shorts"
    }
    return render(request, "portfolio/construction.html.j2", context)


def about(request):
    context = {
        "html_title": "About",
        "active_page": "about"
    }
    return render(request, "portfolio/construction.html.j2", context)


def booking(request):
    context = {
        "html_title": "Booking",
        "active_page": "booking"
    }
    return render(request, "portfolio/construction.html.j2", context)
