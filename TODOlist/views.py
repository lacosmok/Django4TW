from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.utils.timezone import now
from django.http import HttpResponse

from datetime import datetime

from .models import Task, ToDoList
from .forms import TaskCreateForm, ToDoListCreateForm, TaskUpdateForm


# Create your views here.
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'add_task.html'
    success_url = reverse_lazy("all-lists")

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form, **kwargs):
        context = super(TaskCreateView, self).form_valid(form, **kwargs)
        todolist = ToDoList.objects.get(pk=self.kwargs['pk'])
        todolist.last_update = now()
        todolist.save()
        form.instance.todolist = todolist
        form.save()
        return context


class ToDoListCreateView(CreateView):
    model = ToDoList
    form_class = ToDoListCreateForm
    template_name = 'add_list.html'
    success_url = reverse_lazy("all-lists")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("all-lists")


class ToDoListDeleteView(DeleteView):
    model = ToDoList
    success_url = reverse_lazy("all-lists")


class ToDoListUpdateView(UpdateView):
    model = ToDoList
    form_class = ToDoListCreateForm
    template_name = 'add_list.html'
    success_url = reverse_lazy("all-lists")

    def form_valid(self, form, **kwargs):
        context = super(ToDoListUpdateView, self).form_valid(form, **kwargs)
        form.instance.last_update = now()
        form.save()
        return context


class ToDoListView(ListView):
    model = ToDoList
    template_name = 'show_lists.html'

    def get_context_data(self, **kwargs):
        context = super(ToDoListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return self.model.objects.all()


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'add_task.html'
    success_url = reverse_lazy("all-lists")

    def form_valid(self, form, **kwargs):
        context = super(TaskUpdateView, self).form_valid(form, **kwargs)
        todolist = ToDoList.objects.get(pk=form.instance.todolist.pk)
        todolist.last_update = now()
        todolist.save()
        form.instance.last_update = now()
        form.save()
        return context

