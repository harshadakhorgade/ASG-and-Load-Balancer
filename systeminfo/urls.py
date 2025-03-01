from django.urls import path
from .views import system_status, home

urlpatterns = [
    path("", home, name="home"),  # Root URL serves instance details
    path("status/", system_status, name="system_status"),  # JSON response
]
