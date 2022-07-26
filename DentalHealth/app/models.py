from django.db import models
from django.utils import timezone

# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.nombre

class Clinica(models.Model):
    nombre = models.CharField(max_length=45, null=False)
    direccion = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.nombre

  

class Cuenta(models.Model):
    correo = models.CharField(max_length=45, null=False)
    contraseña = models.CharField(max_length=45, null=False)
    idRol = models.ForeignKey(Rol, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.correo

class Paciente(models.Model):
    GENERO= (
        ('Femenino','F'),
        ('Masculino','M')
    )
    nombre = models.CharField(max_length=45, null=False)
    edad = models.CharField(max_length=2, null=False)
    direccion = models.CharField(max_length=45, null=False)
    genero = models.CharField(max_length=10, null=True, choices=GENERO)
    idcuenta = models.ForeignKey(Cuenta, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre
    
class Doctor(models.Model):
    nombre = models.CharField(max_length=45, null=False)
    especialidad = models.CharField(max_length=45, null=False)
    cedulaprof = models.CharField(max_length=45, null=False)
    idclinica = models.ForeignKey(Clinica, null=True, on_delete=models.SET_NULL)
    idcuenta = models.ForeignKey(Cuenta, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre

class Administrador(models.Model):
    nombre = models.CharField(max_length=45, null=False)
    telefono = models.CharField(max_length=13, null=False)
    idcuenta = models.ForeignKey(Cuenta, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre


class Consultorio(models.Model):
    numero = models.IntegerField()
    idClinica = models.ForeignKey(Clinica, null = True, on_delete = models.SET_NULL)
    idDoctor = models.ForeignKey(Doctor, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return str(self.numero)
    
class Cita(models.Model):
    idPaciente = models.ForeignKey(Paciente, null=True, on_delete=models.SET_NULL)
    idClinica = models.ForeignKey(Clinica, null=True, on_delete=models.SET_NULL)
    fecha = models.DateTimeField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    descripcion = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=12, null=True)
    idConsultorio = models.ForeignKey(Consultorio, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.descripcion
   
    
    

    