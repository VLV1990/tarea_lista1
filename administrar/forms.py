from django import forms

#Modelos que queremos validar
from .models import Tarea

class TareaForm(forms.ModelForm):
  class Meta:
    model = Tarea
    exclude = []


    