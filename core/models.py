from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria= models.IntegerField(primary_key=True, verbose_name='Id de Categoría')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria

    
class RegistroPersona(models.Model):
    nombre=models.CharField(max_length=40,verbose_name='Nombre')
    apellido=models.CharField(max_length=40,verbose_name='Apellido')
    rut=models.CharField(max_length=20,primary_key=True,verbose_name='Rut')
    email=models.CharField(max_length=100,verbose_name='Email')
    contraseña=models.CharField(max_length=30,verbose_name='Contraseña')
    conficontraseña=models.CharField(max_length=30,verbose_name='Confirmar Contraseña')
    genero=models.CharField(max_length=20,verbose_name='Género')
    suscripcion=models.CharField(max_length=20,verbose_name='Suscripción')
    direccion=models.CharField(max_length=100,verbose_name='Dirección')

    def __str__(self):
        return self.rut
    
    
class Producto(models.Model):
    boleta=models.IntegerField(primary_key=True,verbose_name='Boleta')
    fecha_compra=models.CharField(max_length=50,verbose_name='Fecha Compra')
    rut=models.CharField(max_length=30,verbose_name='Rut')
    email=models.CharField(max_length=60,verbose_name='Email')
    producto=models.CharField(max_length=40,verbose_name='Producto')
    cantidad=models.IntegerField(verbose_name='Cantidad de Productos')
    metodo=models.CharField(max_length=30,verbose_name='Metodo de pago')
    tarjeta=models.CharField(max_length=80,verbose_name='Tarjeta')
    fecha=models.CharField(max_length=50,verbose_name='Fecha de expiración')
    cvv=models.IntegerField(verbose_name='CVV')
    direccion=models.CharField(max_length=100,verbose_name='Dirección')
    total=models.IntegerField(verbose_name='Total de Boleta')

    def __str__(self):
        return self.rut

class Stock(models.Model):
    productonombre=models.CharField(max_length=40,verbose_name='Nombre Producto')
    stock=models.IntegerField(verbose_name='Stock')
    precio=models.IntegerField(verbose_name='Precio')
    
    def __str__(self):
        return self.productonombre
    
