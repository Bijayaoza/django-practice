from django.db import models

class Students(models.Model):
    stuid=models.IntegerField()
    stName=models.CharField(max_length=40)
    stEmail=models.CharField(max_length=80)
    stPassword=models.CharField(max_length=10,default='not available')

