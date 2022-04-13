from django import forms
from django.forms import ModelForm

from .models import *


class FormComment(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter name'
            }),

            'comment': forms.TextInput(attrs={
                'class': 'form-control',
                'row': '10',
                'placeholder': 'enter your comment',
            })
        }
