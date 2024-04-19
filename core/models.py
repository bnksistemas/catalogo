from django.db import models

# Create your models here.
# MODELO CATEGORIA

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creacion')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['name']

    def __str__(self):
        return self.name
# MODELO CATEGORIA DE PELICULAS
class Genero(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creacion')
    
    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        db_table = 'genero'
        ordering = ['name']

    def __str__(self):
        return self.name