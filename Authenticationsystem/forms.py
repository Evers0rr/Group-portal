from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile ,CustomUser
from django.core.exceptions import ValidationError

# from .models import CustomUser

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email",'first_name','last_name')

class ProfileEditeForm(forms.ModelForm):
    ava = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['name','last_name','first_name','description','isOpen','ava']

    def clean(self):
        ava = self.cleaned_data['ava']
        if ava is None:
            ava = 'media/ava/SkrYaro.jpg'