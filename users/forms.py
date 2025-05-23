from django import  forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1','password2')


class UserUpdateProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'telegram_nickname')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
