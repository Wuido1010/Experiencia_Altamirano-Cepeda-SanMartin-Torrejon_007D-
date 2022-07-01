from rest_framework import serializers
from core.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['boleta' ,'fecha_compra','rut','email','producto','cantidad','metodo','tarjeta','fecha','cvv','direccion','total']
