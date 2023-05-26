from django.shortcuts import render
from django.views.generic import *
from django.urls import *
from control_productos.forms import *
from control_productos.models import *

# Create your views here.

#Vista de Clientes
class ClienteListView(ListView):
    model = Cliente
    template_name='control_productos/lista_clientes.html'

class ClienteCreateView(CreateView):
 model = Cliente
 fields =('apellido', 'nombre', 'email', 'dni')
 success_url = reverse_lazy('lista_clientes')

class ClienteDetailView(DetailView):
   model = Cliente

class ClienteUpdateView(UpdateView):
   model = Cliente
   fields = ('apellido', 'nombre', 'email', 'dni')
   success_url=reverse_lazy('lista_clientes')
class ClienteDeleteView(DeleteView):
   model = Cliente
   success_url=reverse_lazy('lista_clientes')

#Vista de productos
#Vista de Proveedores
