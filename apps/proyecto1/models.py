from django.db import models

# Create your models here.

class Usuarios(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    edad = models.IntegerField()
    contraseña = models.CharField(max_length=50)

class Articulos(models.Model):
    
    nombrearticulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
   