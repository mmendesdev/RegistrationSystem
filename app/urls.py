from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #estou incluido todas as rotas que eu criar dentro de Businnnes URLS
    path('api/v1/', include('businnes.urls'))
]
