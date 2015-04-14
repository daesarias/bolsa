from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

class Usuario(models.Model):
        usuario = models.ForeignKey(User)
	tipo = models.CharField(max_length=50)
	numero = models.CharField(max_length=50, unique=True)
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=20, null=True, blank=True)
	fecha_nacimiento = models.CharField(max_length=20, null=True, blank=True)

        estado= models.CharField(max_length=30, default='En espera')  #en espera,aceptado,rechazado
	perfil= models.CharField(max_length=30, default='Indefinido')  #funcionario, ciudadano etc
	activo = models.BooleanField(default=True)                      #activo, inactivo
	fecha_registro = models.DateTimeField(auto_now=True)		#fecha de registro

	def __unicode__(self):	
		return self.numero
