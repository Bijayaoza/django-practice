# from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class signupform(UserCreationForm):
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']#name haru yehi format ma hunu porxa yo direct  libary batw imort garya ho so..
        label={'email':'Email'}