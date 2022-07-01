from ast import If
from asyncio.windows_events import NULL
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import  Producto, Stock
from .serializers import  ProductoSerializer
@csrf_exempt
    
#=========================================================================================
@api_view(['GET','POST'])
def ingresoProducto(request):
    """
    Lista de todos los productos
    """
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=request.data)
        productostotales=Stock.objects.all()
        nombre=request.POST['producto']
        cantidad=int(request.POST['cantidad'])
        for ve in productostotales:
            if ve.productonombre==nombre:
                stockdisponible=ve.stock
        
        datos={

            }
        datos['boleta']=0
        if serializer.is_valid():
            if cantidad>stockdisponible:
                datos['mensaje']= "Error, la cantidad que desea comprar supera al stock disponible. Puede ver nuestro stock en la lista de productos"
                return render(request, 'core/resultadoCompra.html',datos)
            else:
                datos['mensaje']= "Compra completada"
                boleta=request.POST['boleta']
                datos['boleta']=boleta
                productodescontar = Stock.objects.get(productonombre=nombre)
                productodescontar.stock=productodescontar.stock-cantidad
                productodescontar.save()
                serializer.save()
                return render(request, 'core/resultadoCompra.html',datos)
        else:
            datos['mensaje']= "Se ha producido un error inesperado, la compra no se pudo efectuar"
            datos['boleta']=0
            return render(request, 'core/resultadoCompra.html',datos)
