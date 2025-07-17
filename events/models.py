from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # ⬅️ Обов’язково додай це

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ для нових записів буде автоматично
  # ⬅️ Ось тут виправлення

    def __str__(self):
        return self.title
