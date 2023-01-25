from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Task

def home(request):
    task_list = Task.objects.all
    return render(request, "todo/index.html", {'task_list': task_list})

# Create your views here.
