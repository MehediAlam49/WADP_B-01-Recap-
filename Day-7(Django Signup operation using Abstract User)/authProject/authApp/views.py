from django.shortcuts import render,redirect
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
    return render(request, 'signin.html')