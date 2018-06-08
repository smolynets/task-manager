from django.shortcuts import render

from .models import *



def list(request):
	tasks = Task.objects.all()
	return render(request, 'taskmanager/home.html', {'task': tasks})



def one_task(request, pk):
  task = Task.objects.filter(pk=pk)
  return render(request, 'taskmanager/one_task.html', {'task':task})