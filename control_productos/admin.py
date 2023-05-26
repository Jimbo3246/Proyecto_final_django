from django.contrib import admin

# Register your models here.
from control_productos.models import *
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Producto)
