from django.shortcuts import render
from dashboard.models import *
from datetime import datetime
import json
from . import constant


# Create your views here.
def index(request):
    about = About.objects.last()
    birthday = about.birthday
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    text= TypeWriter.objects.values_list("text",flat=True)
    type_writers = json.dumps(list(text))
    skills = Skill.objects.all()
    skill_content = constant.SKILL_CONTENT  ### for skill content
    galleries = Gallery.objects.all()
    gallery_content = constant.GALLERY_CONTENT ## for gallery content
    context = {
        'about':about, 
        'age':age, 
        'type_writers':type_writers, 
        'skills':skills, 
        'skill_content':skill_content,
        'galleries':galleries,
        'gallery_content':gallery_content,
        }
    return render(request, 'frontend/index.html', context)