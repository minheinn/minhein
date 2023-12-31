from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.crypto import get_random_string
from django.utils.text import slugify

# Create your models here.
### for slug ##
def unique_slugify(instance, slug):
        model = instance.__class__
        unique_slug = slug
        while model.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + get_random_string(length=4)
        return unique_slug

class About(models.Model):
    name = models.CharField(max_length=50, null=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    description = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField(upload_to="about_image/", null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, null=False,blank=True,unique=True,editable=False,)

    def save(self, *args, **kwargs):
        if not self.slug: # If the slug is not set
            self.slug = unique_slugify(self,slugify(self.name,allow_unicode=True)) # Generate the slug from the title
        else:
            new_slug = unique_slugify(self,slugify(self.name,allow_unicode=True))
            if self.slug != new_slug: # Check if the title has changed
                self.slug = new_slug # Update the slug with the new value
        super().save(*args, **kwargs) # Call the parent save method

def __str__(self):
    return self.name

## For Facts ##
class Fact(models.Model):
    fact = models.CharField(max_length=50, null=True)
    number = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, null=False,blank=True,unique=True,editable=False,)
    
    def save(self, *args, **kwargs):
        if not self.slug: # If the slug is not set
            self.slug = unique_slugify(self,slugify(self.fact,allow_unicode=True)) # Generate the slug from the title
        else:
            new_slug = unique_slugify(self,slugify(self.fact,allow_unicode=True))
            if self.slug != new_slug: # Check if the title has changed
                self.slug = new_slug # Update the slug with the new value
        super().save(*args, **kwargs) # Call the parent save method
    
def __str__(self):
    return self.fact

## for Type Writers ##
class TypeWriter(models.Model):
    text = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, null=False,blank=True,unique=True,editable=False,)

    def save(self, *args, **kwargs):
        if not self.slug: # If the slug is not set
            self.slug = unique_slugify(self,slugify(self.text,allow_unicode=True)) # Generate the slug from the title
        else:
            new_slug = unique_slugify(self,slugify(self.text,allow_unicode=True))
            if self.slug != new_slug: # Check if the title has changed
                self.slug = new_slug # Update the slug with the new value
        super().save(*args, **kwargs) # Call the parent save method

def __str__(self):
    return self.text

class Skill(models.Model):
    skill = models.CharField(max_length=50, null=True)
    percent = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, null=False,blank=True,unique=True,editable=False,)

    def save(self, *args, **kwargs):
        if not self.slug: # If the slug is not set
            self.slug = unique_slugify(self,slugify(self.skill,allow_unicode=True)) # Generate the slug from the title
        else:
            new_slug = unique_slugify(self,slugify(self.skill,allow_unicode=True))
            if self.slug != new_slug: # Check if the title has changed
                self.slug = new_slug # Update the slug with the new value
        super().save(*args, **kwargs) # Call the parent save method

    def __str__(self):
        return self.skill
    
### Blogs ###
class Blog(models.Model):
    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="blog-photos", null=True)
    description = RichTextUploadingField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, null=False,blank=True,unique=True,editable=False,)

    def save(self, *args, **kwargs):
        if not self.slug: # If the slug is not set
            self.slug = unique_slugify(self,slugify(self.title,allow_unicode=True)) # Generate the slug from the title
        else:
            new_slug = unique_slugify(self,slugify(self.title,allow_unicode=True))
            if self.slug != new_slug: # Check if the title has changed
                self.slug = new_slug # Update the slug with the new value
        super().save(*args, **kwargs) # Call the parent save method

    def __str__(self):
        return self.title
    
## Subjects
SUBJECT = (
    ('A','APP'),
    ('W','WEB'),
    ('C','CARD'),
)
    
class Gallery(models.Model):
    subject = models.CharField(max_length=3, choices=SUBJECT, null=True)
    image = models.ImageField(upload_to="galleries/", null=True)
    slug = models.SlugField(max_length=255, null=False,blank=True,unique=True,editable=False,)

    def save(self, *args, **kwargs):
        if not self.slug: # If the slug is not set
            self.slug = unique_slugify(self,slugify(self.image,allow_unicode=True)) # Generate the slug from the title
        else:
            new_slug = unique_slugify(self,slugify(self.image,allow_unicode=True))
            if self.slug != new_slug: # Check if the title has changed
                self.slug = new_slug # Update the slug with the new value
        super().save(*args, **kwargs) # Call the parent save method

    def __str__(self):
        return str('image')
    
class Contact(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, null=False,blank=True,unique=True,editable=False,)

    def save(self, *args, **kwargs):
        if not self.slug: # If the slug is not set
            self.slug = unique_slugify(self,slugify(self.name,allow_unicode=True)) # Generate the slug from the title
        else:
            new_slug = unique_slugify(self,slugify(self.name,allow_unicode=True))
            if self.slug != new_slug: # Check if the title has changed
                self.slug = new_slug # Update the slug with the new value
        super().save(*args, **kwargs) # Call the parent save method

    def __str__(self):
        return self.name

