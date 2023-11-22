from django import forms
from .models import Estudiante
from .models import Docente
from .models import Ramo

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

class RamoForm(forms.ModelForm):
    class Meta:
        model = Ramo
        fields = '__all__'