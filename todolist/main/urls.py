from django.urls import path, include
from .views import *
from rest_framework import routers
# router = routers.SimpleRouter()
# router.register(r'', ToDoViewSet)
urlpatterns = [
    path('auto', include('rest_framework.urls')),
    path('<int:pk>/', UpdateTodo.as_view()),
    path('create', CreateTodo.as_view()),
    path('', ListTodo.as_view()),
    path('delete/<int:pk>', DeleteTodo.as_view())
    # path('', include(router.urls)),
]
     