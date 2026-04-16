from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Alumno

from django.urls import reverse_lazy, reverse # reverse_lazy es mejor para CBV
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

#------------------ Altas ----------------
class CrearAlumno(SuccessMessageMixin, CreateView):
    model = Alumno
    # form = Alumno  <-- ELIMINA ESTA LÍNEA, causará errores
    fields = "__all__" 
    template_name = "crear.html" # Asegúrate de que Django sepa qué archivo usar
    success_message = "¡Alumno AGREGADO con ÉXITO!"

    def get_success_url(self):
        return reverse('listar')

#------------------ BAJAS ----------------
class EliminarAlumno(DeleteView): # SuccessMessageMixin no funciona igual en DeleteView por defecto
    model = Alumno
    template_name = "alumno_confirm_delete.html" # O el que prefieras

    def get_success_url(self):
        messages.success(self.request, "¡Alumno ELIMINADO con ÉXITO!")
        return reverse('listar')

#------------------ CAMBIOS ----------------
class ActualizarAlumno(SuccessMessageMixin, UpdateView):
    model = Alumno
    fields = "__all__"
    template_name = "crear.html" # Puedes reutilizar el mismo template de altas
    success_message = "¡Alumno MODIFICADO con ÉXITO!"

    def get_success_url(self):
        return reverse('listar')

#------------------ CONSULTAS ----------------
class DetalleAlumno(DetailView):
    model = Alumno
    template_name = "detalle.html"

class ListarAlumnos(ListView):
    model = Alumno
    template_name = "index.html" # Aquí es donde usas el código de la tabla que me pasaste