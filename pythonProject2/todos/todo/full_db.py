from random import random
from .models import Todo
import datetime
import random
from django.contrib.auth.models import User
from .utils import generate_text, build_generator




def create_initial_db(datetime=None):
    users = []
    users.extend([
        User.objects.create_user(
            username='lena',
            email='lena@gmail.com',
            password='12345',
            is_active=True
        ),
        User.objects.create_user(
            username='andrew',
            email='andrew@gmail.com',
            password='12345',
            is_active=True
        ),
        User.objects.create_user(
            username='olga',
            email='olga@gmail.com',
            password='12345',
            is_active=True
        ),
        User.objects.create_user(
            username='valeria',
            email='valeria@gmail.com',
            password='12345',
            is_active=True
        ),
        User.objects.create_user(
            username='tom',
            email='tom@gmail.com',
            password='12345',
            is_active=True
        )
    ])

    todos = []
    for user in users:
        todo = Todo(
            name=f"{user.username}'s todo",
            author=user,
            created_date=datetime.date.today().replace(
                year=random.randint(2005, 2023),
                month=random.randint(1, 12),
                day=random.randint(1, 28)
            )
        )
        todo.save()
        todos.append(todo)

    for todo in todos:
        generator = build_generator()
        for _ in range(random.randint(4, 200)):
            Todo(
                name = generate_text(generator, random.randint(1, 20)),
                description = generate_text(generator, random.randint(1, 100)),
                user = generate_text(generator, random.randint(1, 100)),
            ).save()