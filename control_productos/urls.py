from control_productos.views import *
from . import views
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

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

    # URLs de Pedidos
    path("pedidos/", PedidoListView.as_view(), name="lista_pedido"),
    path('pedidos/<int:pk>/', PedidoDetailView.as_view(), name='ver_pedido'),
    path('crear-pedido/', PedidoCreateView.as_view(), name='crear_pedido'),
    path('editar-pedido/<int:pk>/', PedidoUpdateView.as_view(), name='editar_pedido'),
    path('eliminar-pedido/<int:pk>/', PedidoDeleteView.as_view(), name='eliminar_pedido'),

    #Comentarios
    path('comentario/<int:pk>/', views.ComentarioPagina.as_view(), name='comentario_producto'),
    
    path('acercaDeMi/', views.about, name='acerca_de_mi'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)