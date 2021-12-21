from django.db import models
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from .models import Task
from django.urls import reverse_lazy

# Create your views here.
#Task List View
class TaskList(LoginRequiredMixin, ListView):  
    model = Task
    context_object_name = 'tasks'

    #method to get only User-specific data.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()

        #for the search of task in the task-list search bar.
        # search_input = self.request.GET.get('search-area') or ''
        # if search_input:
        #     context['tasks'] = context['tasks'].filter(title_icontains = search_input)
        # context['search_input'] = search_input

        # return context

#Task Detail View
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task_detail'
    template_name = "app/task_detail.html"

#ToDo Task Create View
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # template_name = "app/task_form.html"
    fields = ['title','description','complete']
    success_url = reverse_lazy('task-list')

    #method to override the user-specific method so that the task gets created by that specific user only.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

#ToDo Task Update View
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('task-list')

#ToDo Task Delete View
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('task-list')
    template_name = "app/task_delete.html"

#Todo Task Login View
class CustomLoginView(LoginView):
    template_name = 'app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    #method to redirect to the task-list if logged correctly.
    def get_success_url(self):
        return reverse_lazy('task-list')

#ToDO Task Register User View
class RegisterPage(FormView):
    template_name = 'app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task-list')

    #method to redirect the authenticated user to the task-list without letting them to login again.
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    #method for not letting authenticated user to goto login/ or register/ urls.
    def get(self,  *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task-list')
        return super(RegisterPage, self).get(*args, **kwargs)