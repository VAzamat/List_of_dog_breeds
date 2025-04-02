from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegisterForm, UserUpdateProfileForm
from users.models import User

class RegisterView(CreateView):
    pass

class ProfileUpdateView(UpdateView):
    pass
