from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("portfolio/<str:subpage>", views.portfolio, name="portfolio"),
    path("clients", views.clients_landing, name="clients_landing"),
    path("clients/<str:subpage>", views.clients, name="clients"),
    path("samoetikerffa", views.samoetikerffa, name="samoetikerffa"),
    path("shorts", views.shorts, name="shorts"),
    path("about", views.about, name="about"),
    path("booking", views.booking, name="booking"),
]
