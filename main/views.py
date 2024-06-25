from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, TaskForm
from .models import Task

def home_view(request):
    return render(request, 'main/dashboard.html')  


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)  # Hash the password
            user.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'main/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_by = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'main/add_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'main/task_list.html', {'tasks': tasks})






