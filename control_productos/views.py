from django.shortcuts import *
from django.views.generic import *
from django.urls import *
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
 def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

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
 form_class = ProductoForm
 success_url = reverse_lazy('lista_producto')
 def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class ProductoDetailView(DetailView):
   model = Producto

class ProductoUpdateView(LoginRequiredMixin,UpdateView):
   model = Producto
   fields = ('marca', 'empaque', 'categoria')
   success_url=reverse_lazy('lista_producto')


class ProductoDeleteView(LoginRequiredMixin,DeleteView):
   model = Producto
   success_url=reverse_lazy('lista_producto')
#Vista de Pedidos
class PedidoListView(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'control_productos/lista_pedidos.html'

class PedidoCreateView(LoginRequiredMixin, CreateView):
    model = Pedido
    fields = ('cliente', 'producto', 'cantidad')
    success_url = reverse_lazy('lista_pedido')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class PedidoDetailView(LoginRequiredMixin, DetailView):
    model = Pedido

class PedidoUpdateView(LoginRequiredMixin, UpdateView):
    model = Pedido
    fields = ('cliente', 'producto', 'cantidad')
    success_url = reverse_lazy('lista_pedido')

class PedidoDeleteView(LoginRequiredMixin, DeleteView):
    model = Pedido
    success_url = reverse_lazy('lista_pedido')
# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'control_productos/comentario.html'
    def form_valid(self, form):
        producto = get_object_or_404(Producto, pk=self.kwargs['pk'])
        form.instance.producto = producto
        form.instance.creador = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ver_producto', kwargs={'pk': self.kwargs['pk']})

# ACERCA DE MI

def about(request):
    return render(request, 'control_productos/acercaDeMi.html', {})