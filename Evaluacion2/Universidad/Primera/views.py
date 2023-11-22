from django.shortcuts import render, redirect
from .models import Estudiante
from .models import Ramo
from .models import Docente
from .forms import EstudianteForm
from .forms import RamoForm
from .forms import DocenteForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, CreateView

# Estudiantes
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

# Docentes
class listar_docentes(ListView):
    model = Docente
    template_name = 'templatesPrimera/listar_docentes.html'
    context_object_name = 'docentes'

class crear_docentes(CreateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'templatesPrimera/crear_docente.html'
    success_url = '/docentes/'    

class actualizar_docente(UpdateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'templatesPrimera/actualizar_docente.html'
    success_url = '/docentes/'

class eliminar_docente(DeleteView):
    model = Docente
    template_name = 'templatesPrimera/eliminar_docente.html'
    success_url = '/docentes/'

# Ramos
class listar_ramos(ListView):
    model = Ramo
    template_name = 'templatesPrimera/listar_ramos.html'
    context_object_name = 'ramos'

class crear_ramos(CreateView):
    model = Ramo
    form_class = RamoForm
    template_name = 'templatesPrimera/crear_ramo.html'
    success_url = '/ramos/'    

class actualizar_ramo(UpdateView):
    model = Ramo
    form_class = RamoForm
    template_name = 'templatesPrimera/actualizar_ramo.html'
    success_url = '/ramos/'

class eliminar_ramo(DeleteView):
    model = Ramo
    template_name = 'templatesPrimera/eliminar_ramo.html'
    success_url = '/ramos/'

# Funciones
def inicio(request):
    return render(request, 'templatesPrimera/inicio.html')

# Funciones Dstudiantes

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

# Funciones Docentes

def listar_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'templatesPrimera/listar_docentes.html', {'docentes': docentes})

def crear_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_docentes')
    else:
        form = DocenteForm()
    return render(request, 'templatesPrimera/crear_docente.html', {'form': form})

def actualizar_docente(request, id):
    docente = Docente.objects.get(id=id)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('listar_docentes')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'templatesPrimera/actualizar_docente.html', {'form': form})

def eliminar_docente(request, id):
    docente = Docente.objects.get(id=id)
    docente.delete()
    return redirect('listar_docentes')

# Funciones Ramos

def listar_ramos(request):
    ramos = Ramo.objects.all()
    return render(request, 'templatesPrimera/listar_ramos.html', {'ramos': ramos})

def crear_ramo(request):
    if request.method == 'POST':
        form = RamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ramos')
    else:
        form = RamoForm()
    return render(request, 'templatesPrimera/crear_ramo.html', {'form': form})

def actualizar_ramo(request, id):
    ramo = Ramo.objects.get(id=id)
    if request.method == 'POST':
        form = RamoForm(request.POST, instance=ramo)
        if form.is_valid():
            form.save()
            return redirect('listar_ramos')
    else:
        form = RamoForm(instance=ramo)
    return render(request, 'templatesPrimera/actualizar_ramo.html', {'form': form})

def eliminar_ramo(request, id):
    ramo = Ramo.objects.get(id=id)
    ramo.delete()
    return redirect('listar_ramos')