from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

#Да це якийсь титан  
class Material(models.Model):
    MATERIAL_TYPES = [
        ('file', 'Файл'),
        ('image', 'Зображення'),
        ('youtube', 'YouTube відео'),
        ('link', 'Зовнішнє посилання'),
    ]

    title = models.CharField(max_length=255, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name="Опис")
    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPES, verbose_name="Тип матеріалу")

    file = models.FileField(upload_to='materials/', blank=True, null=True, verbose_name="Файл")
    image = models.ImageField(upload_to='materials/images/', blank=True, null=True, verbose_name="Зображення")
    youtube_url = models.URLField(blank=True, null=True, verbose_name="YouTube URL")
    external_link = models.URLField(blank=True, null=True, verbose_name="Зовнішнє посилання")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='materials', verbose_name="Створено користувачем")

    class Meta:
        verbose_name = "Матеріал"
        verbose_name_plural = "Матеріали"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def is_youtube(self):
        return self.material_type == 'youtube'
    
    def is_file(self):
        return self.material_type == 'file'
    
    def is_image(self):
        return self.material_type == 'image'

    def is_link(self):
        return self.material_type == 'link'

    
        
    
        
    
        

        

    

    



