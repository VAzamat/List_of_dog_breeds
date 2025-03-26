from django.urls import path
from dogs.views import DogsDetailView, DogsListView, DogsUpdateView, DogsCreateView, DogsDeleteView

from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path("",			DogsListView.as_view(), name='list'),
    path("Dogs/<int:pk>/", 	DogsDetailView.as_view(), name='detail'),
    path("Dogs/create/", 	DogsCreateView.as_view(), name='create'),
    path("Dogs/update/<int:pk>/",DogsUpdateView.as_view(), name='update'),
    path("Dogs/delete/<int:pk>/",DogsDeleteView.as_view(), name='delete'),
]