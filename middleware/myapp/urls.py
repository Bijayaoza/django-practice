from . import views
from django.urls import path 

urlpatterns=[
path('', views.home,name="home"),
path('data/', views.data,name="hom"),
]