from django.shortcuts import render  #lë um arquivo e renderiza ele


# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html', status=200, context={
        'name': "Logan"
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', status=200, context={
        'name': "Logan"
    })
