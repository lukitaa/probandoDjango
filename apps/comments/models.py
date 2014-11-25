from django.db import models

# Create your models here.
class Comments(models.Model):
	comentario = models.CharField(max_length = 100)
	imagen = models.ImageField(upload_to = 'imagen_comentarios')

	def __unicode__(self):
<<<<<<< HEAD
		return "Comentario:" + self.comentario
=======
		return "Usuario:" + self.usuario + "Comentario:" + self.comentario
>>>>>>> 86e9af534e61d30fa44c8d053cfcb146ec1773cd

	#Funcion para retornar la URL de la imagen de perfil
	def url_imagen(self):
		return 'http://localhost:8000/media/%s' % self.imagen		