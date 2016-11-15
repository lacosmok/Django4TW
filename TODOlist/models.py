from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


# Create your models here.
class ToDoList(models.Model):

    name = models.TextField(default='', blank=True, null=True, verbose_name='Name')
    last_update = models.DateField(null=False, default=now, verbose_name='Last update')


class Task(models.Model):

    name = models.TextField(default='', blank=True, null=True, verbose_name='Name')
    todolist = models.ForeignKey(ToDoList, null=True, blank=True, verbose_name='TODOlist')
    completed = models.BooleanField(default=False, verbose_name='Is it finished?')
    text = models.TextField(default='', blank=True, null=True, verbose_name='Task')
    last_update = models.DateField(null=False, default=now, verbose_name='Last update')

    def save(self, user=None, *args, **kwargs):
        todolist = ToDoList.objects.get(pk=self.todolist.pk)
        todolist.last_update = now
        self.last_update = now
        super(Task, self).save( *args, **kwargs)