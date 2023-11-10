from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Definiciones de las vistas
class listar_estudiantes(ListView):
    model = Estudiante
    template_name = 'templatesPrimera/listar_estudiantes.html'
    context_object_name = 'estudiantes'

class crear_estudiante(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'templatesPrimera/crear_estudiante.html'
    success_url = '/estudiantes/'

class actualizar_estudiante(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'templatesPrimera/actualizar_estudiante.html'
    success_url = '/estudiantes/'

class eliminar_estudiante(DeleteView):
    model = Estudiante
    template_name = 'templatesPrimera/eliminar_estudiante.html'
    success_url = '/estudiantes/'

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'templatesPrimera/listar_estudiantes.html', {'estudiantes': estudiantes})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'templatesPrimera/crear_estudiante.html', {'form': form})

def actualizar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'templatesPrimera/actualizar_estudiante.html', {'form': form})

def eliminar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect('listar_estudiantes')
