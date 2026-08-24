from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from authApp.models import *

# Create your views here.

def signup(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        conf_password=request.POST.get('conf_password')
        userType=request.POST.get('userType')
        gender=request.POST.get('gender')
        education=request.POST.get('education')

        if(password==conf_password):
            user=custumModel.objects.create_user(username=username, password=conf_password)
            user.first_name=fname
            user.last_name=lname
            user.email=email
            user.UserType=userType
            user.Gender=gender
            user.Education=education

            user.save()
            return redirect('signin')
        else:
            return redirect('signup')
    

    return render(request, 'signup.html')

def signin(request):
    if request.method=='POST':
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')

        user=authenticate(username=user_name,password=pass_word)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')

    return render(request, 'signin.html')
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def logout_page(request):
    logout(request)
    return redirect('signin')