from control_productos.views import *
from django.urls import path
from django.contrib import admin

urlpatterns=[
    #URLS de Clientes
    path("clientes/",ClienteListView.as_view(), name="lista_cliente"),
    path('clientes/<int:pk>/',ClienteDetailView.as_view(), name='ver_cliente'),
    path('crear-cliente/',ClienteCreateView.as_view(), name='crear_cliente'),
    path('editar-cliente/<int:pk>/',ClienteUpdateView.as_view(), name='editar_cliente'),
    path('eliminar-cliente/<int:pk>/',ClienteDeleteView.as_view(), name='eliminar_cliente'),

]