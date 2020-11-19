from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'id': 'username',
            }
        )
    )
    email = forms.EmailField(
        label='',
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(
        label='',
        max_length=30,
        min_length=0,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(
        label='',
        max_length=30,
        min_length=0,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
