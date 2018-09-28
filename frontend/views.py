from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Parameter
import os, random
from tipy import settings
from django.http.response import JsonResponse
# Create your views here.

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


def home(request):

    params = Parameter.objects.get(pk=1)
    context_args = {
        'params': params
    }
    template_name = 'presentacion.html'
    return render(request, template_name, context=context_args)



def rand_media(request):
    rand_filename = random.choice(os.listdir(settings.MEDIA_ROOT))
    media_url = '{}{}'.format(settings.MEDIA_URL, rand_filename)
    return JsonResponse({'media_url': media_url})
