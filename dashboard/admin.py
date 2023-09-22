from django.contrib import admin
from . models import About, TypeWriter, Skill, Blog, Gallery

# Register your models here.
class aboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'birthday', 'image']
admin.site.register(About, aboutAdmin)

class TypeWriterAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'created_at', 'updated_at']
admin.site.register(TypeWriter, TypeWriterAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'skill', 'percent']
admin.site.register(Skill, SkillAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'description']
admin.site.register(Blog, BlogAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
admin.site.register(Gallery, GalleryAdmin)