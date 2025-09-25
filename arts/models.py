from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from Authenticationsystem.models import Profile
# Create your models here.
def user_img_path(instance, filename):
    ext = filename.split('.')[-1]
    return f'photos/{instance.owner.user.username}.{ext}'

class Photo(models.Model):
    photo = models.ImageField(upload_to=user_img_path, blank=True,null=True)
    description = models.TextField(null=True, blank=True)
    is_applied = models.BooleanField(default=False)
    owner = models.ForeignKey(Profile, related_name='media_owner',on_delete=models.CASCADE)



