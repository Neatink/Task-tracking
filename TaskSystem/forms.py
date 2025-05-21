from django import forms
from .models import Task,TaskPriority,TaskStatus
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name","status","priority","description","deadline"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Назва задачi',
                'autofocus':'True',
                }),
            'description':forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Опис задачi',
            }),
            'priority':forms.Select(attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control'}),
            'deadline':forms.DateTimeInput(attrs={
                'class':'form-control',
                'type':'datetime-local',
            })
        }


class TaskPriorityForm(forms.ModelForm):
    class Meta:
        model = TaskPriority
        fields = ["name"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Назва прiорiтету',
                'autofocus':'Prisutstvuet',
                }),
        }


class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = ["name"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Назва статусу',
                'autofocus':'Prisutstvuet',
                }),
        }
        
class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","email"]
