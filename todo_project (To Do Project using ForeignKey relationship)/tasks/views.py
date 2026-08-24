from django.shortcuts import render,redirect,get_object_or_404
from tasks.models import *
from tasks.forms import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

#user
def register_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        conf_password=request.POST.get('conf_password')

        if password==conf_password:
            CustomUserModel.objects.create_user(
                username=username,
                full_name=full_name,
                email=email,
                password=password
            )
            return redirect('login_page')
    return render(request, 'register_page.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login_page.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

def home(request):
    return render(request, 'home.html')




#task
def taskList(request):
    task_data=TaskModel.objects.filter(Created_by=request.user)

    context={
        'task_data':task_data
    }
    return render(request, 'taskList.html',context)

def addTask(request):
    #to save data in database
    if request.method=='POST':
        form_data=TaskForm(request.POST)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.Created_by=request.user
            data.save()
            return redirect('taskList')

    
    #to show form in html page
    form_data=TaskForm()
    context={
        'form_data':form_data,
        'form_heading':'Add task form',
        'form_btn': 'Add task'
    }
    return render(request, 'master/base-form.html',context)


def editTask(request,p_id):
    task_data=TaskModel.objects.get(id=p_id)

    #to save data in database
    if request.method=='POST':
        form_data=TaskForm(request.POST, instance=task_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.Created_by=request.user
            data.save()
            return redirect('taskList')

    #to show form in html page
    form_data=TaskForm(instance=task_data)
    context={
        'form_data':form_data,
        'form_heading':'Edit task form',
        'form_btn': 'update task'
    }
    return render(request, 'master/base-form.html',context)


def deleteTask(request,p_id):
    task_data=TaskModel.objects.get(id=p_id)
    task_data.delete()

    return redirect('taskList')