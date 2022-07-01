from django.shortcuts import redirect, render
from django.views.decorators import csrf
from numpy import DataSource
from .models import Categoria, RegistroPersona, Producto, Stock
from .forms import RegistroPersona
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
def inicio(request):
    return render(request, 'core/inicio.html')
def nose(request):
    return render(request, 'core/nose.html')


def formulario2(request):
    return render(request, 'core/formulario2.html')
def  GaleriaDeFotos(request):
    return render(request, 'core/GaleriaDeFotos.html')

def quienesSomos(request):
    return render(request, 'core/quienesSomos.html')

def home2(request):
    return render(request, 'core/home2.html')

def login(request):
    return render(request, 'core/login.html')

def forms_persona(request):
    return render(request, 'core/forms_persona.html')

def consultarRegistro(request):
    return render(request, 'core/consultarRegistro.html')






def mostrar(request):
    persona= RegistroPersona.objects.all()
    datos={
        'persona': persona
    }
    return render (request, 'core/mostrar.html', datos)


def form_persona(request):
    datos={

    }
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    rut=request.POST['rut']
    email=request.POST['email']
    contraseña=request.POST['contraseña']
    conficontraseña=request.POST['conficontraseña']
    genero=request.POST['genero']
    direccion=request.POST['direccion']
    suscripcion=request.POST['suscripcion']

    personaencontrada=RegistroPersona.objects.filter(rut=rut)
    if personaencontrada:
        datos['mensaje']= "Error, ya existe una persona registrada con ese Rut"
        return render(request, 'core/ResultadoRegistro.html',datos)
    else:
        datos['mensaje']= "Registro completado"
        persona=RegistroPersona.objects.create(nombre=nombre, apellido=apellido, rut=rut, email=email, contraseña=contraseña, conficontraseña=conficontraseña, genero=genero, direccion=direccion, suscripcion=suscripcion)
        return render(request, 'core/ResultadoRegistro.html',datos)

def form_mod_persona(request,id):
    persona= RegistroPersona.objects.get(rut=id)
    try:
        rut=request.POST['rut']
    except:
        rut=0
    datos= {
        'Persona':persona
        
    }
    datos['rut']=rut
    return render(request, 'core/form_mod_persona.html',datos)

def loginRegistro(request):
    datos={

    }
    try:
        rut=request.POST['rut']
        contraseña=request.POST['contraseña']
        personas=RegistroPersona.objects.filter(rut=rut).filter(contraseña=contraseña)
        personabuscada=RegistroPersona.objects.filter(rut=rut)
        #personabuscada=Personas.objects.filter(contraseña=contraseña)

        if personas:
                datos['mensaje']= "Usuario encontrado correctamente"
                personax=RegistroPersona.objects.get(rut=rut)
                datos['RegistroPersona']=personax
                return render (request, 'core/consultarRegistro.html',datos)
        elif personabuscada:
            datos['mensaje']= "Usuario encontrado pero contraseña incorrecta"
            return render (request, 'core/consultarRegistro.html',datos)    
        else:
            datos['mensaje'] = "Usuario no encontrado"
            return render (request, 'core/consultarRegistro.html',datos)
    except:
        datos['rut']=0
        return render (request, 'core/consultarRegistro.html',datos)
    
    
def editarRegistro(request):
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    rut=request.POST['rut']
    email=request.POST['email']
    contraseña=request.POST['contraseña']
    conficontraseña=request.POST['conficontraseña']
    genero=request.POST['genero']
    suscripcion=request.POST['suscripcion']
    direccion=request.POST['direccion']
    datos={

    }
    datos['mensaje'] = "Modificados correctamente"

    persona = RegistroPersona.objects.get(rut=rut)
    persona.nombre=nombre
    persona.apellido=apellido
    persona.email=email
    persona.contraseña=contraseña
    persona.conficontraseña=conficontraseña
    persona.genero=genero
    persona.suscripcion=suscripcion
    persona.direccion=direccion
    persona.save()

    return render(request, 'core/consultarRegistro.html',datos)


def forms_venta(request):
    datos={

    }
    datos['producto']=1
    return render (request, 'core/forms_venta.html',datos)

def ventas_completado(request):
    datos={

        }
    try:    
        nombre=request.POST['nombre']
        datos['producto']=nombre

        return render (request, 'core/forms_venta.html',datos)
    except:
        datos['producto']=0
        return render (request, 'core/forms_venta.html',datos)


def proceso_Venta(request):
    datos={

    }
    try:
        rut=request.POST['rut']
        producto=request.POST['producto']
        cantidad=request.POST['cantidad']
        personas=RegistroPersona.objects.filter(rut=rut).filter(suscripcion='Si')
        productoStock=Stock.objects.all()
        
        for i in productoStock:
                if i.productonombre==producto:
                    precio=int(i.precio)
                    precio2=int(i.precio)
                    precioinicio=int(i.precio)
    
        precio=precio*int(cantidad)
        precio2=precio2*int(cantidad)
        
        datos['precio']=precio
        datos['rut']=rut
        datos['producto']=producto
        datos['cantidad']=cantidad
        datos['precioinicio']=precioinicio
        descuento=0
        descuento2=0
        boleta=100
        fecha=datetime.today().strftime('%Y-%m-%d')
        productos=Producto.objects.all()
        
        
        for i in productos:
            boleta=boleta+1
        datos['boleta']=boleta
        
        if personas:
            descuento=descuento+5
            descuento2=descuento2+5
            
        if precio>50000:
            descuento=descuento+10
            descuento2=descuento2+10
            
            
        if descuento==0:
            datos['descuento']=descuento
            datos['descuento2']=descuento2
            datos['fecha']=fecha
            precio=round(precio)
            datos['total']=precio
            return render (request, 'core/procesoVenta.html',datos)
        
        
        else:
            descuento=100-descuento
            descuento=descuento/100
            descuento2=descuento2/100
            precio=round(precio*descuento)
            datos['total']=precio
            datos['fecha']=fecha
            preciodescuento=round(precio2*descuento2)
            datos['descuento']=descuento
            datos['precio2']=preciodescuento
            datos['descuento2']=int(descuento2*100)
            
            return render (request, 'core/procesoVenta.html',datos)
    except:
        rut=0
        datos['rut']=rut
        return render (request, 'core/procesoVenta.html',datos)

def loginConsultarVenta(request):
    return render(request, 'core/loginConsultarVenta.html')
    
    
def consultarCompra(request,id):
    datos={

    }
    persona=RegistroPersona.objects.get(rut=id)
    try:
        compras=Producto.objects.filter(rut=id)
        rut=request.POST['rut']
        datos['mensaje']=0
    except:
        compras=1
        rut=0
    
    datos['compra']=compras
    datos['rut']=rut
    datos['persona']=persona
    
    return render (request, 'core/consultarVenta.html',datos)


def consultarBoleta(request):
    datos={

    }
    encontrado=1
    try:
        boleta=request.POST['boleta']
        try:
            compras=Producto.objects.get(boleta=boleta)
        except:
            encontrado=0
            compras=0
    except:
        boleta=0
        compras=0
    
    datos['compra']=compras
    datos['mensaje']=1
    datos['boleta']=boleta
    datos['encontrado']=encontrado
    return render (request, 'core/consultarVenta.html',datos)

def consultarSeguimiento(request):
    datos={

    }
    try:
        boleta=request.POST['boleta']
        compras=Producto.objects.get(boleta=boleta)
        try:
            rut=request.POST['rut']
            datos['rut']=rut
        except:
            rut=0
            datos['rut']=rut
    except:
        boleta=0
        compras=0
    datos['compra']=compras
    datos['mensaje']=1
    datos['boleta']=boleta
    return render (request, 'core/seguimiento.html',datos)
# Create your views here.
