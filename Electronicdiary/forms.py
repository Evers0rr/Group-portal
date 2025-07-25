from django import forms
from .models import Grade
from django.utils.timezone import now

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subjects', 'value', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            'student': 'Студент',
            'subjects': 'Предмет',
            'value': 'Оцінка',
            'date': 'Дата оцінки'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.initial.get('date') and not self.instance.pk:
            self.initial['date'] = now().date()
