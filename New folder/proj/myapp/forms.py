from django import forms


class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='password again' ,label_suffix='', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        valpwd= self.cleaned_data['password']
        rvalpwd= self.cleaned_data['rpassword']
        if valpwd != rvalpwd:
            raise forms.ValidationError('password not matched')
    
