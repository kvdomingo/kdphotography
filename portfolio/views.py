import os
from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
from boto3 import client
from dotenv import load_dotenv


ON_AWS = (os.environ["FILESYSTEM_SYS"] == "aws")
S3_CUSTOM_DOMAIN = "https://kdphotography-assets.s3.amazonaws.com/"
load_dotenv()
if ON_AWS:
    conn = client("s3")
STATIC_PREFIX = "portfolio/static/portfolio"
MEDIA_PRIVATE_PREFIX = f"{STATIC_PREFIX}/media-private"
MEDIA_STATIC_PREFIX = "portfolio/media-private"


def file_handler(directory):
    if not ON_AWS:
        return os.listdir(directory)
    else:
        conn_result = conn.list_objects(Bucket=os.environ["S3_BUCKET_NAME"], Prefix=directory)
        return [key["Key"] for key in conn_result["Contents"]]


def index(request):
    LATEST_PREFIX = f"{MEDIA_PRIVATE_PREFIX}/latest/"
    latest_images = []
    for f in sorted(file_handler(LATEST_PREFIX), reverse=True):
        latest_images.append(S3_CUSTOM_DOMAIN + f if ON_AWS else "/".join((LATEST_PREFIX + f).split("/")[1:]))
    context = {
        "active_page": "index",
        "image_src": latest_images,
        "html_title": "Latest",
    }
    return render(request, "portfolio/gallery_template.html.j2", context)


def portfolio(request, subpage):
    PREFIX = f"{MEDIA_PRIVATE_PREFIX}/{subpage}"
    img_src = []
    for f in sorted(file_handler(PREFIX), reverse=True):
        img_src.append(S3_CUSTOM_DOMAIN + f if ON_AWS else static(f"{MEDIA_STATIC_PREFIX}/{subpage}/{f}"))
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

    PREFIX = f"{MEDIA_PRIVATE_PREFIX}/clients-landing/"
    img_src = []
    for f in cover_list:
        img_src.append(S3_CUSTOM_DOMAIN + PREFIX + f if ON_AWS else "/".join((PREFIX + f).split("/")[1:]))
    context = {
        "active_page": "clients",
        "cards": zip(client_list, img_src, percent_centery, url_list),
    }
    return render(request, "portfolio/clients.html.j2", context)


def clients(request, subpage):
    PREFIX = f"{MEDIA_PRIVATE_PREFIX}/clients-{subpage}"
    img_src = []
    for f in sorted(file_handler(PREFIX), reverse=True):
        img_src.append(S3_CUSTOM_DOMAIN + f if ON_AWS else static(f"{MEDIA_STATIC_PREFIX}/clients-{subpage}/{f}"))
    context = {
        "active_page": "clients",
        "image_src": img_src,
        "html_title": "Clients",
    }
    return render(request, "portfolio/gallery_template.html.j2", context)


def samoetikerffa(request):
    PREFIX = f"{MEDIA_PRIVATE_PREFIX}/samoetikerffa"
    img_src = []
    for f in sorted(file_handler(PREFIX), reverse=True):
        img_src.append(S3_CUSTOM_DOMAIN + f if ON_AWS else static(f"{MEDIA_STATIC_PREFIX}/samoetikerffa/{f}"))
    context = {
        "html_title": "#samoetikerffa",
        "active_page": "contests",
        "image_src": img_src,
    }
    return render(request, "portfolio/gallery_template.html.j2", context)


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
