from django.shortcuts import get_list_or_404, render  #lë um arquivo e renderiza ele
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')  # Cria a var recipes que vai receber uma receita armazenada na model, ao invés de gerar aleatório
    return render(request, 'recipes/pages/home.html', status=200,
                  context={  # context é importante para passar variáveis aplicadas somente ä pagina
                      'recipes': recipes
                  })


def category(request, category_id):

    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
        # Como acesso id da categoria sendo que id é uma Chave Secundária dentro da tabela Recipe? USA dois
        # underlines ( __id) e passa o id Queria pegar um campo da category que é uma forein key dentro de recipe
    ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={  # context é importante para passar
        # variáveis aplicadas somente ä pagina
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |'
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', status=200, context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
