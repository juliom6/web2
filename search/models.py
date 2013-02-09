from django.db import models

class Usuario(models.Model):
	apodo = models.CharField(max_length = 20, unique = True)
	nombre = models.CharField(max_length = 40)
	apellido = models.CharField(max_length = 40)
	email = models.EmailField()
	telefono = models.CharField(max_length = 15)
	direccion = models.CharField(max_length = 80, blank = True)
	distrito = models.CharField(max_length = 25)
	def __unicode__(self):
		return self.apodo

class Publicacion(models.Model):
	titulo = models.CharField(max_length = 100, unique = True)
	vendedor = models.ForeignKey(Usuario)
	precio = models.DecimalField(max_digits = 15, decimal_places = 2, default = 0)
	cantidad_en_stock = models.IntegerField(default = 1)
	fecha_publicacion = models.DateField(auto_now = True)
	fecha_expiracion = models.DateField()
	descripcion = models.TextField()
	nuevo = models.BooleanField()
	imagen = models.ImageField(upload_to = 'img', verbose_name = 'Imagen', blank = True)
	def __unicode__(self):
		return self.titulo

#class Caracteristicas():
#	estado = 
	


	


