from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    
        path('',views.homepage,name='myapp-homepage'),
        path('user/',views.user,name='myapp-homepage'),
        path('delete/<int:id>/',views.deleteData,name='myapp-delete'),
        path('sucess/',views.user,name='myapp-stdform'),
        path('update/<int:id>/',views.updateData,name='myapp-update'),

]