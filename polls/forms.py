from django import forms
from .models import PollOption

class PollVoteForm(forms.Form):
    option = forms.ChoiceField(widget=forms.RadioSelect)

    def __init__(self, poll, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = [(option.pk, option.text) for option in poll.options.all()]
        self.fields['option'].choices = choices
        self.fields['option'].label = poll.title
