"""
URL configuration for classView project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    # path('clhome/',views.ClHome.as_view(),name='classHome'),
    path('clhome/',views.ClHome.as_view(name='changed to harii'),name='classHome'),##class based url#############
    path('funna/',views.funna,{'template_name':'myapp/funna.html'},name='funna'),##funna and flora both accesing same function
    path('flora/',views.funna,{'template_name':'myapp/flora.html'},name='flora'),##but passing url dynamically from template_name

    ###for class based passing url##### note:in class based view object is passed from argument but at funct based view list is used ie key and value pair
    path('cfunna',views.Cfunna.as_view(template_name='myapp/funna.html'),name='cfunna'),
    path('cflora',views.Cfunna.as_view(template_name='myapp/flora.html'),name='cflora'),



]
