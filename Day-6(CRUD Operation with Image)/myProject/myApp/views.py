from django.shortcuts import render,redirect
from myApp.models import *
# Create your views here.
def student(request):
    student=studentModel.objects.all()

    context={
        'student':student
    }
    return render(request, 'student.html',context)

def addStudent(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        department=request.POST.get('department')
        city=request.POST.get('city')
        profilePicture=request.FILES.get('profilePicture')

        student=studentModel(
            FirstName=fname,
            LastName=lname,
            Department=department,
            City=city,
            ProfilePicture=profilePicture,
        )
        student.save()
        return redirect('student')

    return render(request, 'addStudent.html')

def editStudent(request,id):
    student=studentModel.objects.get(id=id)
    if request.method=='POST':
        student.FirstName=request.POST.get('fname')
        student.LastName=request.POST.get('lname')
        student.Department=request.POST.get('department')
        student.City=request.POST.get('city')

        if request.FILES.get('profilePicture'):
            student.ProfilePicture=request.FILES.get('profilePicture')
        student.save()
        return redirect('student')

    context={
        'student':student
    }
    return render(request, 'editStudent.html',context)


def deleteStudent(request,id):
    student=studentModel.objects.get(id=id)
    student.delete()
    return redirect('student')


def viewStudent(request,id):
    student=studentModel.objects.get(id=id)
    context={
        'student':student
    }
    return render(request, 'viewStudent.html',context)