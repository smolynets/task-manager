from django.shortcuts import render, redirect, get_object_or_404
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
    cur_cat = request.COOKIES.get('current_category')
    if cur_cat:
        tasks = Task.objects.filter(category=Category.objects.filter(name=cur_cat))
    else:
        tasks = Task.objects.order_by('id').reverse()
    return render(request, 'taskmanager/home.html', {'task': tasks,
        'categories': Category.objects.all(), 'cur_cat': cur_cat})



def one_task(request, pk):
  task = get_object_or_404(Task, pk=pk)
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
    return render(request, 'taskmanager/add_edit_task.html', {'form': form})




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



def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('list')
    else:
        form = AddTaskForm(instance=task)
    return render(request, 'taskmanager/add_edit_task.html', {'form': form})