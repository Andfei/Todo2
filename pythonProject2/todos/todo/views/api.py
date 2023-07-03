from django.http import JsonResponse
from django.template.defaulttags import csrf_token
from todo.models import Todo
from django.forms.models import model_to_dict
from todo.forms import TodoForm, TodoUpdateForm


def todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.save()
            return JsonResponse({'posts': model_to_dict(todo)})
        else:
            return JsonResponse({"status":400, 'errors': form.errors})
    todo_dict = [model_to_dict(todo) for todo in Todo.objects.all()]
    return JsonResponse({'posts':  todo_dict})


def todo_one(request, todo_id):
    try:
        todo_obj = Todo.objects.get(id=todo_id)
    except Exception:
        return JsonResponse({'status': 404})

    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo_obj)
        if form.is_valid():
            todo_obj = form.save()
            return JsonResponse({'posts': model_to_dict(todo)})
        else:
            return JsonResponse({"status":400, 'errors': form.errors})
    return JsonResponse({'todo': model_to_dict(todo_obj)})



