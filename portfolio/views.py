import os
from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
from dotenv import load_dotenv


load_dotenv()
MEDIA_HOST = os.environ["FILESYSTEM_SYS"]
STATIC_PREFIX = "portfolio/static/portfolio"

if MEDIA_HOST == "aws":
    from boto3 import client
    S3_CUSTOM_DOMAIN = "https://kdphotography-assets.s3.amazonaws.com/"
    conn = client("s3")
elif MEDIA_HOST == "cloudinary":
    from cloudinary.api import resources
    from cloudinary.utils import cloudinary_url
    STATIC_PREFIX = "kdphotography/portfolio/static/portfolio"

MEDIA_PRIVATE_PREFIX = f"{STATIC_PREFIX}/media-private"
MEDIA_STATIC_PREFIX = "portfolio/media-private"

def file_handler(directory, compress=True):
    if MEDIA_HOST == "local":
        return os.listdir(directory)
    elif MEDIA_HOST == "cloudinary":
        conn_result = resources(prefix=directory, type="upload", max_results=500)
        files = [conn_result["resources"][f]["secure_url"] for f in range(len(conn_result["resources"]))]
        files = ["/".join(files[f].split("/")[6:]) for f in range(len(files))]
        urls = [cloudinary_url(f, transformation=[
            # {
            #     "if": "w_lt_h",
            #     "width": 0.33,
            # },
            # {
            #     "if": "else",
            #     "height": 0.33,
            # },
            {"height": 0.33 if compress else 0.8},
            {"dpr": "auto"},
            {"quality": 60}
        ])[0] for f in files]
        return urls
    elif MEDIA_HOST == "aws":
        conn_result = conn.list_objects(Bucket=os.environ["S3_BUCKET_NAME"], Prefix=directory)
        return [key["Key"] for key in conn_result["Contents"]]

def url_handler(file):
    if MEDIA_HOST == "aws":
        return S3_CUSTOM_DOMAIN + file
    elif MEDIA_HOST == "local":
        return "/".join((LATEST_PREFIX + file).split("/")[1:])
    elif MEDIA_HOST == "cloudinary":
        return file


def index(request):
    LATEST_PREFIX = f"{MEDIA_PRIVATE_PREFIX}/latest/"
    latest_images = []
    for f in sorted(file_handler(LATEST_PREFIX), reverse=True):
        latest_images.append(url_handler(f))
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
        img_src.append(url_handler(f))
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
    for f in sorted(file_handler(PREFIX, compress=False)):
        img_src.append(url_handler(f))
    context = {
        "active_page": "clients",
        "cards": zip(client_list, img_src, percent_centery, url_list),
    }
    return render(request, "portfolio/clients.html.j2", context)


def clients(request, subpage):
    PREFIX = f"{MEDIA_PRIVATE_PREFIX}/clients-{subpage}"
    img_src = []
    for f in sorted(file_handler(PREFIX), reverse=True):
        img_src.append(url_handler(f))
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
        img_src.append(url_handler(f))
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
