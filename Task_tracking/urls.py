
from django.contrib import admin
from django.urls import path
from TaskSystem.views import TasksView,TaskStatusesView,TaskPrioritiesView,HomeView,TasksDetailsView,TaskStatusesDetailsView,TaskPrioritiesDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TasksView.as_view()),
    path('task_priorities/', TaskPrioritiesView.as_view()),
    path('task_statuses/', TaskStatusesView.as_view()),
    path('home/', HomeView.as_view()),
    path('tasks_details/<pk>/', TasksDetailsView.as_view()),
    path('task_statuses_details/<pk>/', TaskStatusesDetailsView.as_view()),
    path('task_priorities_details/<pk>/', TaskPrioritiesDetailsView.as_view()),
]
