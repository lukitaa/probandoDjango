from django.shortcuts import render
from django.views.generic import CreateView, ListView, FormView
from .models import Usuarios
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm

# Create your views here.
class RegistrarUsuario(CreateView):
	template_name = 'usuarios/registrarUsuario.html'
	form_class = UserForm
	success_url = reverse_lazy('mostrar_usuarios')

	#model = Usuarios
	#FUNDAMENTAL este campo, sin este no funciona la muestra del form
	#ya que no sabe que campos son los que se deben mostrar
	#fields = ['usuario', 'imagen']

	#Utilizado para guardar el formulario y mantener el usuario guardado
	def form_valid(self, form):
		user = form.save()
		usuarios = Usuarios()
		usuarios.usuario = user
		usuarios.imagen = form.cleaned_data['imagen']
		usuarios.save()
		return super(RegistrarUsuario, self).form_valid(form)

class MostrarUsuarios(ListView):
	#El template que se va a utilizar
	template_name = 'usuarios/mostrarUsuarios.html'
	#El modelo que se quiere mostrar
	model = Usuarios
	#Este es el nombre de la lista que django retorna a la hora de utilizar
	#a la hora de querer mostrar los objetos
	context_object_name = "listaUsuarios"