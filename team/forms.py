from django import forms

from .models import *

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        exclude = ()