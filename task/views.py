from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic.list import ListView


class FormView(View):
    def get(self,request):
        form= TaskForm
        return render(request,"home.html",{
            "forms":form
        })
    
    def post(self,request):
        form= TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/all-task")
        else:
            return HttpResponse("Error adding task")
        
def all_task(request):
    tasks= Task.objects.all()
    return render(request, "all-task.html",
                  {"tasks":tasks}
                  )
class Home(FormView):
    template_name="home.html"
    form_class= TaskForm
    success_url= "/all-task"

class SortOut(ListView):
    model= Task
    template_name= "all-task.html"
    context_object_name= "tasks"
    


    