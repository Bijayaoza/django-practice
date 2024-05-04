from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    roll=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=40)
    marks=models.IntegerField()

    def save(self,*args,**kwargs):
        #converting name and city in lowercase before saving
        self.name=self.name.lower()
        self.city=self.city.lower()
        super().save(*args,**kwargs)


class Teacher(models.Model):
    name=models.CharField(max_length=40)
    empno=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=40)
    salary=models.IntegerField()

    def save(self,*args,**kwargs):
        #converting name and city in lowercase before saving
        self.name=self.name.lower()
        self.city=self.city.lower()
        super().save(*args,**kwargs)
