from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("director/list", views.director_list, name="director_list"),
    path("director/form", views.director_form, name="director_form"),
    path("protagonista/list", views.protagonista_list, name="protagonista_list"),
    path("protagonista/form", views.protagonista_form, name="protagonista_form"),
    path("pelicula/list", views.pelicula_list, name="pelicula_list"),
    path("pelicula/form", views.pelicula_form, name="pelicula_form"),
]
