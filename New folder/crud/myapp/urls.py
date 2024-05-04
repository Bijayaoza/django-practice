from django.urls import path
from . import views

urlpatterns = [
    path('',views.reg,name='homepage'), 
    path('reg/',views.reg,name='registration'),   
    path('delete/<int:id>/',views.delete,name="deleteid"),
    path('<int:id>/',views.update,name="update"),
]
