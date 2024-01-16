from django import forms
from . import models

class DirectorForm(forms.ModelForm):
    class Meta:
        model = models.Director
        fields = "__all__"

class ProtagonistaForm(forms.ModelForm):
    class Meta:
        model = models.Protagonista
        fields = "__all__"

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = models.Pelicula
        fields = "__all__"


