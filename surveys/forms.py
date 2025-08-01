from django import forms
from .models import SurveyAnswer, SurveyQuestion

class SurveyAnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        choices = [(answer.pk, answer.text) for answer in question.answers.all()]
        self.fields['answer'] = forms.ChoiceField(
            label=question.text,
            choices=choices,
            widget=forms.RadioSelect,
            required=True
        )
