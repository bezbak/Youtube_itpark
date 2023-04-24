from django.contrib import admin
from django.urls import path
from videos.views import index, about_us
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about_us/', about_us),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)