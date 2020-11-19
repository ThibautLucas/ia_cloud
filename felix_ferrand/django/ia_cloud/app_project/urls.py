from django.urls import path, include
from app_project import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
]
