from django import forms

from dogs.models import Dogs, Breed

class DogsForm(forms.ModelForm):
    class Meta:
        model = Dogs
        fields = '__all__'
