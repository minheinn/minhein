from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=50, null=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    description = RichTextUploadingField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name

class TypeWriter(models.Model):
    text = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.text

