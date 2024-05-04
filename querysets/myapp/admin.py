from django.contrib import admin
from myapp.models import Student,Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll','city','marks']


@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','empno','city','salary']