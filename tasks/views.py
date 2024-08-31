from django.shortcuts import render, redirect
from tasks.models import Category, Task
from tasks.form import TaskForm


def main_view(request):
    if request.method == 'GET':
        return render(request, 'main.html')


def ListView(request):
    if request.method == 'GET':
        task = Task.objects.all()
        return render(request, 'tasks/tasks_list.html', {'task': task})

def DatailView(request, task_id):
    if request.method == 'GET':
        task = Task.objects.get(id=task_id)
        return render(request, 'tasks/task_detail.html', context={"task": task})

def CreateView(request):
    if request.method == 'GET':
        form = TaskForm
        return render(request, 'tasks/task_create.html', context={"form": form})
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'tasks/task_create.html', context={"form": form})
        title = form.cleaned_data.get('title')
        description = form.cleaned_data.get('description')
        category = form.cleaned_data.get('category')
        Task.objects.create(
            title=title,
            description=description,
            category=category
        )
        return redirect("/tasks/")