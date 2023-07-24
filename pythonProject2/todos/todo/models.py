from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


