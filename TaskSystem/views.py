from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView
from .models import Task,TaskPriority,TaskStatus

class HomeView(TemplateView):
    template_name = "home.html"

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