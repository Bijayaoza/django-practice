
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('practice.urls')),
    path('reg/',include('practice.urls')),
    

  


]
