from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Task


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "First Name"}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}))


# class TodoForm(ModelForm):
#     class Meta:
#         model = Task

