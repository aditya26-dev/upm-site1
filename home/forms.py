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

class inputFileInfo(forms.ModelForm):
    class Meta:
        model = models.baruFile
        fields = {'nama_file', 'desc_file', 'link_file', 'nama_folder'}

        '''
        widgets = {
            'nama_file' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'fileName'}),
            'desc_file' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'link_file' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'nama_folder' : forms.Select(attrs=('class': 'form-control'))
        }
        '''
