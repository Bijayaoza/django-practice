from django.shortcuts import render,HttpResponse
from .models import *
from django.db.models import Q

# Create your views here.
def home(request):

    # student=Student.objects.all()
    

    return render(request,'myapp/home.html',{'stu':'hello'})


