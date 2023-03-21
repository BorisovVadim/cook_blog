from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        """Метод для фильтрации списка постов по полю slug"""
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related(
            'category')  # Оптимизируем запрос к базе данных. С помощью related_name() получаем название категории.


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'  # определяем название объекта в шаблоне
    slug_url_kwarg = 'post_slug'


def home(request):
    return render(request, 'base.html')
