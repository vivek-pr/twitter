from django.contrib import admin
from django.contrib.auth.models import User



class UserAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','password']


