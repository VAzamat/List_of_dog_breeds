from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import  CreateView, ListView, DetailView, UpdateView, DeleteView
from dogs.models import Dogs, Breed


# Create your views here.

class DogsDetailView(DetailView):
    model = Dogs

class DogsListView(ListView):
    model = Dogs

class DogsCreateView(CreateView):
    model = Dogs
    fields = ("name", 'breed', "photo", "date_born")
    success_url = reverse_lazy('dogs:list')

class DogsUpdateView(UpdateView):
    model = Dogs
    fields = ("name", 'breed', "photo", "date_born")
    def get_success_url(self):
        return reverse('dogs:detail', args=[self.kwargs.get('pk')] )

class DogsDeleteView(DeleteView):
    model = Dogs
    success_url = reverse_lazy('dogs:list')


