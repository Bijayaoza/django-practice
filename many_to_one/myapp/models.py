from django.db import models
from django.contrib.auth.models import User
# Create your models here.

####  buit in User class is used  ###

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=90)
    
    