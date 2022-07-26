from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login', views.login),
    path('logout', views.logout),
    path('registrarCita', views.registrarCita),
    path('doctorperfil', views.doctorperfil),
    path('doctorvercitas', views.doctorvercitas),
    path('pacientecita', views.pacientecita),
    path('registro', views.registro),
    path('registrarPaciente', views.registrarPaciente),
    path('registrarCita', views.registrarCita),
    path('pacienteVerCitas', views.pacienteVerCitas),
    path('pacientePerfil', views.pacientePerfil),
    path('actualizarperfilpaciente/<str:pk>/', views.actualizarPerfilPaciente, name="pacientePerfil")
    
]