"""tipy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from frontend import views


url_parameters = include(([
                           path('', views.ParameterListView.as_view(), name='list'),
                           path('create', views.ParameterCreateView.as_view(), name='create'),
                           path('<int:pk>/update', views.ParameterUpdateView.as_view(), name='update'),
                           # path('<int:pk>', especialidades.EspecialidadDetailView.as_view(), name='detail'),
                           # path('<int:pk>/delete', especialidades.EspecialidadDeleteView.as_view(), name='delete'),
                       ], 'parameters'), namespace='parameters')


urlpatterns = [
    path('', views.home, name='home'),
    # path('parameters', views.ParameterCreateView.as_view(), name='parameters_create'),
    # path('parameters_list', views.ParameterListView.as_view(), name='parameters_list'),

    path('parameters/', url_parameters)
]
