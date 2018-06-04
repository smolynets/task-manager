from django.db import models

from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Category %s" % self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Label(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Label %s" % self.name

    class Meta:
        verbose_name = 'Label'
        verbose_name_plural = 'Labels'


class Author(models.Model):
    name = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Author %s" % self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Author'




class Task(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, null=True, default=None)
    category = models.ForeignKey(Category)
    label = models.ForeignKey(Label)
    start = models.DateTimeField(blank=True, null=True, default=None)
    finish = models.DateTimeField(blank=True, null=True, default=None)
    author = models.ForeignKey(Author)
    executer = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Task %s" % self.name

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
