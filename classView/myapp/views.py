from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse
# Create your views here.

####lets do first by function based
def home(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('thanks for submitted')
    else:
        form=ContactForm()
        return render(request,'myapp/home.html',{'form':form})
    
##### base class view example####
class ClHome(View):
    name='rohan'
    def get(self,request):
        form=ContactForm()
        return render(request,'myapp/home.html',{'form':form,'name':self.name})
    
    def post(self,request):
        form=ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('thanks for submitted')


##### let change the tempte dynamically from url### means same view function will redirect to different template through
######  different url


###here two different url accesing same function passing different template from url

def funna(request,template_name):
    template_name=template_name
    title='template reusing'
    return render(request,template_name,{'title':title})


########################## doing same things using class based view

class Cfunna(View):
    template_name=''   ###here blank_string is given, as from url.py template url location is passed #note variable name should be written mendatory
    def get(self,request):
        title='class based reusable component'
        return render(request,self.template_name,{'title':title})
