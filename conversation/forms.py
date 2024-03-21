from django import forms
from accounts.models import User
from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content', 'sent_to')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['sent_to'].queryset = User.objects.filter(is_trainer=True)
