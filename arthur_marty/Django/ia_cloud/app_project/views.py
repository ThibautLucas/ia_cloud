from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_project.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

# Create your views here.
@login_required(login_url='signup')
def hello_world(request):
    return render(request, 'app_project/hello_world.html', locals())

def hello_world_id(request, id):
    return render(request, 'app_project/hello_world_id.html', locals())



def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = User.objects.create_user(username, email, password)
            user.is_active = True
            user.save()

            login(request, user, backend='django.contrib.auth.backends.ModelBackend' )
            return redirect('hello_world')
        else:
            return render(request, 'app_project/signup.html', {
                'form' : form
            })
    else:
        form = SignUpForm()
        return render(request, 'app_project/signup.html', {
            'form' : form
        })

def logout_view(request):
    logout(request)
    return redirect('signup')


def signin(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = User.objects.create_user(username, email, password)
            user.is_active = True
            user.save()

            login(request, user, backend='django.contrib.auth.backends.ModelBackend' )
            return redirect('hello_world')
        else:
            return render(request, 'app_project/signup.html', {
                'form' : form
            })
    else:
        form = SignUpForm()
        return render(request, 'app_project/signup.html', {
            'form' : form
        })