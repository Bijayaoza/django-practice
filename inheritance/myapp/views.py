from django.shortcuts import render
from .models import *
# from django.db.models import Q

# Create your views here.
def home(request):

    # student=Student.objects.all()

    student=ProxyStudent.crange.get_age_range(10,80)###crange is custom manager def inside porxy inheritance get_age_range is custom manager def inside manager.py
    

    return render(request,'myapp/home.html',{'stu':student})
