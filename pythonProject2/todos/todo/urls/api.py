from django.urls import path
from todo.views.api import todo, todo_one

urlpatterns = [
    path('', todo),
    path('<int:todo_id>', todo_one)
]