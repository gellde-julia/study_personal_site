from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all() #для импорта данных из базы
    return render(request, "portfolio/home.html", {'projects':projects})