from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class RecipeInline(admin.StackedInline):
    """Класс для возможности добавить создание рецепта в админке в постах"""
    model = models.Recipe
    extra = 1  # количество рецептов


class PostAdmin(admin.ModelAdmin):
    """Класс для отображения указанных полей в админке в постах"""
    list_display = ['title', 'category', 'author', 'create_at', 'id']
    inlines = [RecipeInline]  # добавляем возможность создания рецепта в посте


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Класс для отображения указанных полей в админке в рецептах"""
    list_display = ['name', 'prep_time', 'cook_time', 'post']


admin.site.register(models.Category, MPTTModelAdmin)  # для отображения вложенности категорий в админке
admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)
# admin.site.register(models.Recipe)
# Используем декоратор @admin.register(models.Recipe) в классе RecipeAdmin вместо регистра выше
admin.site.register(models.Comment)
