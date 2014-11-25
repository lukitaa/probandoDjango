from django.contrib import admin
from .models import Usuarios

#Funciones para los distintos filtros del sector admin
class UsuariosAdmin(admin.ModelAdmin):
	list_display = ('id', 'usuario', 'imagen_usuario')
	list_filter = ('usuario',)
	search_fields = ('usuario__username', 'imagen')
	list_editable = ('id',)

#Funcion para mostrar el tag con la imagen en lugar de la URL de la imagen
	def imagen_usuario(self, usuarios):
		url = usuarios.url_imagen()
		tag = "<img src='%s' width='128' height='64'>" % url
		return tag

#Boolean para permitir mostrar imagenes en lugar del tag.	
	imagen_usuario.allow_tags = True

# Register your models here.
admin.site.register(Usuarios, UsuariosAdmin)