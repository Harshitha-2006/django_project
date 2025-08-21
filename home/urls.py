from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path("", views.index, name="home"),  # Map the index view
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact")
]
