from django.shortcuts import render
from .models import Comments
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
class CrearComment(CreateView):
	template_name = 'comments/crearComentario.html'
	model = Comments
	fields = ['comentario', 'imagen']
	success_url = reverse_lazy('mostrar_comentarios')

	def myview(request):
		if request.user.get_profile().is_store():
			return HttpResponseRedirect('inicio/inicio.html')
	
class MostrarComments(ListView):
	template_name = 'comments/mostrarComentarios.html'
	model = Comments
	context_object_name = "listaComments"