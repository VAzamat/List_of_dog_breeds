from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import  CreateView, ListView, DetailView, UpdateView, DeleteView
from dogs.models import Dogs, Breed, Parent
from dogs.forms import DogsForm, ParentForm

# Create your views here.

class DogsDetailView(DetailView):
    model = Dogs

class DogsListView(ListView):
    model = Dogs

class DogsCreateView(CreateView, LoginRequiredMixin):
    model = Dogs
    success_url = reverse_lazy('dogs:list')
    #fields = ("name", 'breed', "photo", "date_born")
    form_class = DogsForm

    def form_valid(self, form):
        dog = form.save()
        user = self.request.user
        dog.owner = user
        dog.save()
        return super().form_valid(form)

class DogsUpdateView(UpdateView):
    model = Dogs
    #fields = ("name", 'breed', "photo", "date_born")
    form_class = DogsForm
    def get_success_url(self):
        return reverse('dogs:detail', args=[self.kwargs.get('pk')] )

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ParentFormset = inlineformset_factory(Dogs, Parent, form=ParentForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ParentFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ParentFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

class DogsDeleteView(DeleteView):
    model = Dogs
    success_url = reverse_lazy('dogs:list')
