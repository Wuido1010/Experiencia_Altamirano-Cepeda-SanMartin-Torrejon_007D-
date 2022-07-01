from django.urls import path
from .views import  form_persona, forms_venta, home, inicio, formulario2, GaleriaDeFotos, quienesSomos, forms_persona, mostrar, form_mod_persona, nose, home2, loginRegistro, login, editarRegistro, form_persona, consultarRegistro, forms_venta, proceso_Venta, ventas_completado, loginConsultarVenta, consultarCompra, consultarBoleta, consultarSeguimiento
urlpatterns = [
    path('home',home,name="home"),
    path('ini',inicio,name="ini"),
    path('', nose, name="nose"),
    path('form2', formulario2,name="form2"),
    path('Galeria', GaleriaDeFotos,name="Galeria"),
    path('quienes', quienesSomos,name="quienes"),
    path('mostrar2', mostrar,name="mostrar2"),
    path('forms-persona', forms_persona, name="forms-persona"),
    path('form_mod_persona/<id>', form_mod_persona, name="form_mod_persona"),
    path('home2', home2, name="home2"),
    path('loginRegistro', loginRegistro, name="loginRegistro"),
    path('login', login, name="login"),
    path('editarRegistro', editarRegistro, name="editarRegistro"),
    path('form_persona', form_persona, name="form_persona"),
    path('consultarRegistro', consultarRegistro, name="consultarRegistro"),
    path('forms_venta', forms_venta, name="forms_venta"),
    path('proceso_Venta', proceso_Venta, name="proceso_Venta"),
    path('ventas_completado', ventas_completado, name="ventas_completado"),
    path('loginVenta', loginConsultarVenta, name="loginVenta"),
    path('consultarVenta/<id>', consultarCompra, name="consultarVenta"),
    path('consultarBoleta', consultarBoleta, name="consultarBoleta"),
    path('consultarSeguimiento', consultarSeguimiento, name="consultarSeguimiento"),
    
    
    
    
    
]