from django.db import models

# Create your models here.
class Comments(models.Model):
	comentario = models.CharField(max_length = 100)
	imagen = models.ImageField(upload_to = 'imagen_comentarios')

	def __unicode__(self):
		return "Comentario:" + self.comentario

	#Funcion para retornar la URL de la imagen de perfil
	def url_imagen(self):
		return 'http://localhost:8000/media/%s' % self.imagen		