from django.urls import path  # criei minha urls dentro do arquivo

from . import views

# agora estou criando meu caminho
urlpatterns = [  # vai ser direcionado para minha views
    path(
        "businness/",
        views.BusinnessCreateListView.as_view(),
        name="businness-create-list",
    ),
    path(
        "businness/<uuid:pk>/",
        views.BusinnessRetrieveUpdateDestroyView.as_view(),
        name="business-detail-view",
    ),
]
