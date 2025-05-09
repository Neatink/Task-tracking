from django.db import models
from django.contrib.auth.models import User


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
    create_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    description = models.TextField(null=False,blank=False)