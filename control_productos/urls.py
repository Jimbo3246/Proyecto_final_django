from control_productos.views import *
from . import views
from django.urls import path
from django.contrib import admin

urlpatterns=[
    #URLS de Clientes
    path("clientes/",ClienteListView.as_view(), name="lista_cliente"),
    path('clientes/<int:pk>/',ClienteDetailView.as_view(), name='ver_cliente'),
    path('crear-cliente/',ClienteCreateView.as_view(), name='crear_cliente'),
    path('editar-cliente/<int:pk>/',ClienteUpdateView.as_view(), name='editar_cliente'),
    path('eliminar-cliente/<int:pk>/',ClienteDeleteView.as_view(), name='eliminar_cliente'),

    #URLS de Productos
    path("productos/",ProductoListView.as_view(), name="lista_producto"),
    path('productos/<int:pk>/',ProductoDetailView.as_view(), name='ver_producto'),
    path('crear-producto/',ProductoCreateView.as_view(), name='crear_producto'),
    path('editar-producto/<int:pk>/',ProductoUpdateView.as_view(), name='editar_producto'),
    path('eliminar-producto/<int:pk>/',ProductoDeleteView.as_view(), name='eliminar_producto'),
    
    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]