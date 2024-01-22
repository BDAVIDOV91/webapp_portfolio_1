from django.shortcuts import render
from webapp_portfolio.models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def about_me(request):
    return render(request, 'about_me.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
