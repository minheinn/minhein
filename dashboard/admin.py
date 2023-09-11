from django.contrib import admin
from . models import About, TypeWriter

# Register your models here.
class aboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'birthday']
admin.site.register(About, aboutAdmin)

class TypeWriterAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'created_at', 'updated_at']
admin.site.register(TypeWriter, TypeWriterAdmin)