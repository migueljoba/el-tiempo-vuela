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
from django.urls import path, include
from frontend import views

url_parameters = include(([
                              path('', views.ParameterListView.as_view(), name='list'),
                              path('create', views.ParameterCreateView.as_view(), name='create'),
                              path('<int:pk>/update', views.ParameterUpdateView.as_view(), name='update'),
                              path('<int:pk>/delete', views.ParameterDeleteView.as_view(), name='delete'),
                          ], 'parameters'), namespace='parameters')

url_activities = include(([
                              path('', views.ActivityListView.as_view(), name='list'),
                              path('create', views.ActivityCreateView.as_view(), name='create'),
                              path('<int:pk>/update', views.ActivityUpdateView.as_view(), name='update'),
                              path('<int:pk>/delete', views.ActivityDeleteView.as_view(), name='delete'),
                          ], 'activity'), namespace='activity')

urlpatterns = [
    path('', views.home, name='home'),
    path('rand_filename', views.rand_media, name='rand_media'),
    path('parameters/', url_parameters),
    path('activities/', url_activities),
]
