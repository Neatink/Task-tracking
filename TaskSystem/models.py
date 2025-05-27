from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class TaskStatus(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class TaskPriority(models.Model):
    name = models.CharField(max_length=35)
    
    def __str__(self):
        return self.name
    

class Task(models.Model):
    name = models.CharField(max_length=70,unique=True,blank=False,null=False)
    description = models.TextField(max_length=200)
    status = models.ForeignKey(TaskStatus,max_length=50,on_delete=models.SET_NULL,null=True)
    priority = models.ForeignKey(TaskPriority,max_length=35,on_delete=models.SET_NULL,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    deadline = models.DateTimeField(blank=True,null=True)
    
    class Meta:
        ordering = ['deadline']    

    def clean(self):
        if self.deadline is not None and self.deadline < timezone.now():
            raise ValidationError('Дедлайн повинен бути не в минулому часi!')
        

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    description = models.TextField(null=False,blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']