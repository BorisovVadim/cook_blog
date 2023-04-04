from django import template
from contact.models import Social, About

register = template.Library()


@register.simple_tag()
def get_social_links():
    """Функция возвращает список социальных сетей"""
    return Social.objects.all()


@register.simple_tag()
def get_about():
    """Функция возвращает последний пост модели About"""
    return About.objects.last()
