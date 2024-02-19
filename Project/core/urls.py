from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("director/list", director_list.as_view(), name="director_list"),
    path("director/form", director_form.as_view(), name="director_form"),
    path("protagonista/list", protagonista_list.as_view(), name="protagonista_list"),
    path("protagonista/form", protagonista_form.as_view(), name="protagonista_form"),
    path("pelicula/list", pelicula_list.as_view(), name="pelicula_list"),
    path("pelicula/form", pelicula_form.as_view(), name="pelicula_form"),
    # director
    path("director/update/<int:pk>", directorUpdate.as_view(), name="directorUpdate"),
    path("director/delete/<int:pk>", directorDelete.as_view(), name="directorDelete"),
    # protagonista
    path("protagonista/update/<int:pk>", protagonistaUpdate.as_view(), name="protagonistaUpdate"),
    path("protagonista/delete/<int:pk>", protagonistaDelete.as_view(), name="protagonistaDelete"),
    # pelicula
    path("pelicula/update/<int:pk>", peliculaUpdate.as_view(), name="peliculaUpdate"),
    path("pelicula/delete/<int:pk>", peliculaDelete.as_view(), name="peliculaDelete"),
    path("pelicula/detail/<int:pk>", peliculaDetail.as_view(), name="peliculaDetail"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("panel/", panel, name="panel"),





]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)