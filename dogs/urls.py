from django.urls import path
#from dogs.views import home

from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
#    path("", home, name='index'),
]
