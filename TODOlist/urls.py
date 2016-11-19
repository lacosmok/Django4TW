
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^list/all$', views.ToDoListView.as_view(), name='all-lists'),
    url(r'^list/add/$', views.ToDoListCreateView.as_view(), name='add-list'),
    url(r'^list/(?P<pk>\d+)/task/add/$', views.TaskCreateView.as_view(), name='add-task'),
    url(r'^list/task/(?P<pk>\d+)/edit/$', views.TaskUpdateView.as_view(), name='update-task'),
    url(r'^list/(?P<pk>\d+)/edit/$', views.ToDoListUpdateView.as_view(), name='update-list'),
    url(r'^list/(?P<pk>\d+)/task/delete/$', views.TaskDeleteView.as_view(), name='delete-task'),
    url(r'^list/(?P<pk>\d+)/delete/$', views.ToDoListDeleteView.as_view(), name='delete-list'),
]
