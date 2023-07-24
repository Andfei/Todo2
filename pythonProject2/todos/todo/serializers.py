from todo.models import Todo
from rest_framework import serializers


class TodoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Todo
        fields = ["id", "name", "description"]
