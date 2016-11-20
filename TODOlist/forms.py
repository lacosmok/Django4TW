from django import forms
from .models import Task, ToDoList


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
        }


class ToDoListCreateForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['name']


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'completed']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
            'completed': forms.RadioSelect
        }
