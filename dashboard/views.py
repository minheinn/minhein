from django.shortcuts import render, redirect
from . models import *
from . forms import *
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

########### About ###########
def about(request):
    forms = AboutForm()
    about = About.objects.first()
    if not about:
        if request.method == "POST":
            form = AboutForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'About Has been added successfully!')
                return redirect('about')
        context = {'forms':forms, 'about':about}
        return render(request, 'dashboard/about/about.html', context)
    else:
        about = About.objects.latest('id')
        forms = AboutForm(instance=about)
        if request.method == "POST":
            form = AboutForm(request.POST, request.FILES, instance=about)
            if form.is_valid():
                form.save()
                messages.success(request, 'About {} has been updated successfully!'.format(about.name))
                return redirect('about')
        context = {'about':about, 'forms':forms}
        return render(request, 'dashboard/about/about.html', context)    

def aboutDelete(request, slug):
    about = About.objects.latest('slug')
    if request.method == "POST":
        about.delete()
        messages.error(request, 'About {} has been deleted successfully!'.format(about.name))
        return redirect('about')
    context = {'about':about}
    return render(request, 'dashboard/about/delete.html', context)

## Facts 
def fact(request):
    page = "fact"
    facts = Fact.objects.all()
    forms = FactForm()
    if request.method == "POST":
        form = FactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Has been added successfully!')
            return redirect('fact')
    context = {'page':page,'facts':facts, 'forms':forms}
    return render(request, 'dashboard/fact/fact.html', context)

def fact_edit(request, slug):
    facts = Fact.objects.all()
    fact = Fact.objects.get(slug=slug)
    forms = FactForm(instance=fact)
    if request.method == "POST":
        form = FactForm(request.POST, instance=fact)
        if form.is_valid():
            form.save()
            messages.success(request, "{} has been updated successfully!".format(fact.fact))
            return redirect('fact')
    context = {'facts':facts, 'fact':fact, 'forms':forms}
    return render(request, 'dashboard/fact/fact.html', context)

def fact_delete(request, slug):
    fact = Fact.objects.get(slug=slug)
    if request.method == "POST":
        fact.delete()
        messages.error(request, '{} has been deleted successfully!'.format(fact.fact))
        return redirect('fact')       
    context = {'fact':fact}
    return render(request, 'dashboard/fact/delete.html', context)

## type_writer started
def type_writer(request):
    page = "type_writer"
    type_writers = TypeWriter.objects.all()
    forms = TypeWriterForm()
    if request.method == "POST":
        form = TypeWriterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Has been added successfully!')
            return redirect('type-writer')
    context = {'page':page, 'type_writers':type_writers, 'forms':forms}
    return render(request, 'dashboard/type_writer/type_writer.html', context)

def type_writer_edit(request, slug):
    type_writers = TypeWriter.objects.all()
    type_writer = TypeWriter.objects.get(slug=slug)
    forms = TypeWriterForm(instance=type_writer)
    if request.method == "POST":
        form = TypeWriterForm(request.POST, instance=type_writer)
        if form.is_valid():
            form.save()
            messages.success(request, '{} has been updated successfully!'.format(type_writer.text))
            return redirect('type-writer')
    context = {'type_writers':type_writers, 'type_writer':type_writer, 'forms':forms}
    return render(request, 'dashboard/type_writer/type_writer.html', context)

def type_writer_delete(request, slug):
    type_writer = TypeWriter.objects.get(slug=slug)
    if request.method == "POST":
        type_writer.delete()
        messages.error(request, '{} has been deleted successfully!'.format(type_writer.text))
        return redirect('type-writer')
    context = {'type_writer':type_writer}
    return render(request, 'dashboard/type_writer/delete.html', context)

## type_writer end ##

## skill started ##
def skill(request):
    page = 'skill'
    skills = Skill.objects.all()
    forms = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Has been added successfully!')
            return redirect('skill')
    context = {'page':page,'skills':skills, 'forms':forms}
    return render(request, 'dashboard/skill/skill.html', context)

def skill_edit(request, slug):
    skills = Skill.objects.all()
    skill = Skill.objects.get(slug=slug)
    forms = SkillForm(instance=skill)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, '{} has been updated successfully!'.format(skill.skill))
            return redirect('skill')
    context = {'skills':skills, 'skill':skill, 'forms':forms}
    return render(request, 'dashboard/skill/skill.html', context)

def skill_delete(request, slug):
    skill = Skill.objects.get(slug=slug)
    if request.method == "POST":
        skill.delete()
        messages.error(request, '{} has been deleted successfully!'.format(skill.skill))
        return redirect('skill')
    context = {'skill':skill}
    return render(request, 'dashboard/skill/delete.html', context)
## skill ended ##

### blog started ###
def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'dashboard/blog/blog.html', context)

def blog_add(request):
    forms = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Has been added successfully!')
            return redirect('blog')
    context = {'forms':forms}
    return render(request, 'dashboard/blog/add_blog.html', context)

def blog_edit(request, slug):
    blog = Blog.objects.get(slug=slug)
    forms = BlogForm(instance=blog)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, '{} has been updated successfully!'.format(blog.title))
            return redirect('blog')
    context = {'blog':blog, 'forms':forms}
    return render(request, 'dashboard/blog/edit_blog.html', context)

def blog_delete(request, slug):
    blog = Blog.objects.get(slug=slug)
    if request.method == "POST":
        blog.delete()
        messages.error(request, '{} has been deleted successfully!'.format(blog.title))
        return redirect('blog')
    context = {'blog':blog}
    return render(request, 'dashboard/blog/delete.html', context)

## Gallery started
def gallery(request):
    page = "gallery"
    galleries = Gallery.objects.all()
    forms = GalleryForm()
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Has been added successfully!')
            return redirect('gallery')
    context = {'page':page, 'galleries':galleries, 'forms':forms}
    return render(request, 'dashboard/gallery/gallery.html', context)

def gallery_edit(request, slug):
    galleries = Gallery.objects.all()
    gallery = Gallery.objects.get(slug=slug)
    forms = GalleryForm(instance=gallery)
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            messages.success(request, '{} has been updated successfully!'.format(gallery.image))
            return redirect('gallery')
    context = {'galleries':galleries, 'gallery':gallery, 'forms':forms,}
    return render(request, 'dashboard/gallery/gallery.html', context)

def gallery_delete(request, slug):
    gallery = Gallery.objects.get(slug=slug)
    if request.method == "POST":
        gallery.delete()
        messages.error(request, '{} has been deleted successfully!'.format(gallery.image))
        return redirect('gallery')
    context = {'gallery':gallery}
    return render(request, 'dashboard/gallery/delete.html', context)

## for Contact
def contact(request):
    contacts = Contact.objects.all()
    context = {'contacts':contacts}
    return render(request, 'dashboard/contact/contact.html', context)
