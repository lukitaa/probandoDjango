from django.contrib import admin
from .models import Comments

#Funciones para los distintos filtros del sector admin
class CommentsAdmin(admin.ModelAdmin):
	list_display = ('id', 'comentario', 'imagen_comentario')
	list_filter = ('comentario','imagen')
	search_fields = ('comentario', 'imagen')
	list_editable = ('comentario',)

#Funcion para mostrar el tag con la imagen en lugar de la URL de la imagen
	def imagen_comentario(self, comments):
		url = comments.url_imagen()
		tag = "<img src='%s' width='128' height='64'>" % url
		return tag

#Boolean para permitir mostrar imagenes en lugar del tag.	
	imagen_comentario.allow_tags = True

# Register your models here.
admin.site.register(Comments, CommentsAdmin)