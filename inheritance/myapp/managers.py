from django.db import models

class CustomManager(models.Manager):
    def get_age_range(self,r1,r2):###user define object
        return super().get_queryset().filter(age__range=(r1,r2))###using lookup range is calculated from model roll
    
    ###.get_queryset id builtin function in custom manager ie wher we call .get.all we call this function
    #super() call the root of all manager function
    ## _ _range is an lookup built in function