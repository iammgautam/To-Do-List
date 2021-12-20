from django.db import models
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView


from .models import Task
from django.urls import reverse_lazy

# Create your views here.
#Task List View
class TaskList(ListView):  
    model = Task
    context_object_name = 'tasks'

#Task Detail View
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task_detail'
    template_name = "app/task_detail.html"

#ToDo Task Create View
class TaskCreate(CreateView):
    model = Task
    # template_name = "app/task_form.html"
    fields = '__all__'
    success_url = reverse_lazy('task-list')

#ToDo Task Update View
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')
#ToDo Task Delete View
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('task-list')
    template_name = "app/task_delete.html"

#Todo Task Login View
class CustomLoginView(LoginView):
    template_name = 'app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task-list')