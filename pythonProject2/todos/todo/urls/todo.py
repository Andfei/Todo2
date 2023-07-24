from django.urls import path
from todo.views.todo import todo, create_todo, update_todo

urlpatterns = [
    path('', todo, name="todo"),
    path('create/', create_todo, name="create_todo"),
    path('update/<int:todo_id>/', update_todo, name="update_todo"),
]