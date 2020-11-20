
from django.urls import path
from app_project import views

urlpatterns = [
    path('project/hello_world', views.hello_world, name="hello_world"),
    path('project/hello_world/<id>', views.hello_world_id, name="hello_world_id"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('logout', views.logout_view, name="logout_view"),
]
