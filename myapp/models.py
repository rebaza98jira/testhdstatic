from django.db import models

# Create your models here.

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    nacimiento = models.DateField()
    genero = models.CharField(max_length=50)
    foto = models.ImageField()

    def __str__(self):
        return '{}'.format(self.nombre)

class Album(models.Model):
    artista = models.ForeignKey(Artista, verbose_name=("artista"), on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    anio = models.SmallIntegerField()
    foto = models.ImageField()

    def __str__(self):
        return '{} -> {}'.format(self.nombre, self.artista)

class Cancion(models.Model):
    album = models.ForeignKey(Album, verbose_name=("artista"), on_delete=models.PROTECT)
    titulo = models.CharField(max_length=100)
    duracion = models.DurationField()

    def __str__(self):
        return '{} -> {}'.format(self.titulo, self.album)

