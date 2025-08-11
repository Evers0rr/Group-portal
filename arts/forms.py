from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    description = forms.CharField(required=False)

    class Meta:
        model = Photo
        fields = ['phote', 'description']
