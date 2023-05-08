from django.contrib import admin
from django.urls import path
from videos.views import index, post_detail, season, series
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('post_detail/<int:id>/', post_detail, name='post_detail'),
    path('season/<int:id>/', season, name='season'),
    path('series/<int:id>/', series, name='series'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)