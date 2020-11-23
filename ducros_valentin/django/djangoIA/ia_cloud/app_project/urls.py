from django.urls import path, include
from app_project import views

urlpatterns = [
    path('project/hello_world', views.hello_world, name="hello_world"),
    path('project/signup', views.signup, name='signup')
]