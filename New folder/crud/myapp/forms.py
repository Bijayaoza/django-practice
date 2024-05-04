from django import forms
from .models import * 

class Registration(forms.ModelForm):
    class Meta:
        model=User
        fields= ['name','email','password']
        labels= {'name':'enter  name','email':'enter mail id','password':'enter password'}
        widgets={
                'name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter name'}),
                'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'enter email'}),
                'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter pwd'}),
                }
        
