
from django.contrib import admin
from django.urls import path
from TaskSystem.views import TasksView,TaskStatusesView,TaskPrioritiesView,HomeView,TasksDetailsView,TaskStatusesDetailsView
from TaskSystem.views import TaskPrioritiesDetailsView,AddTaskView,AddTaskPrioritiesView,AddTaskStatusesView,DeleteTaskView,DeleteTaskPrioritiesView,DeleteTaskStatusesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TasksView.as_view()),
    path('task_priorities/', TaskPrioritiesView.as_view()),
    path('task_statuses/', TaskStatusesView.as_view()),
    path('home/', HomeView.as_view()),
    path('tasks_details/<pk>/', TasksDetailsView.as_view()),
    path('task_statuses_details/<pk>/', TaskStatusesDetailsView.as_view()),
    path('task_priorities_details/<pk>/', TaskPrioritiesDetailsView.as_view()),
    path('add_tasks/', AddTaskView.as_view()),
    path('add_task_priorities/', AddTaskPrioritiesView.as_view()),
    path('add_task_statuses/', AddTaskStatusesView.as_view()),
    path('delete_task/<pk>', DeleteTaskView.as_view()),
    path('delete_task-status/<pk>', DeleteTaskStatusesView.as_view()),
    path('delete_task-priority/<pk>', DeleteTaskPrioritiesView.as_view()),
]
