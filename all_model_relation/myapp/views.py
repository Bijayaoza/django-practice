from django.shortcuts import render
from .models import Page,Post,Song,User
# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def user(request):
    data1=User.objects.all()
    data2=User.objects.filter()
    data3=User.objects.filter(page__page_name='programming')### here from parent User child class of model data is used 
    ### page is child class name of model, ### looks  up(- -) is used to acces child data(page_name) 
    data4=User.objects.filter(page__page_publish_date='2023-23-11')
    data5=User.objects.filter(post__post_title='hero')
    data6=User.objects.filter(song__songname='birthday')
    return render(request,'myapp/user.html',{'data1':data1},
    {'data2':data2},{'data3':data3},{'data4':data4},
    {'data5':data5},{'data6':data6})



def page(request):
    
    return render()

def post(request):
    return render()

def song(request):
    return render()

