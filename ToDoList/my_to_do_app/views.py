from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import  reverse
from .models import *

# Create your views here.
def index(request) :
    #todos = Todo.objects.all()
    todos  = Todo.objects.filter(isDone=False)
    content = {'todos' : todos}
    #return HttpResponse("my_to_to_app first page")
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request) :
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("create Todo를 할 거야 ! =>"+user_input_str)

def finishTodo(request) :
    done_todo_id = request.GET['todoNum']
    todo = Todo.objects.get(id = done_todo_id)
    if todo.exists() :
        todo.isDone = True
        todo.save()

#    todo.delete()

    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("create Todo를 할 거야 ! =>"+user_input_str)