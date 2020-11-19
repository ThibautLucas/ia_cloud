from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    return render(request, 'app_project/hello_world.html', locals())
