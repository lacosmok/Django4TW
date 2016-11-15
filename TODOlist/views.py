from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView
from django.core.urlresolvers import reverse_lazy

from .models import Task, ToDoList
from .forms import TaskCreateForm, ToDoListCreateForm
# Create your views here.
class TaskCreateView(CreateView):
    model =Task
    form_class = TaskCreateForm
    template_name = 'add_task.html'

    def form_valid(self, form, **kwargs):
        context = super(TaskCreateView, self).form_valid(form, **kwargs)
        self.object = form.save(commit=True)
        self.object.todolist = ToDoList.objects.get(pk=self.kwargs['application_pk'])
        return context

class ToDoListCreateView(CreateView):
    model = ToDoList
    form_class = ToDoListCreateForm
    template_name = 'add_todo.html'

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("home")

class ToDoListDeleteView(DeleteView):
    model = ToDoList
    success_url = reverse_lazy("home")

class TaskUpdateView(UpdateView):
    model =Task
    #form_class = TaskCreateForm
    template_name = 'add_task.html'

class ToDoListUpdateView(UpdateView):
    model = ToDoList
    #form_class = TaskCreateForm
    template_name = 'add_todo.html'

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

