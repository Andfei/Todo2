from todo.models import Todo
from rest_framework import serializers


class Todo_serializers(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Todo
        fields = ["id", "name", "description"]
