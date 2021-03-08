from django import forms

from .models import Pgs


class PgsForm(forms.ModelForm):
    class Meta:
        model = Pgs
        fields = ('name', 'place', 'image')
