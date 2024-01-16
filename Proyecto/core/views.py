from django.shortcuts import redirect, render
from . import models
from . import forms


def index(request):
    return render(request, "core/index.html")

# Director

def director_list(request):
    consulta = models.Director.objects.all()
    contexto = {"directores": consulta}
    return render(request, "core/director_list.html", contexto)

def director_form(request):
    if request.method == "POST":
        form = forms.DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(director_list)
    else:
        form = forms.DirectorForm()
    return render(request, "core/director_form.html", {"form": form})

# Protagonista

def protagonista_list(request):
    consulta = models.Protagonista.objects.all()
    contexto = {"protagonistas": consulta}
    return render(request, "core/protagonista_list.html", contexto)

def protagonista_form(request):
    if request.method == "POST":
        form = forms.ProtagonistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(protagonista_list)
    else:
        form = forms.ProtagonistaForm()
    return render(request, "core/protagonista_form.html", {"form": form})

# Pelicula

def pelicula_list(request):
    consulta = models.Pelicula.objects.all()
    contexto = {"peliculas": consulta}
    return render(request, "core/pelicula_list.html", contexto)

def pelicula_form(request):
    if request.method == "POST":
        form = forms.PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(pelicula_list)
    else:
        form = forms.PeliculaForm()
    return render(request, "core/pelicula_form.html", {"form": form})
