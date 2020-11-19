from django.urls import path, include
from app_project import views

urlpatterns = [
    path('project/hello_world', views.hello_world, name='hello_world'),
    path('project/hello_world/<id>', views.hello_world_id, name='hello_world_id'),
]
