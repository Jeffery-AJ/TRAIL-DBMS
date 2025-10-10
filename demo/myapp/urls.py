from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # URL pattern for the home view
    path("todos/", views.todos, name="todos")  # URL pattern for the todos view
]