from django.urls import path
from cliente_app import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarCliente/",views.registrarCliente,name="registrarCliente"),
    path("seleccionarCliente/<codigo>",views.seleccionarCliente,name="seleccionarCliente"),
    path("editarCliente/",views.editarCliente,name="editarCliente"),
    path("borrarCliente/<codigo>",views.borrarCliente,name="borrarCliente"),
    
]
