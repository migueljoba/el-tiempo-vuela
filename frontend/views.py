import os
import random

from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from tipy import settings
from .models import Parameter, Activity


class ActivityCreateView(CreateView):
    model = Activity
    fields = '__all__'
    success_url = reverse_lazy('activity:list')


class ActivityListView(ListView):
    model = Activity
    context_object_name = 'activities'


class ActivityUpdateView(UpdateView):
    model = Activity
    fields = '__all__'
    success_url = reverse_lazy('activity:list')

class ActivityDeleteView(DeleteView):
    model = Activity
    fields = '__all__'
    success_url = reverse_lazy('activity:list')
    template_name = 'frontend/generic_confirm_delete.html'
    extra_context = {
        'form_title': 'Eliminar actividad',
        'cancel_url': success_url
    }


class ParameterCreateView(CreateView):
    model = Parameter
    fields = '__all__'
    success_url = reverse_lazy('parameters:list')


class ParameterUpdateView(UpdateView):
    model = Parameter
    fields = '__all__'
    success_url = reverse_lazy('parameters:list')


class ParameterListView(ListView):
    model = Parameter
    context_object_name = 'parameters'

class ParameterDeleteView(DeleteView):
    model = Parameter
    fields = '__all__'
    success_url = reverse_lazy('parameters:list')
    template_name = 'frontend/generic_confirm_delete.html'
    extra_context = {
        'form_title': 'Eliminar parámetro',
        'cancel_url': success_url
    }

def home(request):
    try:
        params = Parameter.objects.get(pk=1)
    except Exception as e:
        print(e)
        params = {}

    activities = Activity.objects.all()

    context_args = {
        'params': params,
        'activities': activities,
    }
    template_name = 'presentacion.html'
    return render(request, template_name, context=context_args)


def rand_media(request):
    """
    Controlador para obtener URL de archivo media aleatoriamente.
    """

    # lista de archivos en directorio media
    filename_list = os.listdir(settings.MEDIA_ROOT)

    while True:
        filename_rand = random.choice(filename_list)

        prev_url = request.session.get('filename_rand')

        if prev_url is None or prev_url != filename_rand:
            request.session['filename_rand'] = filename_rand
            break

    media_url = '{}{}'.format(settings.MEDIA_URL, filename_rand)
    return JsonResponse({'media_url': media_url})
