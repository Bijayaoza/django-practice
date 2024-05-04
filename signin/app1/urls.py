from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    
        path('',views.homepage,name='app1-homepage'),
        path('signup/',views.sign,name='myapp-sign'),
        path('login/',views.user_login,name='myapp-user_login'),
        path('profile/',views.prof,name='myapp-prof'),
        path('logout/',views.user_logout,name='myapp-logout'),
        path('changepass/',views.change_pass,name='myapp-changepass')


        
]