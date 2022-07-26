from asyncio.windows_events import NULL
from contextlib import nullcontext
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    print(Paciente.objects.get(idcuenta_id=Cuenta.objects.get(idUser_id=request.user.id).id).id)
    idPaciente = Paciente.objects.get(idcuenta_id=Cuenta.objects.get(idUser_id=request.user.id).id).id
    context = {
        'idPaciente':idPaciente
    }
    return render(request, 'app/index.html', context)

def login(request):

    if request.method == 'POST':
        usuario = request.POST.get('username')
        contra = request.POST.get('password')

        user = authenticate(request, username=usuario, password = contra)

        if user is not None:
            login_auth(request, user)
            return redirect('/')
        else:
            print('Usuario o contraseña erroneo.')
            return redirect('/login')
            

    return render(request, 'app/Login.html', {})

def logout(request):
    logout_auth(request)
    return redirect('/login')

login_required(login_url='/login')
def doctorperfil(request):
    return render(request, 'app/DoctorPerfil.html', {})

def registro(request):
    form = CreateUserForm()
    form2 = cuentaForm()
    rol = '1'
    id = NULL
    username = NULL
    password = NULL
    
    if request.method == 'POST':
        print('metodo Post:', request.POST)
        form = CreateUserForm(request.POST)
        form2 = cuentaForm(request.POST)
        if form.is_valid():
            form.save()
            
            id = form.cleaned_data.get('id')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

        if form2.is_valid():
            form2.save()
            
            return redirect('/registrarPaciente')
			
    context = { 'form':form, 'form2':form2, 'rol':rol, 'id':id, 'username':username, 'password':password }

    return render(request, 'app/registro.html', context)

login_required(login_url='login')
def registrarPaciente(request):
    form = pacienteForm()
    
    if request.method == 'POST':
        print('metodo Post:', request.POST)
        form = pacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
			
    context = { 'form':form}
    return render(request, 'app/registrarPaciente.html', {})

@login_required(login_url='/login')
def registrarCita(request):
    form = citaForm()
    
    if request.method == 'POST':
        print('metodo Post:', request.POST)
        form = citaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
			
    context = { 'form':form }
    return render(request, 'app/RegistrarCita.html', context)

@login_required(login_url='/login')
def pacienteVerCitas(request):
    citas = Cita.objects.all()
    context = {
        'citas':citas
    }
    return render(request, 'app/PacienteVerCitas.html', context)

def pacientePerfil(request):
    form = pacienteForm()
    bandera = False

    if request.method == 'POST':
        print('metodo Post:', request.POST)
        form = pacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request, 'app/PacientePerfil.html', {'form':form,'bandera':bandera})

def doctorvercitas(request):
    return render(request, 'app/DoctorVerCitas.html', {})

def pacientecita(request):
    return render(request, 'app/PacienteCita.html', {})

# Updates
login_required(login_url='login')
def actualizarCuenta(request, pk):
    cuenta =  Cuenta.objects.get(id=pk)
    form = cuentaForm(instance= cuenta)

    if request.method == 'POST':
        form = cuentaForm(request.POST, instance= cuenta)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form} 
    return render(request, 'app/registro.html', context)

login_required(login_url='login')
def actualizarCita(request, pk):
    cita =  Cita.objects.get(id=pk)
    form = citaForm(instance=cita)

    if request.method == 'POST':
        form = citaForm(request.POST, instance= cita)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form} 
    return render(request, 'app/RegistrarCita.html', context)

#------------------ Paciente ----------------
login_required(login_url='login')
def actualizarPerfilPaciente(request, pk):
    perfilpaciente = Paciente.objects.get(id=pk)
    form = pacienteForm(instance=perfilpaciente)
    bandera = True

    if request.method == 'POST':
        form = pacienteForm(request.POST, instance= perfilpaciente)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form, 'bandera':bandera} 
    return render(request, 'app/PacientePerfil.html', context)

#Deletes
login_required(login_url='login')
def deleteCuenta(request, pk):
    cuenta =  Cuenta.objects.get(id=pk)

    if request.method == 'POST':
        cuenta.delete()
        return redirect('/')
    context = {'item':cuenta} 
    return render(request, 'app/registro.html', context)
    
login_required(login_url='login')
def deleteCita(request, pk):
    cita =  Cita.objects.get(id=pk)
    
    if request.method == 'POST':
        cita.delete()
        return redirect('/')
        
    context = {'item':cita} 
    return render(request, 'app/RegistrarCita.html', context)

login_required(login_url='login')
def deletePerfilPaciente(request, pk):
    paciente =  Paciente.objects.get(id=pk)
    
    if request.method == 'POST':
        paciente.delete()
        return redirect('/')
        
    context = {'item':paciente} 
    return render(request, 'app/PacientePerfil.html', context)