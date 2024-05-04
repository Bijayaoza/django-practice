from django.contrib import admin
from myapp.models import Page,Likes

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['page_name','page_cat','page_published_date','user']


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display=['like','page_name','page_cat','page_published_date','user']


