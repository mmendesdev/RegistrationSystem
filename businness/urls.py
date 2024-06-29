from django.urls import path  #criei minha urls
from . import views

#agora estou criando meu caminho
urlpatterns = [   #vai ser direcionado para minha views
    path('business/', views.BusinessCreateListView.as_view(), name='business-create-list'),

]
