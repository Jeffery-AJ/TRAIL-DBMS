from django.shortcuts import render
from .models import TodoItem
# Create your views here.
def home(request):
    return render(request, 'myapp/hello_world.html')
def todos(request):
    items = TodoItem.objects.all()
    return render(request, 'myapp/todos.html', {"todos": items})
   