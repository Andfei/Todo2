
from django.contrib.auth.models import User

from .models import Todo


def create_initial_db():
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