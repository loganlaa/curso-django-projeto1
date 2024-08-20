from django.urls import path
from . import views  #importando o módulo views

urlpatterns = [
    path('', views.home, name="recipes-home"),  #Usando a funcao homer que está dentro de views
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),
    #Recebe o parametro "id" ao acionar a view, que é passado com ela junto com a request, deixando a url dinamica
]
# "name" dá nomes únicos para as urls que podem ser referenciadas por {% url 'name' %}
