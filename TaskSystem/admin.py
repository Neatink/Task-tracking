from django.contrib import admin
from .models import Task,Comment,TaskPriority,TaskStatus

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(TaskPriority)
admin.site.register(TaskStatus)