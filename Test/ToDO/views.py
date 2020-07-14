from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import *
from django.contrib import messages

# Create your views here.
def item_to_do(request):
    context={'todo_list' : Todo.objects.all()}
    return render(request,'ToDo/Index.html',context)
def list_of_item(request):
    if request.method == "POST":
        contents = request.POST.get('contents')
        if len(contents)==0:
            messages.error(request,"safjhfsajfd")
        else:
            todo = Todo(content=contents)
            todo.save()
            messages.success(request,"Yaad Se Krlena Kaam")
        return redirect('/')
def todo_done(request,todo_id):
    todo_delete= Todo.objects.get(id=todo_id)
    todo_delete.delete()
    return redirect('/')



