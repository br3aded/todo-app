from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import redirect , get_object_or_404
from django.urls import reverse
from .models import Task

def index(request):
    task_list = Task.objects.all
    return render(request, "todo/index.html", {'task_list': task_list})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    task_list = Task.objects.all
    return HttpResponseRedirect(reverse('todo:index'))
# Create your views here.
