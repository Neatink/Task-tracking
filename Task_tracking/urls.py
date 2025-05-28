
from django.contrib import admin
from TaskSystem.views import TasksView,TaskStatusesView,TaskPrioritiesView,HomeView,TasksDetailsView,TaskStatusesDetailsView,UpdateTaskView,UpdateTaskPrioritiesView,UpdateTaskStatusesView,ProfileView,AddCommentView,DeleteCommentView
from TaskSystem.views import TaskPrioritiesDetailsView,AddTaskView,AddTaskPrioritiesView,AddTaskStatusesView,DeleteTaskView,DeleteTaskPrioritiesView,DeleteTaskStatusesView,DeniedView,RegisterUserView,UpdateCommentView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path

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
    path('update_task/<pk>', UpdateTaskView.as_view()),
    path('update_task-status/<pk>', UpdateTaskStatusesView.as_view()),
    path('update_task-priority/<pk>', UpdateTaskPrioritiesView.as_view()),
    path('denied', DeniedView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/',RegisterUserView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view()),
    path('add_comment/<task_pk>', AddCommentView.as_view(), name='add_comment'),
    path('update_comment/<pk>', UpdateCommentView.as_view()),
    path('delete_comment/<pk>', DeleteCommentView.as_view()),
]
