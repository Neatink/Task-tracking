
from django.contrib import admin
from django.urls import path
from TaskSystem.views import TasksView,TaskStatusesView,TaskPrioritiesView,HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TasksView.as_view()),
    path('task_priorities/', TaskPrioritiesView.as_view()),
    path('task_statuses/', TaskStatusesView.as_view()),
    path('home/', HomeView.as_view()),
]
