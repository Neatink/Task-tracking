from django.shortcuts import redirect,render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView
from .models import Task,TaskPriority,TaskStatus
from .forms import TaskForm,TaskPriorityForm,TaskStatusForm


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

class DeleteTaskView(DeleteView):
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