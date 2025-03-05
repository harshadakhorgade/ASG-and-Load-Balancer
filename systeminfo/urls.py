from django.contrib import admin
from django.urls import path
from .views import system_status, home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", home, name="home"),  # Root URL serves instance details
    path("status/", system_status, name="system_status"),  # JSON response
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
