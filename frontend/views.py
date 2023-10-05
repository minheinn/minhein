from django.shortcuts import render, redirect
from dashboard.models import *
from datetime import datetime
import json
from . import constant


# Create your views here.
def index(request):
    about = About.objects.last()
    facts = Fact.objects.all()
    fact_content = constant.FACT_CONTENT ## for fact content
    birthday = about.birthday
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    text= TypeWriter.objects.values_list("text",flat=True)
    type_writers = json.dumps(list(text))
    skills = Skill.objects.all()
    skill_content = constant.SKILL_CONTENT  ### for skill content
    galleries = Gallery.objects.all()
    gallery_content = constant.GALLERY_CONTENT ## for gallery content
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        Contact.objects.create(
            name=name, 
            email=email, 
            message=message 
        )
        return redirect("index")
    context = {
        'about':about, 
        'facts':facts,
        'fact_content':fact_content,
        'age':age, 
        'type_writers':type_writers, 
        'skills':skills, 
        'skill_content':skill_content,
        'galleries':galleries,
        'gallery_content':gallery_content,
        }
    return render(request, 'frontend/index.html', context)