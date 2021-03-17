from django.shortcuts import render, redirect
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
            messages.success(request, "New task added!")
            return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        context = {
            'all_tasks': all_tasks,
        }
        return render(request, 'todolist.html', context)


def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated")
            return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        context = {
            'task_obj': task_obj,
        }
        return render(request, 'edit.html', context)


@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.success(request, "You are not authorized")
    return redirect('todolist')


@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.success(request, "You are not authorized")
    return redirect('todolist')


def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')


def contact(request):
    context = {
        'contact_text': "Welcome to contact us page",
    }
    return render(request, 'contact.html', context)


def index(request):
    context = {
        'index_text': "Welcome to Index page",
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'about_text': "Welcome to about us page",
    }
    return render(request, 'about.html', context)
