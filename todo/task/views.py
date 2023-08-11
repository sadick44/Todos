from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Task
from .forms import UserForm


def home(request):
    return render(request, "home.html")


def signup(request):
    form = UserForm
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                user = User.objects.create_user(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
                user.save()
                return redirect('todos/')

    return render(request, "account/signup.html", {'form': form})


@login_required(login_url="login")
def todos(request):
    return render(request, 'todos/todos.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'todos'))

    return render(request, "account/login.html")