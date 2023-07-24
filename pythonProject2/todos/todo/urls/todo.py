from django.urls import path
from todo.views.todo import todos, create_todo, update_todo

urlpatterns = [
    path('', todos, name="todos"),
    path('create/', create_todo, name="create_todo"),
    path('update/<int:todo_id>/', update_todo, name="update_todo"),
]