from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields='__all__'
        labels={"title": "Title",
                "description":"Add a description",
                "completed":"Task Completed"
                }
    

    
