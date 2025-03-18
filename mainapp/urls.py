from django.urls import path
from mainapp.views import home

from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", home, name='home'),
]

