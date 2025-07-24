from django.urls import path
from .views import home, contact, about

urlpatterns = [
    path("", home),
    path("about/", about),
    path("contact/", contact),
]