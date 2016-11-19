# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

STATUS = (
    (1, "Completed"),
    (0, "Not Completed")
)

# Create your models here.
class ToDoList(models.Model):

    name = models.TextField(default='', blank=True, null=True, verbose_name='Name')
    last_update = models.DateField(null=False, default=now, verbose_name='Last update')

    def __unicode__(self):
        return self.name

class Task(models.Model):

    name = models.TextField(default='', blank=True, null=True, verbose_name='Name')
    todolist = models.ForeignKey(ToDoList, null=True, blank=True, verbose_name='TODOlist', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False, choices=STATUS, verbose_name='Is it finished?')
    text = models.TextField(default='', blank=True, null=True, verbose_name='Task')
    last_update = models.DateField(null=True, default=now, verbose_name='Last update')

    def __unicode__(self):
        return self.text