from django.test import TestCase
from control_productos.models import Producto
class ProductoTests(TestCase):
    """En esta clase van todas las pruebas del modelo producto"""
    def test_creacion_producto(self):
        # caso uso esperado
        producto = Producto(marca="Kle", diseno="Diseño 1", empaque="Empaque 1", categoria="Boxer", genero="Masculino", precio_costo=10.99)
        producto.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Producto.objects.count(), 1)
        self.assertEqual(producto.marca, "Kle")
        self.assertEqual(producto.categoria, "Boxer")

    def test_curso_str(self):
        producto = Producto(marca="Yuriko",  diseno="Diseño 1", empaque="Empaque 1", categoria="Boxer", genero="Masculino", precio_costo=10.99)
        producto.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(producto.__str__(), "Boxer Yuriko Diseño 1 Masculino")
# Create your tests here.
