from django.core.exceptions import ValidationError
from django import forms
from django.utils import timezone

from .models import  Project, Media

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description']


class MedaiAddForm(forms.ModelForm):
    img = forms.ImageField(required=False)
    files = forms.FileField(required=False)
    links = forms.URLField(required=False)
    description = forms.CharField(required=False , max_length=25 )

    class Meta:
        model = Media
        fields = ["img",'files','links','description']

