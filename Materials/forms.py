from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'description', 'material_type', 'file', 'image', 'youtube_url', 'external_link']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'file': forms.ClearableFileInput(attrs={'multiple': False}),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }
        labels = {
            'title': 'Назва',
            'description': 'Опис',
            'material_type': 'Тип матеріалу',
            'file': 'Файл',
            'image': 'Зображення',
            'youtube_url': 'YouTube URL',
            'external_link': 'Зовнішнє посилання'
        }

    def clean(self):
        cleaned_data = super().clean()
        material_type = cleaned_data.get('material_type')

        if material_type == 'file' and not cleaned_data.get('file'):
            self.add_error('file', "Необхідно завантажити файл.")
        if material_type == 'image' and not cleaned_data.get('image'):
            self.add_error('image', "Необхідно завантажити зображення.")
        if material_type == 'youtube' and not cleaned_data.get('youtube_url'):
            self.add_error('youtube_url', "Необхідно вказати посилання на YouTube.")
        if material_type == 'link' and not cleaned_data.get('external_link'):
            self.add_error('external_link', "Необхідно вказати зовнішнє посилання.")
