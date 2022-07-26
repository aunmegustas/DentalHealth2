from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Cita)
admin.site.register(Consultorio)
admin.site.register(Administrador)
admin.site.register(Doctor)
admin.site.register(Paciente)
admin.site.register(Rol)
admin.site.register(Clinica)
admin.site.register(Cuenta)

