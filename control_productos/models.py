from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    fecha_nacimiento=models.DateField()
    email=models.EmailField()
    telefono=models.CharField(max_length=20)
    dni=models.CharField(max_length=32)
    genero=models.CharField(max_length=32)
    class Meta:
        abstract=True

class Producto(models.Model):
    marca=models.CharField(max_length=256)
    diseno=models.CharField(max_length=256)
    empaque=models.CharField(max_length=256)
    categoria=models.CharField(max_length=256)
    genero=models.CharField(max_length=256)
    precio_costo = models.DecimalField(max_digits=8, decimal_places=2)
    imagenInstrumento = models.ImageField(null=True, blank=True, upload_to="imagenes/")


class Cliente(Persona):
    ciudad=models.CharField(max_length=256)
    distrito=models.CharField(max_length=256)
    codigo_postal=models.CharField(max_length=20,default="15494")

class Empleado(Persona):
    cargo=models.CharField(max_length=256)
    turno=models.CharField(max_length=32)
    