
from django.contrib import admin
from django.urls import path
from TaskSystem.views import TasksView,TaskStatusesView,TaskPrioritiesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TasksView.as_view()),
    path('task_priorities/', TaskPrioritiesView.as_view()),
    path('task_statuses/', TaskStatusesView.as_view()),
]
