from django.shortcuts import render
from dashboard.models import *

# Create your views here.
def index(request):
    about = About.objects.last()
    context = {'about':about}
    return render(request, 'frontend/index.html', context)