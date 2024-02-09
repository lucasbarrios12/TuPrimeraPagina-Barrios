from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import *   
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, "core/index.html")

# Director

# def director_list(request):
#     consulta = Director.objects.all()
#     contexto = {"object_list": consulta}
#     return render(request, "core/director_list.html", contexto)

class director_list(ListView):
    model = Director

# def director_form(request):
#     if request.method == "POST":
#         form = forms.DirectorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(director_list)
#     else:
#         form = forms.DirectorForm()
#     return render(request, "core/director_form.html", {"form": form})

class director_form(LoginRequiredMixin, CreateView):
    model = Director
    form_class = DirectorForm
    success_url = reverse_lazy('core/director_list.html')

class directorUpdate(LoginRequiredMixin, UpdateView):
    model = Director
    form_class = DirectorForm
    success_url = reverse_lazy('core/director_list.html')

class directorDelete(LoginRequiredMixin, DeleteView):
    model = Director
    success_url = reverse_lazy('core/director_list')

# Protagonista

# def protagonista_list(request):
#     consulta = models.Protagonista.objects.all()
#     contexto = {"protagonistas": consulta}
#     return render(request, "core/protagonista_list.html", contexto)
class protagonista_list(ListView):
    model = Protagonista


# def protagonista_form(request):
#     if request.method == "POST":
#         form = forms.ProtagonistaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(protagonista_list)
#     else:
#         form = forms.ProtagonistaForm()
#     return render(request, "core/protagonista_form.html", {"form": form})
    
class protagonista_form(LoginRequiredMixin, CreateView):
    model = Protagonista
    form_class = ProtagonistaForm
    success_url = reverse_lazy('core/protagonista_list')

class protagonistaUpdate(LoginRequiredMixin, UpdateView):
    model = Protagonista
    form_class = ProtagonistaForm
    success_url = reverse_lazy('core/protagonista_list')

class protagonistaDelete(LoginRequiredMixin, DeleteView):
    model = Protagonista
    success_url = reverse_lazy('core/protagonista_list')

# Pelicula

# def pelicula_list(request):
#     consulta = models.Pelicula.objects.all()
#     contexto = {"peliculas": consulta}
#     return render(request, "core/pelicula_list.html", contexto)

class pelicula_list(ListView):
    model = Pelicula

# def pelicula_form(request):
#     if request.method == "POST":
#         form = forms.PeliculaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(pelicula_list)
#     else:
#         form = forms.PeliculaForm()
#     return render(request, "core/pelicula_form.html", {"form": form})

class pelicula_form(LoginRequiredMixin, CreateView):
    model = Pelicula
    form_class = PeliculaForm
    success_url = reverse_lazy('core/pelicula_list')


class peliculaUpdate(LoginRequiredMixin, UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    success_url = reverse_lazy('core/pelicula_list')

class peliculaDelete(LoginRequiredMixin, DeleteView):
    model = Pelicula
    success_url = reverse_lazy('pelicula_list')

class peliculaDetail(DetailView):
    model = Pelicula


# LOGIN--------------------------

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'

def register(request):
    if request.method == "POST":
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core/index")
    else:
        form = CustomCreationForm()
    return render(request, "core/register.html", {"form": form})

# class panel(ListView):
#     model = Director.objects.all()
#     model = Protagonista.objects.all()
#     model = Pelicula.objects.all()
#     template_name = 'core/panel.html'


# panel-------------------------

def panel(request):
    directores = Director.objects.all()
    protagonistas = Protagonista.objects.all()
    peliculas = Pelicula.objects.all()
    return render(request,'core/panel.html',
    {'directores':directores, 'protagonistas': protagonistas, 'peliculas': peliculas})