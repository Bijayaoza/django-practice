from . import views
from django.urls import path 

urlpatterns=[
path('', views.home,name="home"),
path('cart',views.cart,name='cart'),
path('registration/',views.registration,name='registration'),
path('success/',views.thanks,name='sucess'),
]
