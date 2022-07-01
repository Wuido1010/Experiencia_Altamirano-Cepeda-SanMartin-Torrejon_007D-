from django.contrib import admin
from .models import Categoria, RegistroPersona, Producto, Stock
# Register your models here.
admin.site.register(Categoria)
admin.site.register(RegistroPersona)
admin.site.register(Producto)
admin.site.register(Stock)