from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Todo 

@login_required(login_url='login')
def home(request):
    if request.method == "POST":
        task = request.POST['task']
        start = request.POST['start']
        finish = request.POST['finish']
        Todo.objects.create(task=task,start=start,finish=finish,user=request.user)
        return redirect('/')
    todos = Todo.objects.filter(user=request.user)
    context = {
        "todos":todos
    }
    return render(request,'index.html',context=context)

def comuncom(request,id):
    task = Todo.objects.get(id=id)
    task.status = not(task.status)
    task.save()
    return redirect('/')

def delete(request,id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('/')

def update(request,id):
    if request.method == "POST":
        task = request.POST['task']
        start = request.POST['start']
        finish = request.POST['finish']
        todo = Todo.objects.get(id=id)
        todo.task = task
        todo.start = start
        todo.finish = finish
        todo.save()
        return redirect('/')
    task = Todo.objects.get(id=id)
    context = {
        'task':task
    }
    return render(request,'update.html',context=context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST['username']
            psw1 = request.POST['psw1']
            user = authenticate(username=username,password=psw1)
            if user is None:
                messages.error(request, "Bunaqa foydalanuvchi topilmadi!")
                return redirect('/login')
            else:
                login(request,user)
                messages.success(request, "Muvaffaqqiyatli tizimga kirdingiz")
                return redirect('/')     
    return render(request,'login.html')
def registerpage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST['username']
            psw1 = request.POST['psw1']
            psw2 = request.POST['psw2']
            if User.objects.filter(username=username).exists():
                messages.error(request, "Bunaqa foydalanuvchi allaqachon mavjud!")
                return redirect('/register')
            if psw1 != psw2:
                messages.error(request, "Parollar birxil emas")
                return redirect('/register')
            else:
                User.objects.create_user(username=username,password=psw1)
                messages.success(request, "Muvaffaqqiyatli ro'yhatdan o'tdingiz")
                return redirect('/login')        
    return render(request,'register.html')
    