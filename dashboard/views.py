from django.shortcuts import render
from . forms import aboutForm

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

########### About ###########
def about(request):
    forms = aboutForm()
    context = {'forms':forms}
    return render(request, 'dashboard/about/about.html', context)