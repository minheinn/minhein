from django.contrib import admin
from . models import About, TypeWriter, Skill, Blog, Gallery, Fact, Contact

# Register your models here.
class aboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'birthday', 'image']
admin.site.register(About, aboutAdmin)

class FactAdmin(admin.ModelAdmin):
    list_display = ['id', 'fact', 'number']
admin.site.register(Fact, FactAdmin)

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
    list_display = ['id', 'subject', 'image']
admin.site.register(Gallery, GalleryAdmin)

## contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message']
admin.site.register(Contact, ContactAdmin)