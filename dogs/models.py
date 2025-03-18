from django.db import models

# Create your models here.
BLANKNULL = {'blank':True, 'null':True}

class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название породы', help_text='Введите породу собаки')
    description = models.TextField(verbose_name='Описание породы', help_text='Введите описание породы', **BLANKNULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

class Dogs(models.Model):
    name = models.CharField(max_length=100, verbose_name='Кличка', help_text='Введите кличку собаки')
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, verbose_name='Порода', help_text='Введите породу собаки', related_name='dogs', **BLANKNULL)
    photo = models.ImageField(upload_to="dogs/photo", verbose_name='Фото собаки', help_text='Загрузите фото собаки', **BLANKNULL)
    date_born = models.DateField(verbose_name='Дата рождения', help_text='Укажите дату рождения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'
        ordering = ['breed','name']

