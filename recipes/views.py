from django.shortcuts import render  #lë um arquivo e renderiza ele
from utils.recipes.factory import make_recipe

# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html', status=200, context={ #context é importante para passar variáveis aplicadas somente ä pagina
        'recipes': [make_recipe() for _ in range(10)]
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', status=200, context={
        'recipe': make_recipe(),
        'is_detail_page' : True,
    })
