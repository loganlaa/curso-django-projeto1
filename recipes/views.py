from django.shortcuts import render   #lë um arquivo e renderiza ele
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', status=200, context={
        'name' : "Logan"
    })

def sobre(request):
    return HttpResponse("SOBRE!")

def contato(request):
    return render(request, 'recipes/contato.html')