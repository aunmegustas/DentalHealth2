from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'app/index.html', {})

def login(request):
    return render(request, 'app/Login.html', {})

def registrarCita(request):
    

    return render(request, 'app/RegistrarCita.html', {})

def doctorperfil(request):
    return render(request, 'app/DoctorPerfil.html', {})

def registro(request):
    form = cuentaForm()
    rol = '1'
    if request.method == 'POST':
        print('metodo Post:', request.POST)
        form = cuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
			
    context = { 'form':form, 'rol':rol }

    return render(request, 'app/registro.html', context)

def registrarPaciente(request):
    return render(request, 'app/registrarPaciente.html', {})

def registrarCita(request):
    return render(request, 'app/RegistrarCita.html', {})

def pacienteVerCitas(request):
    citas = Cita.objects.all()
    context = {
        'citas':citas
    }
    return render(request, 'app/PacienteVerCitas.html', context)

def pacientePerfil(request):
    return render(request, 'app/PacientePerfil.html', {})

def doctorvercitas(request):
    return render(request, 'app/DoctorVerCitas.html', {})

def pacientecita(request):
    return render(request, 'app/PacienteCita.html', {})

