from django.shortcuts import render
from .models import Comments
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class CrearComment(CreateView):
	template_name = 'comments/crearComentario.html'
	model = Comments
	fields = ['comentario', 'imagen']
	success_url = reverse_lazy('mostrar_comentarios')

class MostrarComments(ListView):
	template_name = 'comments/mostrarComentarios.html'
	model = Comments
	context_object_name = "listaComments"