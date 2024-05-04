from django import forms
from .models import Students

class studentRegistration(forms.Form):
    name=forms.CharField(label="your name")
    email=forms.EmailField()

class Widgetsform(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    hints=forms.CharField(widget=forms.HiddenInput,initial='the password id test321')
    checkbox=forms.CharField(widget=forms.CheckboxInput)
    file_input=forms.CharField(widget=forms.FileInput)
    text=forms.CharField(widget=forms.TextInput(attrs={'class':'flora','id':'funna'}))

# class CsrfToken(forms.Form):
#     stuid=forms.IntegerField()
#     name=forms.CharField(min_length=2,max_length=5,error_messages={'required':'enter your  name'})
#     email=forms.EmailField()
#     password=forms.CharField(widget=forms.PasswordInput)
#     agree=forms.BooleanField(label_suffix="  ",label='I agree')

class CsrfToken(forms.ModelForm):
    agree=forms.BooleanField(label_suffix="  ",label='I agree')#yo model(database) ma xaina so...
    class Meta:
        model=Students
        fields=['stuid','stName','stEmail','stPassword']
        Widgets={'stPassword':forms.PasswordInput,
                'stName':forms.TextInput(attrs={'class':'Name','palceholder':'enter your name'})},
        labels={'stName':'enter your name',
                'stPassword':'enter  your  password'}

