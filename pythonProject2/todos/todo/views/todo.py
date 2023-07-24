from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from todo.forms import TodoForm, TodoUpdateForm
from todo.models import Todo




@cache_page(60 * 15)
def todo(request):
    return render(request, "todos.html", {"todo": Todo.objects.all()})

def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect("todo")
        else:
            render(request, "create_todo.html", {"form": form})
    return render(request, "create_todo.html", {"form": TodoForm})

def update_todo(request, todo_id):
    try:
        todo_obj = Todo.objects.get(id=todo_id)
    except Exception:
        return JsonResponse({'status': 404})

    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo_obj)
        if form.is_valid():
            todo_obj = form.save()
    return render(request, "update_todo.html", {"form": form})


