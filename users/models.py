from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

NULLABLE = {'null':True, 'blank': True}

class User(AbstractUser):
    username = None

    phone = PhoneNumberField( verbose_name='телефон', help_text='Введите телефон пользователя', **NULLABLE)
    telegram_nickname = models.CharField(max_length=60, verbose_name='Ник в Telegram', help_text='Введите никнейм в Telegram', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Фотография пользователя', help_text='Выберете и загрузите фотографию для профиля пользователя')
    email = models.EmailField(unique=True, verbose_name='почта', help_text='Почта пользователя как уникальное поле регистрации')

    token = models.CharField(max_length=100, verbose_name="проверочный код для подтверждения пользователя", **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
