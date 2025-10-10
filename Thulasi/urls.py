from django.urls import path
from .views import home, todos

urlpatterns = [
    path('',home,name="home"),
    path('todos/',todos,name="todos"),
]