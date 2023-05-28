from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=32)
    genero = models.CharField(max_length=32)

    class Meta:
        abstract = True

class Producto(models.Model):
    marca = models.CharField(max_length=256)
    diseno = models.CharField(max_length=256)
    empaque = models.CharField(max_length=256)
    categoria = models.CharField(max_length=256)
    genero = models.CharField(max_length=256)
    precio_costo = models.DecimalField(max_digits=8, decimal_places=2)
    imagenProducto = models.ImageField(null=True, blank=True, upload_to='productos')
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.categoria} {self.marca} {self.diseno} {self.genero}"

class Cliente(Persona):
    ciudad = models.CharField(max_length=256)
    distrito = models.CharField(max_length=256)
    codigo_postal = models.CharField(max_length=20, default="15494")
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}-{self.apellido}"

class Comentario(models.Model):
    producto = models.ForeignKey(Producto, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.mensaje)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    importe = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.producto and self.cantidad:
            self.importe = self.producto.precio_costo * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido de {self.cliente.nombre}: {self.cantidad} {self.producto.marca} {self.producto.diseno}"

    

    