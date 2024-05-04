from django.db import models
from .managers import CustomManager
# Create your models here.#########    look buttom also
class CommonInfo(models.Model):
    name=models.CharField(max_length=70)
    age=models.IntegerField()
    date=models.DateField()
    class Meta:
        abstract=True


class Student(CommonInfo):
    fees=models.IntegerField()
    date=None

class Teacher(CommonInfo):
    salary=models.IntegerField()

class Contactor(CommonInfo):
    date=models.DateTimeField()
    payment=models.IntegerField()
    

########################### custom manager with prox inheritance################

class ProxyStudent(Student):
    crange=CustomManager()
    class Meta:
        proxy=True