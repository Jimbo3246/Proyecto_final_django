from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from control_productos.forms import *
from control_productos.models import *
from django.contrib.auth.mixins import *
from django.contrib.auth.decorators import *

# Create your views here.

#Vista de Clientes
class ClienteListView(LoginRequiredMixin,ListView):
    model = Cliente
    template_name='control_productos/lista_clientes.html'

class ClienteCreateView(LoginRequiredMixin,CreateView):
 model = Cliente
 fields =( 'nombre','apellido', 'email', 'dni','fecha_nacimiento','telefono','genero','ciudad','distrito','codigo_postal')
 success_url = reverse_lazy('lista_cliente')

class ClienteDetailView(LoginRequiredMixin,DetailView):
   model = Cliente

class ClienteUpdateView(LoginRequiredMixin,UpdateView):
   model = Cliente
   fields = ('apellido', 'nombre', 'email', 'dni')
   success_url=reverse_lazy('lista_cliente')
class ClienteDeleteView(LoginRequiredMixin,DeleteView):
   model = Cliente
   success_url=reverse_lazy('lista_cliente')

#Vista de productos
class ProductoListView(ListView):
    model = Producto
    template_name='control_productos/lista_productos.html'


class ProductoCreateView(LoginRequiredMixin,CreateView):
 model = Producto
 fields =('marca', 'diseno','empaque', 'categoria','genero','precio_costo','imagenProducto')
 success_url = reverse_lazy('lista_producto')

class ProductoDetailView(DetailView):
   model = Producto

class ProductoUpdateView(LoginRequiredMixin,UpdateView):
   model = Producto
   fields = ('marca', 'empaque', 'categoria')
   success_url=reverse_lazy('lista_producto')


class ProductoDeleteView(LoginRequiredMixin,DeleteView):
   model = Producto
   success_url=reverse_lazy('lista_producto')
#Vista de Proveedores

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'control_productos/comentario.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'control_productos/acercaDeMi.html', {})