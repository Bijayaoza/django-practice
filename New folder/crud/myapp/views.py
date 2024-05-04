from django.shortcuts import render
from .forms import *
from .models import User
from django.http import HttpResponseRedirect 
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def reg(request):
    if request.method =='POST':
        fm=Registration(request.POST) 
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            messages.success(request,'Updated successfully!')
            return HttpResponseRedirect('/sucess/reg/')
    else:
        fm=Registration()
    
    std=User.objects.all()#its for diplaying database content

    return render(request,'myapp/home.html',{'form':fm ,'stu':std})


def delete(request,id):
    if request.method=='POST':
        fm=User.objects.get(pk=id) 
        fm.delete()
        messages.warning(request,'deleted sucessfully')
    return HttpResponseRedirect('/')

def update(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=Registration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Updated successfully!')
            

    else:#ie for get request i.e url part
        pi=User.objects.get(pk=id)
        fm=Registration(instance=pi)
    return render(request,'myapp/update.html',{'form':fm})