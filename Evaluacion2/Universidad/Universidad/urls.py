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
from Primera.views import listar_estudiantes, crear_estudiante, actualizar_estudiante, eliminar_estudiante
from Primera import views
from django.contrib import admin
app_name = 'estudiantes'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_estudiantes, name='listar_estudiantes'),
    path('crear/', crear_estudiante, name='crear_estudiante'),
    path('actualizar/<int:id>/', actualizar_estudiante, name='actualizar_estudiante'),
    path('eliminar/<int:id>/', eliminar_estudiante, name='eliminar_estudiante'),
]
