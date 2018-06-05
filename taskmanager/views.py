from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
from django import forms

from .models import *



def list(request):
	tasks = Task.objects.all()
	return render(request, 'taskmanager/home.html', {'task': tasks})



def one_task(request, pk):
  task = Task.objects.filter(pk=pk)
  return render(request, 'taskmanager/one_task.html', {'task':task})



def add_task(request):
  # was form posted?
  if request.method == "POST":
    # was form add button clicked?
    if request.POST.get('add_button') is not None:
      # errors collection
      errors = {}
      # data for student object
      data = {}
      # validate user input
      name = request.POST.get('name', '').strip()
      if not name:
        errors['name'] = "enter name"
      else:
        data['name'] = name

      description = request.POST.get('description', '').strip()
      if not description:
        errors['description'] = "enter description"
      else:
        data['description'] = description

      category = request.POST.get('category', '').strip()
      if not category:
        errors['category'] = "select category"
      else:
        category = Category.objects.filter(pk=category)
        if len(category) != 1:
          errors['category'] = "Please select correct category"
        else:
          data['category'] = category[0]

      start = request.POST.get('start', '').strip()
      if not start:
        errors['start'] = "select start time"
      else:
      	try:
      		datetime.strptime(start, '%Y-%m-%d')
      	except:
      		errors['start'] = "select correct time"
      	else:
        	data['start'] = start

      finish = request.POST.get('finish', '').strip()
      if not finish:
        errors['finish'] = "select finish time"
      else:
      	try:
      		datetime.strptime(finish, '%Y-%m-%d')
      	except:
      		errors['finish'] = "select correct time"
      	else:
        	data['finish'] = finish

      label = request.POST.get('label', '').strip()
      if not label:
        errors['label'] = "select label"
      else:
        label = Label.objects.filter(pk=label)
        if len(label) != 1:
          errors['lebel'] = "Please select correct label"
        else:
          data['label'] = label[0]
       


      # save object
      if not errors:
        task = Task(**data)
        task.save()
        # redirect to home
        return HttpResponseRedirect( u'%s?status_message=task added!'  % reverse('list'))
      else:
        # render form with errors and previous user input
        return render(request, 'taskmanager/add_task.html',
        {'errors': errors, 'categories': Category.objects.all(),
        'labels': Label.objects.all()})
    elif request.POST.get('cancel_button') is not None:
      # redirect to home page on cancel button
      return HttpResponseRedirect( u'%s?status_message=Adding of task canseled!' % reverse('list'))
  else:
   # initial form render
   return render(request, 'taskmanager/add_task.html', 
   	{'categories': Category.objects.all(),
   	'labels': Label.objects.all()})