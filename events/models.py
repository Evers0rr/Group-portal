from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
 

    def __str__(self):
        return self.title
