from django import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

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


# LOGIN_________________________________________________

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fieldsets = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class":"" }),
            "password": forms.PasswordInput(attrs={"class": ""}),
        }

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class":"" }),
            "password1": forms.PasswordInput(attrs={"class": ""}),
            "password2": forms.PasswordInput(attrs={"class": ""}),
        }