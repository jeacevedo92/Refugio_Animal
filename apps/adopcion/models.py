from django.db import models


class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=15)
	email = models.CharField(max_length=50)
	domicilio = models.CharField(max_length=50)

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellidos)


