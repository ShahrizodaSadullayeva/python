from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter last_name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter email'
            }),

            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter password',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter password again'
            }),


        }
