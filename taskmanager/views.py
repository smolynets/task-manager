from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
from django import forms
from django.http import JsonResponse
from django.utils import timezone

from .models import *
from .forms import AddTaskForm
from django.contrib.auth.models import User



def list(request):
	tasks = Task.objects.order_by('id').reverse()
	return render(request, 'taskmanager/home.html', {'task': tasks})



def one_task(request, pk):
  task = Task.objects.filter(pk=pk)
  return render(request, 'taskmanager/one_task.html', {'task':task})



def add_task(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('list')
    else:
        form = AddTaskForm()
    return render(request, 'taskmanager/add_task.html', {'form': form})




def checkname(request):
    tasks = Task.objects.all()
    return_dict = dict()  
    nm = request.POST.get('name', '').strip()
    for t in tasks:
      if t.name == nm:
        a = 1
        break
      else:
        a = 0
    return_dict["a"] = a
    return JsonResponse(return_dict)   