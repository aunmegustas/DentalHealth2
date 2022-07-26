from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'})
        } 

class clinicaForm(ModelForm):
    class Meta:
        model = Clinica
        fields = ['nombre','direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'})
        }

class citaForm(ModelForm):
    class Meta:
        model = Cita
        fields = ['idPaciente','idClinica','fecha','hora','descripcion','estado','idConsultorio']
        widgets = {
            'idPaciente': forms.TextInput(attrs={'class': 'form-control'}),
            'idClinica': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'invisible'}),
            'hora': forms.TextInput(attrs={'class': 'invisible'}),
            'descripcion': forms.TextInput(attrs={'class': 'invisible'}),
            'estado': forms.TextInput(attrs={'class': 'invisible'}),
            'idConsultorio': forms.TextInput(attrs={'class': 'invisible'})
        }

class cuentaForm(ModelForm):
    class Meta:
        model = Cuenta
        fields = ['idUser','idRol']
        widgets = {
            'idUser': forms.TextInput(attrs={'class': 'form-control'}),
            'idRol': forms.TextInput(attrs={'class': 'form-control'})
        }
               
class doctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'especialidad','cedulaprof']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'cedulaprof': forms.TextInput(attrs={'class': 'form-control'})

        }
        
class pacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'edad', 'genero', 'direccion'] 
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'})
        }

class consultorioForm(ModelForm):
    class Meta:
        model = Consultorio
        fields = ['numero', 'idClinica','idDoctor']
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'idClinica': forms.TextInput(attrs={'class': 'form-control'}),
            'idDoctor': forms.TextInput(attrs={'class': 'form-control'})
        }

class administradorForm(ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre', 'telefono']     
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'})
        }  