from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def cart(request):
    return render(request,'myapp/cart.html')

def registration(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            print('form validated')
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            passw=fm.cleaned_data['password']
            rpassw=fm.cleaned_data['rpassword']
            print('name',name)
            print('email',email)
            print('password',passw)
            print('repassword',rpassw)
            return HttpResponseRedirect('/regi/success/')
    else:
        fm=StudentRegistration()

    return render(request,'myapp/reg.html',{'form':fm})

def thanks(request):
    am='thanks for registration'
    return render(request,'myapp/body.html',{'stri':am})