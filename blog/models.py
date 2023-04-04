from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    Модель объявляет поле parent для модели Category,
    которое является внешним ключом и ссылается сам на себя.
    Каждая категория может иметь только одного родителя,
    который также должен быть категорией.
    """

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, default='', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Метод для построения пути к посту в шаблоне"""
        return reverse('post_single', kwargs={'slug': self.category.slug, 'post_slug': self.slug})

    def get_recipes(self):
        """Метод для итерации по всем рецептам в шаблоне post_detail.html"""
        return self.recipes.all()


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = RichTextField()
    directions = RichTextField()
    post = models.ForeignKey(
        Post,
        related_name='recipes',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
