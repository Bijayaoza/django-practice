from django.contrib import admin
from myapp.models import Student,Teacher,Contactor

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','date','fees']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['name','age','date','salary']

@admin.register(Contactor)
class ContactorAdmin(admin.ModelAdmin):
    list_display=['name','date','payment']