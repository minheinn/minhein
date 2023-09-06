from django.contrib import admin
from . models import About

# Register your models here.
class aboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'birthday']
admin.site.register(About, aboutAdmin)