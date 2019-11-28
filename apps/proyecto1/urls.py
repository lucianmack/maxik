from django.contrib import admin
from django.urls import path
from .views import home,quienessomos,contactenos,micuenta,registro,misordenes


urlpatterns = [
    path('', home, name='index'),
    path('quienessomos.html/', quienessomos, name='Quienes'),
    path('contactenos.html/', contactenos, name='Contacto'),
    path('micuenta.html/', micuenta, name='Cuenta'),
    path('registro.html/',registro, name='registro'),
    path('misordenes.html/',misordenes, name='ordenes'),
]

