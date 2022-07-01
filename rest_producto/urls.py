from django.urls import path
from rest_producto.views import  ingresoProducto

urlpatterns = [
    path('ingresoProducto/', ingresoProducto, name="ingresoProducto"),
]