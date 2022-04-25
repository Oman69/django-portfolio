from django.shortcuts import render
from .models import Project, Certificates

# Create your views here.


def home(request):
    projects = Project.objects.all()
    certificates = Certificates.objects.all()
    return render(request, 'port/home.html', {'projects': projects, 'certificates': certificates})