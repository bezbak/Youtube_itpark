from django.db import models

# Create your models here.
class Videos(models.Model):
    title = models.CharField(
        'Загаловок',
        max_length=255
    )
    description = models.TextField(
        'Описание',
        max_length=1500
    )
    poster = models.ImageField(
        upload_to='poster/'
    )
    video = models.FileField(
        upload_to='video_file/'
    )
    channel = models.CharField(
        max_length=255
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'