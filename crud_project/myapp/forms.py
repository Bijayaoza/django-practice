from django import forms
from .models import *

class Flora(forms.ModelForm):
    
    class Meta:
        model=User
        fields=['name','email','password']
        widgets={'password':forms.PasswordInput(attrs={'class':'form-control','palceholder':'enter your password'}),
                'name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'})}
        labels={'name':'enter your name',
                'password':'enter  your  password'}

#for user defined signing page importing from admin
from django.contrib.auth.models import User #it contain the data which are listed below in fields
from django.contrib.auth.forms import UserCreationForm


