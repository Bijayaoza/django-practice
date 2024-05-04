from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def home(request):
    print('i am view')
    return HttpResponse('THIS IS HOME')

def data(request):
    print("this is  view name=hatti.." )
    context={'name':'hatti'}
    return TemplateResponse(request,'myapp/cart.html',context)