from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskManageForm
from django.http import HttpResponseForbidden

def task_list(request):
    tasks = Task.objects.all()
    create_form = TaskManageForm() # Форма для створення задач

    if request.method == 'POST':
        task_id = request.POST.get('task_id')  # Отримуємо ідентифікатор завдання
        task = get_object_or_404(Task, id=task_id)  # Отримуємо завдання для редагування
        form = TaskManageForm (request.POST, instance=task)  # Створюємо форму для цього завдання

        if form.is_valid():
            form.save()  # Зберігаємо зміни
            return redirect('todoapp:task_list')  # Перенаправляємо на ту саму сторінку після збереження
    else:
        task_form_list = []
        for task in tasks:
            form = TaskManageForm(instance=task) # Створюємо форму для кожної задачі
            task_form_list.append((task, form))

    return render(request, 'todoapp/tasks/list.html', { # Передаємо список завдань і форму до шаблону
        'task_form_list': task_form_list,
        'create_task_form': create_form
        }) 

def task_create(request):
    if request.method == 'POST':
        form = TaskManageForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('todoapp:task_list')
        else:
            return HttpResponseForbidden("You don't have permission to create task.")
    return render(request, 'todoapp/tasks/create.html', {'form': form})


def task_delete(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        if request.user == task.author: # Перевірка на права доступу
            task.delete()
            return redirect('todoapp:task_list')
        else:
            return HttpResponseForbidden("You don't have permission to delete this task.")
    else:
        return HttpResponseForbidden("Invalid request.")
