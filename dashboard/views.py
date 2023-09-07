from django.shortcuts import render, redirect
from . models import About
from . forms import AboutForm
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
            form = AboutForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'About {} has been added successfully!'.format(about.name))
                return redirect('about')
        context = {'forms':forms, 'about':about}
        return render(request, 'dashboard/about/about.html', context)
    else:
        about = About.objects.latest('id')
        forms = AboutForm(instance=about)
        if request.method == "POST":
            form = AboutForm(request.POST, instance=about)
            if form.is_valid():
                form.save()
                messages.success(request, 'About {} has been updated successfully!'.format(about.name))
                return redirect('about')
        context = {'about':about, 'forms':forms}
        return render(request, 'dashboard/about/about.html', context)    

def aboutDelete(request, pk):
    about = About.objects.latest('id')
    if request.method == "POST":
        about.delete()
        messages.error(request, 'About {} has been deleted successfully!'.format(about.name))
        return redirect('about')
    context = {'about':about}
    return render(request, 'dashboard/about/delete.html', context)