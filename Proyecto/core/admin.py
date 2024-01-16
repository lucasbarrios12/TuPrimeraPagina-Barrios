from django.contrib import admin

from . import models

admin.site.register(models.Director)
admin.site.register(models.Pelicula)
admin.site.register(models.Protagonista)