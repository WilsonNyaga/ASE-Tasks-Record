from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Task, BlogPost
from datetime import datetime
from .forms import TaskForm

from django.shortcuts import render


def home_view(request):
    # You can perform any necessary logic here
    # For example, fetch data from your database

    # Render a template and return an HTTP response
    # Replace 'tasks/home.html' with your actual template path
    return render(request, 'tasks/home.html')


# User registration view


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the login page after successful registration
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Profile related views


@login_required
def profile_view(request):
    # Implement your profile view logic here
    return render(request, 'tasks/profile.html')


@login_required
def edit_profile_view(request):
    # Implement your edit profile view logic here
    return render(request, 'tasks/edit_profile.html')

# Task-related views


@login_required
def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/view_tasks.html', {'tasks': tasks})


@login_required
def search_tasks(request):
    # Implement your search tasks view logic here
    return render(request, 'tasks/search_tasks.html')


@login_required
def add_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.date = datetime.now()
            task.save()
            return redirect('view_tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})


@login_required
def edit_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'task': task, 'form': form})


@login_required
def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('view_tasks')
    return render(request, 'tasks/delete_task.html', {'task': task})

# Blog related views


@login_required
def blog_view(request):
    blog_posts = BlogPost.objects.all().order_by('-date_published')[:5]
    return render(request, 'tasks/blog.html', {'blog_posts': blog_posts})


@login_required
def view_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    # Implement your view post view logic here
    return render(request, 'tasks/view_post.html', {'post': post})


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    # Implement your add comment view logic here
    return render(request, 'tasks/add_comment.html', {'post': post})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    # Implement your edit post view logic here
    return render(request, 'tasks/edit_post.html', {'post': post})
