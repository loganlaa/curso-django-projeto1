from django.urls import path
from . import views  # importando o módulo views

# "recipes:'name'", para passar o name da url de maneira mais elegante nos lugares
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),  # Usando a funcao homer que está dentro de views
    path('recipes/category/<int:category_id>/', views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),  # Recebe o parametro "id" ao acionar a view, que é
    # passado com ela junto com a request, deixando a url dinamica
]
