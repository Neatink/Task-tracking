from django.shortcuts import redirect,HttpResponseRedirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Task,TaskPriority,TaskStatus,Comment
from .forms import TaskForm,TaskPriorityForm,TaskStatusForm,RegisterForm,FilterForm,CommentForm
from .mixins import UserIsOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = "home.html"


class DeniedView(TemplateView):
    template_name = "denied.html"


class TasksView(ListView):
    context_object_name = 'tasks'
    template_name = "tasks.html"
    model = Task    
    
    def get_queryset(self):
        queryset = Task.objects.filter()
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        
        if status:
            queryset = queryset.filter(status_id = status)
        if priority:
            queryset = queryset.filter(priority_id = priority)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = FilterForm(self.request.GET)
        return context

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment"] = Comment.objects.filter(task=self.object)
        context["form"] = CommentForm
        return context
    

class AddTaskView(LoginRequiredMixin,CreateView):
    template_name = 'add/add_tasks.html'
    form_class = TaskForm
    success_url = '/tasks'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddTaskPrioritiesView(LoginRequiredMixin,CreateView):
    template_name = 'add/add_task_priorities.html'
    form_class = TaskPriorityForm
    success_url = '/task_priorities'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddTaskStatusesView(LoginRequiredMixin,CreateView):
    template_name = 'add/add_task_statuses.html'
    form_class = TaskStatusForm
    success_url = '/task_statuses'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteTaskView(LoginRequiredMixin,UserIsOwnerMixin,DeleteView):
    model = Task
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return redirect('/tasks')
    

class DeleteTaskPrioritiesView(LoginRequiredMixin,UserIsOwnerMixin,DeleteView):
    model = TaskPriority
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return redirect('/task_priorities')
    

class DeleteTaskStatusesView(LoginRequiredMixin,UserIsOwnerMixin,DeleteView):
    model = TaskStatus
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return redirect('/task_statuses')
    

class UpdateTaskView(LoginRequiredMixin,UserIsOwnerMixin,UpdateView):
    template_name = 'update/update_tasks.html'
    model = Task
    form_class = TaskForm
    success_url ="/tasks"

    
class UpdateTaskPrioritiesView(LoginRequiredMixin,UserIsOwnerMixin,UpdateView):
    template_name = 'update/update_task_priorities.html'
    model = TaskPriority
    form_class = TaskPriorityForm
    success_url ="/task_priorities"
    
    
class UpdateTaskStatusesView(LoginRequiredMixin,UserIsOwnerMixin,UpdateView):
    template_name = 'update/update_task_statuses.html'
    model = TaskStatus
    form_class = TaskStatusForm
    success_url ="/task_statuses"
    
    
class RegisterUserView(CreateView):
    template_name = 'registration/register.html'
    success_url = '/login'
    form_class = RegisterForm
    
    
class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'profile.html'
    
    
class AddCommentView(LoginRequiredMixin,CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.task = Task.objects.get(id=self.kwargs['task_pk'])
        form.save()
        return HttpResponseRedirect(self.request.POST.get(f'/tasks_details/{ self.kwargs['task_pk'] }', f'/tasks_details/{ self.kwargs['task_pk'] }'))
    

class UpdateCommentView(LoginRequiredMixin,UserIsOwnerMixin,UpdateView):
    model = Comment
    fields = ["description"]
    template_name = 'update/update_comment.html'

    def get_success_url(self):
        return (self.request.POST.get(f'/tasks_details/{ self.get_object().task_id }', f'/tasks_details/{ self.get_object().task_id }'))
    
    
class DeleteCommentView(LoginRequiredMixin,UserIsOwnerMixin,DeleteView):
    model = Comment
    
    def get(self, request, *args, **kwargs):
        task_id = self.get_object().task_id
        self.get_object().delete()
        return redirect(f'/tasks_details/{task_id}')