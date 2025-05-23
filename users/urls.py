from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.views import RegisterView, ProfileUpdateView, email_verification

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("",         LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/",  LogoutView.as_view(), name='logout'),
    path("register/", RegisterView.as_view(), name='register'),
    path("updateprofile/", ProfileUpdateView.as_view(), name='profile'),
    path("email-confirm/<str:token>/", email_verification, name='email-confirm'),
]
