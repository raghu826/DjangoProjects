from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myProjects.models import Project

def project_index(request):
    myProjects = Project.objects.all()
    context = {
        'myProjects': myProjects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)