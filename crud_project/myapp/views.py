from django.shortcuts import render,HttpResponseRedirect
from .forms import *
from django.contrib import messages



# Create your views here.
def homepage(request):
        return render(request,'myapp/home.html')

def user(request):
        if request.method=='POST':
                fl=Flora(request.POST)  
                if fl.is_valid():
                        print('form validated')
                        # sid=fl.cleaned_data['id']
                        nm=fl.cleaned_data['name']
                        eml=fl.cleaned_data['email']
                        pas=fl.cleaned_data['password']
                        reg=User(name=nm,email=eml,password=pas)
                        reg.save()
                        messages.success(request,'your account has been created!!!')
                        fl=Flora()
                        

        else:
                fl=Flora()
                
                
        
        stud=User.objects.all()
        return render(request,'myapp/home.html',{'f':fl ,'stu':stud})


#delete function
def deleteData(request,id):
        if request.method=='POST':
                pi=User.objects.get(pk=id)
                pi.delete()
                return HttpResponseRedirect('/reg/sucess')#this one is done to remain  in a same page afer delete ,it goes to the crud url first


# update data

def updateData(request,id):
        if request.method=='POST':
                pi=User.objects.get(pk=id)
                fm=Flora(request.POST,instance=pi)
                if fm.is_valid():
                        fm.save()


                        return HttpResponseRedirect('/reg/sucess')
                       
        else:
                pi=User.objects.get(pk=id)
                fm=Flora(request.POST,instance=pi)

        return render(request,'myapp/updateStd.html',{'form':fm})