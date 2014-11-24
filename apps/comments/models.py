from django.db import models

# Create your models here.
class Comments(models.Model):
	comentario = models.CharField(max_length = 100)
	imagen = models.ImageField(upload_to = 'imagen_comentarios')

	def __unicode__(self):
		return "Usuario:" + self.usuario + "Comentario:" + self.comentario