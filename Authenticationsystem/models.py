from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.
def user_img_path(instance, filename):
    ext = filename.split('.')[-1]
    return f'ava/{instance.user.username}.{ext}'

class Profile(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    isOpen = models.BooleanField(default=False)
    ava = models.ImageField(upload_to=user_img_path, blank=True,null=True, default="ava/default_ava.jpg")
    user = models.OneToOneField(settings.AUTH_USER_MODEL  , related_name='name' , on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True,default=' ')
    time_create = models.DateTimeField(auto_now_add=True)
    time_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class CustomUser(AbstractUser):
    def __str__(self):
        return f"{self.username}"

