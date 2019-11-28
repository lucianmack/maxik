from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from apps.proyecto1.forms import RegistroForm
from django.contrib.auth import login as do_login

# Create your views here.
def home (request):
    return render(request,"proyecto1/index.html")

def quienessomos (request):
    return render(request,"proyecto1/quienessomos.html")

def contactenos (request):
    return render(request,"proyecto1/contactenos.html")

def micuenta (request):
    return render(request,"proyecto1/micuenta.html")
    
def registro (request):
    return render(request,"proyecto1/registro.html")

def misordenes (request):
    return render(request,"proyecto1/misordenes.html")

class RegistroUsuario(CreateView):
    model = User
    template_name = "proyecto1/micuenta.html"
    form_class = RegistroForm
   
