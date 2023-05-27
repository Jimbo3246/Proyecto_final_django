from django.contrib.auth.forms import *
from django import forms
from django.contrib.auth.models import User 
from control_productos.models import *
class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('marca', 'diseno', 'empaque', 'categoria', 'genero', 'precio_costo', 'imagenProducto')
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'centrado'}),
            'diseno': forms.TextInput(attrs={'class': 'centrado'}),
            'empaque': forms.TextInput(attrs={'class': 'centrado'}),
            'categoria': forms.TextInput(attrs={'class': 'centrado'}),
            'genero': forms.TextInput(attrs={'class': 'centrado'}),
            'precio_costo': forms.NumberInput(attrs={'class': 'centrado'}),
            'imagenProducto': forms.ClearableFileInput(attrs={'class': 'centrado'}),
        }


