from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import User
from django.db import models
import os
# Create your models here.
def user_img_path(instance, filename):
    ext = filename.split('.')[-1]
    return f'ava/{instance.user.username}.{ext}'

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    time_add = models.DateTimeField(auto_now_add=True)
    time_upd = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL  , related_name='owner', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} and owner  {self.owner.name}"


class Media(models.Model):
    img = models.ImageField(upload_to='files', null=True,blank=True)
    files = models.FileField(upload_to='files',null=True,blank=True)
    links = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=25, null=True,blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL , related_name = "media", on_delete=models.CASCADE)
    time_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}"



