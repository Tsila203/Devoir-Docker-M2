from django.contrib import admin
from django.urls import path, include
from blog.views import home,detail

from django.conf import settings # configuration d'affichage d'image
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name = "home"),
    path("article/<int:id_article>", detail, name = "detail"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)