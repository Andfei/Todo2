from todo.models import Todo
from rest_framework import viewsets, filters, generics
from rest_framework import permissions
from todo.serializers import Todo_serializers
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = Todo_serializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["id", "name", "description"]

class TodoDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = Todo_serializers(todo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todos = self.get_object(pk)
        serializer = Todo_serializers(todos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
