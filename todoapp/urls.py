from . import views
from django.urls import path

app_name = 'todoapp'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task_delete/<int:task_id>', views.task_delete, name='task_delete'),
    path('task_create/', views.task_create, name='task_create'),
]
