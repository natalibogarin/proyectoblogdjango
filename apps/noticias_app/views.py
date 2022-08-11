from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    texto = {'mensaje_texto': 'Esta es mi primer pagina :)'}
    return render(request, 'index.html',{})

def nosotros(request):
    return render(request, 'nosotros.html',{})

def noticias(request):
    return render(request, 'noticias.html',{})
