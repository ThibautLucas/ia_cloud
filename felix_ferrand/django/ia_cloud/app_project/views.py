from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_project.models import Profile
from app_project.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def profile(request):
    return render(request, 'app_project/profile.html', locals())

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username, email, password)
            user.is_active = True
            user.save()
            profile = Profile(user=user)
            profile.save()
            login(request, user, backend='django.contrib.auth.backends.MoveBackend')
            return redirect('profile')
        else:
            return render(request, 'app_project/signup.html', {
                'form': form,
            })
    else:
        form = SignUpForm()
        return render(request, 'app_project/signup.html', {
            'form': form,
        })

# def signin(request):
