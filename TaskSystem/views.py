from django.shortcuts import redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Task,TaskPriority,TaskStatus
from .forms import TaskForm,TaskPriorityForm,TaskStatusForm,RegisterForm
from .mixins import UserIsOwnerMixin
from django.contrib.auth.views import LoginView

class HomeView(TemplateView):
    template_name = "home.html"

class DeniedView(TemplateView):
    template_name = "denied.html"


class TasksView(ListView):
    context_object_name = 'tasks'
    template_name = "tasks.html"
    model = Task


class TaskPrioritiesView(ListView):
    context_object_name = 'taskprior'
    template_name = "task_priorities.html"
    model = TaskPriority


class TaskStatusesView(ListView):
    context_object_name = 'taskstatus'
    template_name = "task_statuses.html"
    model = TaskStatus
    
    
class TaskStatusesDetailsView(DetailView):
    context_object_name = 'taskstatus'
    template_name = "details/task_statuses_details.html"
    model = TaskStatus
    

class TaskPrioritiesDetailsView(DetailView):
    context_object_name = 'taskprior'
    template_name = "details/task_priorities_details.html"
    model = TaskPriority
    
    
class TasksDetailsView(DetailView):
    context_object_name = 'tasks'
    template_name = "details/tasks_details.html"
    model = Task
    

class AddTaskView(CreateView):
    template_name = 'add/add_tasks.html'
    form_class = TaskForm
    success_url = '/tasks'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddTaskPrioritiesView(CreateView):
    template_name = 'add/add_task_priorities.html'
    form_class = TaskPriorityForm
    success_url = '/task_priorities'


class AddTaskStatusesView(CreateView):
    template_name = 'add/add_task_statuses.html'
    form_class = TaskStatusForm
    success_url = '/task_statuses'

class DeleteTaskView(UserIsOwnerMixin,DeleteView):
    model = Task
    context_object_name = 'tasks'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return redirect('/tasks')
    

class DeleteTaskPrioritiesView(DeleteView):
    model = TaskPriority
    context_object_name = 'taskprior'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return redirect('/task_priorities')
    

class DeleteTaskStatusesView(DeleteView):
    model = TaskStatus
    context_object_name = 'taskstatus'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return redirect('/task_statuses')
    

class UpdateTaskView(UserIsOwnerMixin,UpdateView):
    template_name = 'update/update_tasks.html'
    model = Task
    form_class = TaskForm
    success_url ="/tasks"

    
class UpdateTaskPrioritiesView(UpdateView):
    template_name = 'update/update_task_priorities.html'
    model = TaskPriority
    form_class = TaskPriorityForm
    success_url ="/task_priorities"
    
    
class UpdateTaskStatusesView(UpdateView):
    template_name = 'update/update_task_statuses.html'
    model = TaskStatus
    form_class = TaskStatusForm
    success_url ="/task_statuses"
    
class RegisterUserView(CreateView):
    template_name = 'registration/register.html'
    success_url = '/login'
    form_class = RegisterForm