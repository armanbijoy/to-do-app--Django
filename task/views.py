from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    
    taskform = TaskForm()
    search = SearchForm( request.GET,queryset=tasks)
    tasks = search.qs
    if request.method == "POST":
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            taskform.save()
            
            return redirect('/')
            
    context = {'tasks':tasks, 'taskform': taskform, 'search': search}
    
    return render(request,'task/list.html',context)

def updateTask(request, pk):
    items = Task.objects.get(id=pk)
    taskform = TaskForm(instance=items)
    
    if request.method=='POST':
        taskform = TaskForm(request.POST, instance = items)
        if taskform.is_valid():
            taskform.save()
            return redirect('/')
    
    context = {'items': items, 'taskform': taskform}
    
    return render(request,'task/update.html', context)

def deleteTask(request,pk):
    
    item = Task.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect('/')
    
    context = {'item':item}
    
    return render(request,'task/delete.html',context )
    