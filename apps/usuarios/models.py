from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class Usuarios(models.Model):
	usuario = models.OneToOneField(User)
	imagen = models.ImageField(upload_to='foto_usuario')

	#Esto es utilizado para el texto que se va a observar desde el lado del admin
	#A la hora de mostrar cada uno de los usuarios.
	def __unicode__(self):
		return "Usuario: " + self.usuario.username

#Esto no fue necesario, pero puede serlo mas adelante.
#class UsuarioForm(ModelForm):
#	class Meta:
#		model = Usuario
#		fields = ['usuario', 'password', 'imagen']

	#Esto representa la URL a la cual se envia luego de completar un formulario.
	def get_absolute_url(self):
		return u'/usuarios/mostrar/'