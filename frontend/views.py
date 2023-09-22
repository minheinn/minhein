from django.shortcuts import render
from dashboard.models import *
from datetime import datetime
import json


# Create your views here.
def index(request):
    about = About.objects.last()
    birthday = about.birthday
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    text= TypeWriter.objects.values_list("text",flat=True)
    type_writers = json.dumps(list(text))
    context = {'about':about, 'age':age, 'type_writers':type_writers}
    return render(request, 'frontend/index.html', context)