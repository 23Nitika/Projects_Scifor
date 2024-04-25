from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def about_view(request):
    return render(request, 'about.html')

def experience_view(request):
    return render(request, 'experience.html')

def projects_view(request):
    return render(request, 'projects.html')

def contact_view(request):
    return render(request, 'contact.html')

