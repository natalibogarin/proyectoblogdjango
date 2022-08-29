from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Categoria, Comentarios,Noticia
from apps.noticias_app import models

# Register your models here.
#admin.site.register(Categoria)
#admin.site.register(Noticia)
#admin.site.register(Comentarios)

class CategoriasInline(admin.StackedInline):
    model= Noticia.categorias.through
    extra= 5

class NoticiasAdmin(admin.ModelAdmin):
    model = Noticia
    inlines = (CategoriasInline,)
    #print(CategoriasInline)
    #exclude= ('categorias',)
    raw_id_fields = ("categorias",)
    list_display = ('titulo', 'autor', 'img', 'categoria')
    search_fields = ('titulo', 'autor', 'creado')
    list_per_page = 25

    readonly_fields = ['noticia_img']

    def categoria(self, obj):
        #print("\n".join([c.nombre for c in obj.categorias.all()]))
        return "\n".join([c.nombre for c in obj.categorias.all()])

    def noticia_img(self,obj):
        return mark_safe(
            '<a href="{0}"><img src="{0}" width="30%"></a>'.format(self.img.url)
        )

    fieldsets = (
        (   
            "Contenido de la noticia", {
                # Descripcion muestra la linea donde indica que se ingresa en estae seccion
                "description" : "Ingrese la información de titulo y contenido de la noticia",
                # Campos que van relacionados a esta seccion
                "fields": [("titulo","autor"), "contenido", "noticia_img", "creado", "publicado",]
            }
        ),
    )

admin.site.register(Categoria,admin.ModelAdmin)
admin.site.register(Noticia, NoticiasAdmin)


class ComentariosAdmin(admin.ModelAdmin):
    list_display=('autor', 'cuerpo_comentario','noticia','creado','aprobado')

    list_filter = ('aprobado', 'creado')

    search_fields = ('autor', 'cuerpo_comentario')

    actions= ['aprobar_comentarios']

    def aprobar_comentarios(self,request,queryset):
        queryset.update(aprobado=True)

admin.site.register(Comentarios,ComentariosAdmin)
