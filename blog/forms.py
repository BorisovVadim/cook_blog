from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['create_at', 'post']  # исключаем поля create_at и post для отображения в форме
