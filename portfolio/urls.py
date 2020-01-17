from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("portraits", views.portraits, name="portraits"),
    path("clients", views.clients, name="clients")
]
