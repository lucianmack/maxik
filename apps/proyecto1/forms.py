from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegistroForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    correo = forms.EmailField()
    contraseña = forms.CharField(max_length=50)

class RegistroFor(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        labels = {
            
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Correo',
            'password':'Contraseña',
        }
  
   