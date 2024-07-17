from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # estou incluido todas as rotas que eu criei dentro de Businnnes URLS
    path("api/v1/", include("businness.urls")),
]
