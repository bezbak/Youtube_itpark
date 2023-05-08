from django.db import models

# Create your models here.

class Serial(models.Model):
    name = models.CharField(
        max_length=55
    )
    original_name = models.CharField(
        max_length=55
    )
    description = models.CharField(
        max_length=500
    )
    poster = models.ImageField(
        upload_to='serial_poster'
    )
    date_of_created = models.DateField(
        auto_now_add=False
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'
    
class Season(models.Model):
    name = models.CharField(
         max_length=2
    )
    serial = models.ForeignKey(
        Serial,
        related_name='serial',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'
    
    
class Series(models.Model):
    name = models.CharField(
        max_length=100
    )
    video = models.FileField(
        upload_to='series_files/'
    )
    season = models.ForeignKey(
        Season,
        related_name='season',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=False
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'