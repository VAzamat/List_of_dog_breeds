from django.contrib import admin
from dogs.models import Dogs, Breed, Parent
# Register your models here.

@admin.register(Dogs)
class DogsAdmin(admin.ModelAdmin):
    list_display = ('id','name','breed')
    list_filter = ('breed',)
    search_fields = ('name',)

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('dog','name','breed','year')
