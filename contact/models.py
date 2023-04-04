from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    """Класс модели обратной связи"""
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    """Класс модели контактов"""
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class About(models.Model):
    """Класс модели страницы 'О нас'"""
    text = RichTextField()  # добавляет текстовый редактор в административной панели
    mini_text = RichTextField()

    def get_first_image(self):
        """Метод для отображения первого изображения в шаблоне about.html"""
        item = self.about_images.first()
        return item.image.url

    def get_images(self):
        """Метод для итерации по всем изображениям, кроме первого, в шаблоне about.html"""
        return self.about_images.order_by('id')[1:]


class ImageAbout(models.Model):
    """Класс модели изображений на странице 'О нас'"""
    image = models.ImageField(upload_to='about/')
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_images')
    alt = models.CharField(max_length=100)  # для вывода альта в шаблоне about.html


class Social(models.Model):
    """Класс модели социальных сетей на странице 'О нас'"""
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)
    link = models.URLField()
