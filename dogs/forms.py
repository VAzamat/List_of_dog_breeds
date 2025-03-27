from django import forms
from django.forms import BooleanField

from dogs.models import Dogs, Breed, Parent

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control text-start'

class DogsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Dogs
        fields = '__all__'

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
