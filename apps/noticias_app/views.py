from time import timezone
from django.shortcuts import render
from .models import Noticia,Categoria,Comentarios
from django.http.response import Http404
#from django.http import HttpResponse


# Create your views here.
def index(request):
    texto = {'mensaje_texto': 'Esta es mi primer pagina :)'}
    ultimasnoticias = Noticia.objects.all().order_by('creado').reverse()[:3]
    context ={
        'noticiasdestacadas':ultimasnoticias
    }
    return render(request, 'index.html',context)

def nosotros(request):
    return render(request, 'nosotros.html',{})

def noticias(request):
    lista_noticias = Noticia.objects.all().order_by('creado')
    context = {
        "noticias": lista_noticias,
    }
    return render(request, 'noticias.html',context)

def noticiasdetalle(request,id):
    try:
        datanoticia = Noticia.objects.get(id=id)
        lista_comentarios = Comentarios.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')

    context = {
        "noticia": datanoticia,
        "comentarios":lista_comentarios
    }

    return render(request,'detalle-noticia.html',context)