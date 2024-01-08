from django.shortcuts import render
from .models import Project, About
from moviepy.editor import VideoFileClip
from django.contrib.humanize.templatetags import humanize
from django.utils import timezone


# Create your views here.


def home(request):
    projects = Project.objects.all().order_by('-id')
    # Llamar a la función para obtener el tiempo actual
    current_time = get_current_time()
    for project in projects:
        project.created_at = current_time
        project.save()
    return render(request, 'home.html', {'projects': projects, 'current_time': current_time})


def get_current_time():
    return humanize.naturaltime(timezone.now())


def about(request):
    about = About.objects.all()
    return render(request, 'about.html', {'obj': about})
