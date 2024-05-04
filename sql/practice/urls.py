from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.homepage,name='practice-homepage'),
    path('students/',views.studentpage,name='practice-stdpage'),
    path('studentform/',views.showFormData,name='practice-stdform'),
    path('widgetsform/',views.widgetsform,name='practice-stdform'),
    path('csrf/',views.csrf,name='practice-stdform'),
    path('sucess/',views.thankyou,name='practice-stdform'),
    path('url/<my_id>',views.myUrl,name='practice-url'),

]