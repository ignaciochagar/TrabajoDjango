from .models import Cliente, Componente, Categoria, Producto, Pedido
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404

# Devuelve el listado de clientes
def clientes(request):
    clientes = Cliente.objects.order_by('nombre_empresa')
    output = ', '.join([d.nombre_empresa for d in clientes])
    return HttpResponse(output)

#devuelve los datos de un cliente
def detalle_cliente(request, cliente_id):
	cliente = Cliente.objects.get(pk=cliente_id)
	output = ', '.join([str(cliente.id) , cliente.nombre_empresa, str(cliente.telefono), cliente.persona_contacto])
	return HttpResponse(output)

# Devuelve el listado de componentes
def componentes(request):
    componentes = Componente.objects.order_by('nombre')
    output = ', '.join([d.nombre for d in componentes])
    return HttpResponse(output)

#devuelve los datos de un componente
def detalle_componentes(request, componente_id):
	componente = Cliente.objects.get(pk=componente_id)
	output = ', '.join([componente.codigo_referencia, componente.nombre, componente.marca])
	return HttpResponse(output)

# Devuelve el listado de categorias
def categorias(request):
    categorias = Categoria.objects.order_by('nombre')
    output = ', '.join([d.nombre for d in categorias])
    return HttpResponse(output)

# Devuelve el listado de productos
def productos(request):
    productos = Producto.objects.order_by('nombre')
    output = ', '.join([d.nombre for d in productos])
    return HttpResponse(output)

#devuelve los datos de cada producto
def detalle_productos(request, producto_id):
	producto = Producto.objects.get(pk=producto_id)
	output = ', '.join([producto.nombre, producto.descripcion, str(producto.precio)])
	return HttpResponse(output)

#devuelve los datos de cada pedido
def detalle_pedidos(request, pedido_id):
	pedido = Pedido.objects.get(pk=pedido_id)
	output = ', '.join([pedido.identificador, pedido.cliente])
	return HttpResponse(output)
