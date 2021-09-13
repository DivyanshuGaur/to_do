
from django.contrib import admin
from django.urls import path,include 
from . import views

urlpatterns = [
        path('',views.homepage),
        path('add_to',views.add_to),
        path('delete_todo/<int:todo_id>/',views.delete)
]
