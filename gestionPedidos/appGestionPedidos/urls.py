from django.urls import path
from . import views

urlpatterns = [

    path('', views.clientes, name='clientes'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='detalle_cliente'),
    path('componentes/', views.componentes, name='componentes'),
    path('componentes/<int:componente_id>/', views.detalle_componentes, name='detalle_componentes'),
    path('categorias/', views.categorias, name='categorias'),
    path('productos/', views.productos, name='productos'),
    path('productos/<int:producto_id>/', views.detalle_productos, name='detalle_productos'),
    path('pedidos/<int:pedido_id>/', views.detalle_pedidos, name='detalle_pedidos')


]
