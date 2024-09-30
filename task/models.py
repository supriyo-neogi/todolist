from django.db import models

#model for Form

class Task(models.Model):
    title= models.CharField(max_length=200)
    completed= models.BooleanField(default= False)
    created_on= models.DateTimeField(auto_now_add=True)
    description=models.TextField(max_length=500, blank=True)
    
