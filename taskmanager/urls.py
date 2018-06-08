from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^task/(?P<pk>\d+)/', views.one_task, 
    	name='one_task'),
]