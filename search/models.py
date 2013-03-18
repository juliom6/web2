from django.db import models

class Usuario(models.Model):
    alias = models.CharField(max_length=20, unique=True)
	nombres = models.CharField(max_length=40)
	apellidos = models.CharField(max_length = 40)
	email = models.EmailField()
	telefono = models.CharField(max_length = 15, blank = True)
	direccion = models.CharField(max_length = 80, blank = True)
	distrito = models.CharField(max_length = 25, blank = True)
    def __unicode__(self):
        return self.alias

class Publicacion(models.Model):
	titulo = models.CharField(max_length = 100, unique = True)
	vendedor = models.ForeignKey(Usuario)
	precio = models.DecimalField(max_digits = 15, decimal_places = 2, default = 0)
	cantidad_en_stock = models.IntegerField(default = 1)
	fecha_publicacion = models.DateField(auto_now = True)
	fecha_expiracion = models.DateField()
	descripcion = models.TextField()
	nuevo = models.BooleanField()
	imagen = models.ImageField(upload_to = 'img', verbose_name = 'Imagen de la publicacion', blank = True)
	def __unicode__(self):
		return self.titulo

class Categoria(models.Model):
	nombre = models.CharField(max_length = 20, unique = true)
	descripcion = models.TextField()
	
	def __unicode__(self):
		return self.nombre

class Comentario(models.Model):
	publicacion = models.ForeignKey(Publicacion)
	descripcion = models.TextField()
	usuario = models.ForeignKey(Usuario)
	fecha_creacion = models.DateField(auto_now = True)
	def __unicode__(self):
		return self.nombre
	class Meta:
		ordering = ['fecha_creacion']


