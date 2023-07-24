from django.urls import path, include
from rest_framework import routers
from todo.views.api_v2 import TodoViewSet, TodoDetail
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('/<int:pk>/', TodoDetail.as_view()),
]


