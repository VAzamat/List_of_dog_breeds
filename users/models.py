from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null':True, 'blank': True}

class User(AbstractUser):
    username = None

    phone = models.CharField(max_length=35, verbose_name='телефон', help_text='Введите телефон пользователя', **NULLABLE)
    telegram_nickname = models.CharField(max_length=60, verbose_name='Ник в Telegram', help_text='Введите никнейм в Telegram', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Фотография пользователя', help_text='Выберете и загрузите фотографию для профиля пользователя')
    email = models.EmailField(unique=True, verbose_name='почта', help_text='Почта пользователя как уникальное поле регистрации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
