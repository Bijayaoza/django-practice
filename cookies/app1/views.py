from django.shortcuts import render ,HttpResponseRedirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def homepage(request):
        return render(request,'app1/home.html')

def sign(request):
        if request.method=='POST':
                fm=signupform(request.POST)
                if fm.is_valid():
                        fm.save()
                        messages.success(request,'account created sucessfully')
        
        else:
                fm=signupform()

        return render(request,'app1/signup.html',{'form':fm})

#login form

def user_login(request):
    if not request.user.is_authenticated:#yedi login vaisakya xa vaNE feri login ma jaNA NASAKOS vanera ho ,yedi login garisakya xa vane feri login  ma jana khojda auto  profile ma reload 
        if request.method=="POST":
                fm=AuthenticationForm(request=request ,data=request.POST)
                if fm.is_valid():
                        uname=fm.cleaned_data['username']
                        upass=fm.cleaned_data['password']
                        User=authenticate(username=uname,password=upass)
                        if User is not None:#yedi user  ko user  name ra password mily0 vane user  ma hal ani login ma request gar
                                login(request,User)
                                return HttpResponseRedirect('/profile/')

        else:
                fm=AuthenticationForm()
        
        return render(request,'app1/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
           
           
# profile page after login

def prof(request):
        if request.user.is_authenticated:#yo chai direct url batw access nagaros vanera check garya ho
                return render(request,'app1/profile.html')
        else:
                return HttpResponseRedirect('/login/')

# logout after login

def user_logout(request):
        logout(request)
        return HttpResponseRedirect('/login/')

def change_pass(request):
        if request.user.is_authenticated:
                if request.method=='POST':
                        fm=PasswordChangeForm(user=request.user,data=request.POST)
                        if fm.is_valid():
                                fm.save()
                                messages.success(request,'password change sucessfully')
                                return HttpResponseRedirect('/login/')
                else:
                        fm=PasswordChangeForm(user=request.user)
                        messages.info(request,'enter old and new password')
        else:
               return HttpResponseRedirect('/login/')
        return render(request,'app1/pass_change.html',{'form':fm})