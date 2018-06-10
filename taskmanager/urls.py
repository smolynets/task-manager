from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^add_task', views.add_task, name='add_task'),
    url(r'^task/(?P<pk>\d+)/one', views.one_task, 
    	name='one_task'),
    url(r'^checkname', views.checkname, name='checkname'),
    url(r'^task/(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),
]