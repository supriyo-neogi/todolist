from django.urls import path
from . import views

urlpatterns = [
    path("",views.FormView.as_view()),
    path("all-task",views.all_task,name="all_task"),
    path("home/",views.Home.as_view(),name="home"),
]


