from django.contrib import admin
from django.urls import path, include
from blog.views import home

from django.conf import settings # configuration d'affichage d'image
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name = "home"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)