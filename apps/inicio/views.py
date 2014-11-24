from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PaginaInicio(TemplateView):
	template_name = 'inicio/inicio.html'

class Registrarse(TemplateView):
	template_name = 'inicio/registrarse.html'