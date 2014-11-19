from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Usuario
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class RegistrarUsuario(CreateView):
	template_name = 'usuarios/registrarUsuario.html'
	model = Usuario
	#FUNDAMENTAL este campo, sin este no funciona la muestra del form
	#ya que no sabe que campos son los que se deben mostrar
	fields = ['usuario', 'password', 'imagen']
	succes_url = reverse_lazy('mostrar_usuarios')

class MostrarUsuarios(ListView):
	#El template que se va a utilizar
	template_name = 'usuarios/mostrarUsuarios.html'
	#El modelo que se quiere mostrar
	model = Usuario
	#Este es el nombre de la lista que django retorna a la hora de utilizar
	#a la hora de querer mostrar los objetos
	context_object_name = "listaUsuarios"