"""
URL configuration for Universidad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Primera.views import listar_estudiantes, crear_estudiante, actualizar_estudiante,inicio, eliminar_estudiante, listar_docentes, crear_docente, actualizar_docente, eliminar_docente, listar_ramos, eliminar_ramo, actualizar_ramo, crear_ramo
from django.contrib import admin


app_name = 'estudiantes'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),


    path('estudiantes/', listar_estudiantes, name='listar_estudiantes'),
    path('crear/', crear_estudiante, name='crear_estudiante'),
    path('actualizar/<int:id>/', actualizar_estudiante, name='actualizar_estudiante'),
    path('eliminar/<int:id>/', eliminar_estudiante, name='eliminar_estudiante'),


    path('docentes/', listar_docentes, name='listar_docentes'),
    path('docentes/crear/', crear_docente, name='crear_docente'),
    path('docentes/actualizar/<int:id>/', actualizar_docente, name='actualizar_docente'),
    path('docentes/eliminar/<int:id>/', eliminar_docente, name='eliminar_docente'),
    
    path('ramos/', listar_ramos, name='listar_ramos'),
    path('ramos/crear/', crear_ramo, name='crear_ramo'),
    path('ramos/actualizar/<int:id>/', actualizar_ramo, name='actualizar_ramo'),
    path('ramos/eliminar/<int:id>/', eliminar_ramo, name='eliminar_ramo')
]