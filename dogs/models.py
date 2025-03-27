from django.db import models

# Create your models here.
BLANKNULL = {'blank':True, 'null':True}

class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название породы', help_text='Введите породу собаки')
    description = models.TextField(verbose_name='Описание породы', help_text='Введите описание породы', **BLANKNULL)
    photo = models.ImageField(upload_to="breeds/photo", verbose_name='Фото породы', help_text='Загрузите фото породы',
                              **BLANKNULL)

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


class Parent(models.Model):
    dog = models.ForeignKey(Dogs, on_delete=models.SET_NULL, verbose_name='Собака',
                              help_text='Выберете собаку', related_name='parent', **BLANKNULL)
    name = models.CharField(max_length=100, verbose_name='Кличка', help_text='Введите кличку предка собаки')
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, verbose_name='Порода',
                              help_text='Введите породу предка собаки', related_name='parent_dogs', **BLANKNULL)
    year = models.PositiveIntegerField(verbose_name='Год рождения', help_text='Укажите год рождения',default=100)
    class Meta:
        verbose_name = 'Предок собаки'
        verbose_name_plural = 'Предки собаки'
