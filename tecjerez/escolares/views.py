from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Alumno

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms 

#------------------Altas ----------------
class CrearAlumno(SuccessMessageMixin, CreateView):
    model = Alumno
    form = Alumno
    fields = "__all__"
    success_message = "Alumo AGREGADO con EXITO!!"

    def get_success_url(self):
        return reverse('listar')

#------------------ BAJAS ----------------
class EliminarAlumno(SuccessMessageMixin, DeleteView):
    model = Alumno
    form = Alumno
    fields = "__all__"

    def get_success_url(self):
        success_message = "Alumo ELIMINADO con EXITO!!"
        messages.success(self.request, success_message)
        return reverse('listar')

#------------------CAMBIOS ----------------
class ActualizarAlumno(SuccessMessageMixin, UpdateView):
    model = Alumno
    form = Alumno
    fields = "__all__"
    success_message = "Alumo MODIFICADO con EXITO!!"

    def get_success_url(self):
        return reverse('listar')

#------------------CONSULTAS ----------------
class DetalleAlumno(DetailView):
    model = Alumno

class ListarAlumnos(ListView):
    model = Alumno