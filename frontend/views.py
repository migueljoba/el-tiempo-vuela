import os
import random

from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView

from tipy import settings
from .forms import FileFieldForm
from .models import Parameter, Activity


def handle_uploaded_file(dest_path, f):
    img_path = os.path.join(dest_path, f.name)
    with open(img_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'gallery/upload.html'
    success_url = reverse_lazy('gallery:upload')

    def post(self, request, *args, **kwargs):

        # obtener parámetros de configuración
        try:
            params = Parameter.objects.filter(active=True)[0]
        except Exception as e:
            params = Parameter()
            params.path_image_folder = 'galeria'

        # formar el path a la galería
        img_folder = params.path_image_folder
        img_gallery_path = os.path.join(settings.MEDIA_ROOT, img_folder)

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')

        if form.is_valid():
            for f in files:
                handle_uploaded_file(img_gallery_path, f)

            return self.form_valid(form)

        else:
            return self.form_invalid(form)


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
    Controlador para obtener URL de archivo dentro
    de la galería, aleatoriamente.
    """

    # obtener parámetros de configuración
    try:
        params = Parameter.objects.filter(active=True)[0]
    except Exception as e:
        params = Parameter()
        params.path_image_folder = 'galeria'

    # formar el path a la galería
    img_folder = params.path_image_folder
    img_gallery_path = os.path.join(settings.MEDIA_ROOT, img_folder)

    # lista de archivos en directorio media
    filename_list = os.listdir(img_gallery_path)

    count = len(filename_list)

    while True and count > 0:
        filename_rand = random.choice(filename_list)

        prev_url = request.session.get('filename_rand')

        if prev_url is None or prev_url != filename_rand:
            request.session['filename_rand'] = filename_rand
            break

    media_url = '{}{}'.format(settings.MEDIA_URL, os.path.join(img_folder, filename_rand))

    dict_response = {
        'count': count,
        'media_url': media_url
    }

    return JsonResponse(dict_response)
