from django import forms
from . import models


class CustomUserLogin(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = {'email', 'password'}

        '''
        widgets = {
            'email' : forms.EmailInput(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'password' : forms.EmailInput(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
        }
        '''

        