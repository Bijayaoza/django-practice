from django.db import models
from django.contrib.auth.models import User
# Create your models here.

####  buit in User class is used  ###

class Page(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    # user=models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    # user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,limit_choices_to={'is_staff':True})


    #### here User is an built in class ## CASCADE, is an mode of delete ie in case of CASCADE if creator_user is  deleted then the page will als0 delete ## 
    ## user is an variable used to denote which class is relation with we can used any name tho

    page_name=models.CharField(max_length=70)
    page_cat=models.CharField(max_length=70)
    page_published_date=models.DateField()


#### let us do  by using inheritance concept#######
class Likes(Page):
    paggge=models.OneToOneField(Page,on_delete=models.CASCADE,primary_key=True,parent_link=True)
    like=models.IntegerField()
