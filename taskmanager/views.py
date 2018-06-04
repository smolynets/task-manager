from django.shortcuts import render

from .models import *

def list(request):
	tasks = Task.objects.all()
	return render(request, 'taskmanager/home.html', {'task': tasks})
