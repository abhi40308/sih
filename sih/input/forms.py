from django import forms

from .models import Input

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Input