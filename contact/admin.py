from django.contrib import admin
from .models import ContactModel, ContactLink, About, Social, ImageAbout


class ImageAboutInline(admin.StackedInline):
    """
    Класс для возможности добавить изображение
    в разделе About в административной панели
     """
    model = ImageAbout
    extra = 1  # количество изображений


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'create_at']
    list_display_links = ('name',)  # поле для перехода к более подробной записи при нажатии на name


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ImageAboutInline]  # добавляем возможность добавить изображение в разделе About


admin.site.register(ContactLink)
admin.site.register(Social)
