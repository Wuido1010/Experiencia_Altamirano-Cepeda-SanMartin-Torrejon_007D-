from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria,  RegistroPersona


class RegistroPersonaForm(ModelForm):
    
    class Meta: 
        model= RegistroPersona
        fields=['nombre','apellido','rut','email','contraseña','conficontraseña','genero','suscripcion','direccion']


