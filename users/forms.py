from django import  forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User

class UserRegisterForm(UserCreationForm):
    pass

class UserUpdateProfileForm(UserChangeForm):
    pass
