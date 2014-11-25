from django.db import models

# Create your models here.
class Productos(models.Model):
	nombre = models.CharField(max_length = 50)
	precio = models.IntegerField(default = 0)

	def __unicode__(self):
		return '%s' % (self.nombre,)