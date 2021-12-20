from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Task
from django.urls import reverse_lazy

# Create your views here.
class TaskList(ListView):  
    model = Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task_detail'
    template_name = "app/task_detail.html"

class TaskCreate(CreateView):
    model = Task
    # template_name = "app/task_form.html"
    fields = '__all__'
    success_url = reverse_lazy('task-list')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('task-list')
    template_name = "app/task_delete.html"
