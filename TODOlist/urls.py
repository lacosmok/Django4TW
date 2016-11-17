
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^list/all$', views.ToDoListView.as_view(), name='all-lists'),
    url(r'^list/add/$', views.ToDoListCreateView.as_view(), name='add-list'),
    url(r'^list/(?P<pk>\d+)/task/add/$', views.TaskCreateView.as_view(), name='add-task'),
]
