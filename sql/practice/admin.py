from django.contrib import admin

# Register your models here.
from .models import Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display=('id','stuid','stName','stEmail','stPassword')

#admin.site.register(Students,StudentsAdmin)
