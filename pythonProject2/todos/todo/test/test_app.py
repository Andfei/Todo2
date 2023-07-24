from django.test import Client
from django.contrib.auth.models import User
from todo.models import Todo

import pytest


@pytest.fixture
def client():
    return Client()


@pytest.fixture()
def test_data():

        user1 = User.objects.create_user(
            username='lena',
            email='lena@gmail.com',
            password='12345',
            is_active=True
        ),
        user2 = User.objects.create_user(
            username='andrew',
            email='andrew@gmail.com',
            password='12345',
            is_active=True
        ),
        user3 = User.objects.create_user(
            username='olga',
            email='olga@gmail.com',
            password='12345',
            is_active=True
        ),
        user4 = User.objects.create_user(
            username='valeria',
            email='valeria@gmail.com',
            password='12345',
            is_active=True
        ),
        user5 = User.objects.create_user(
            username='tom',
            email='tom@gmail.com',
            password='12345',
            is_active=True
        )
