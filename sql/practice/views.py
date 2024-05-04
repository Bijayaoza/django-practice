from django.shortcuts import render
from practice.models import Students 
from .forms import *
from django.http import HttpResponseRedirect


def homepage(request):
        return render(request,'practice/home.html')


def studentpage(request):
        stud =Students.objects.all()
        return render(request,'practice/student.html',{'stu': stud})

def showFormData(request):
        fm=studentRegistration(auto_id='some_%s',label_suffix='  ')#this argument "auto_id='some_%s" change the from html tag(default) into  some
        return render(request,'practice/stdRegForm.html',{'form':fm})

def widgetsform(request):
        wf=Widgetsform()
        return render(request,'practice/widgetsForm.html',{'wform':wf})

def thankyou(request):
        fs='bj you have sucessfully complete csrf'
        return render(request,'practice/csrf.html',{'csf':fs})
def csrf(request):
        if request.method =='POST':
                cf =CsrfToken(request.POST)
                if cf.is_valid():
                        print('form validated')
                        id=cf.cleaned_data['stuid']
                        name=cf.cleaned_data['stName']
                        email=cf.cleaned_data['stEmail']
                        agree=cf.cleaned_data['agree']
                        password=cf.cleaned_data['stPassword']
                        reg=Students(stName=name,stEmail=email,stPassword=password,stuid=id)
                        reg.save()
                        print('name is ',name)
                        print('email is',email)
                        print('agreed??',agree)
                        # return render(request,'practice/csrf.html',{'csf': name})
                        return HttpResponseRedirect('/reg/sucess')

        else:
                cf =CsrfToken()
                print('get method')

        return render(request,'practice/csrf.html',{'cs': cf})

def myUrl(request,my_id):
        unn={'id':my_id}
        return render(request,'practice/url.html',unn)