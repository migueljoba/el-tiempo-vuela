from django.db import models


class Parameter(models.Model):
    settings_name = models.CharField('Nombre', max_length=100)
    title_header = models.CharField('Título cabecera', max_length=100)
    path_image_fixed = models.CharField('Ubicación imagen fija', max_length=200)
    path_image_folder = models.CharField('Ubicacion galería', max_length=200)
    time_duration = models.PositiveSmallIntegerField('Duración de cada imagen (ms)')
    active = models.BooleanField('Activo', default=True)

class Activity(models.Model):
    order = models.PositiveIntegerField('Orden')
    description = models.CharField('Descripción', max_length=250)

    class Meta:
        ordering = ['order']