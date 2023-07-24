import random
import datetime
from time import sleep
from celery import shared_task

from todo.models import Todo
from todo.utils import build_generator, generate_text
from todos.celery import app

@shared_task()
def logging_task(params=None):
    print(params)
    sleep(10)

@app.task
def create_todo():
    todos = Todo.objects.all()
    for todo in todos:
        generator = build_generator()
        for _ in range(random.randint(4, 200)):
            Todo(
                name=generate_text(generator, random.randint(1, 20)),
                description=generate_text(generator, random.randint(1, 100)),
                user=generate_text(generator, random.randint(1, 100)),
            ).save()

