from django.shortcuts import render
from tasks.models import Tasks
from rest_framework import viewsets
from rest_framework.decorators import action
from django.views.generic import ListView
from rest_framework import generics
from .forms import TaskForm


def task_list(request,status=None):
    if status:
        tasks = Tasks.objects.filter(status=status)
    else:
        tasks = Tasks.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
'''def task_list_status(request, status=None):
    if status:
        tasks = Task.objects.filter(status=status)
    else:
        tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})'''
def task_detail(request,pk):
    task=get_object_or_404(Tasks,pk=pk)
    return render(request,'tasks/task_detail.html',{'task':task})
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
    

    
    


