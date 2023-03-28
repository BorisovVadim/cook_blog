from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # подключаем CKEditor
    path('', include('contact.urls')),
    path('', include('blog.urls')),
]

if settings.DEBUG:  # Если DEBUG True, статику и медиа раздает Django
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
