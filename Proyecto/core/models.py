from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre
    
class Protagonista(models.Model):
    nombre = models.CharField(max_length=100)
    personaje = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre
    
class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    protagonista = models.ForeignKey(Protagonista, on_delete=models.SET_NULL, null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}-{self.año}"    
    