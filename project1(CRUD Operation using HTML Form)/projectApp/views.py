from django.shortcuts import render,redirect
from projectApp.models import *

# Create your views here.
def studentList(request):
    student_data=studentModel.objects.all()

    context={
        'student_data':student_data
    }
    return render(request, 'student_list.html',context)

def add_student(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        age=request.POST.get('age')
        phone=request.POST.get('phone')

        student=studentModel(
            name=name,
            address=address,
            age=age,
            phone=phone,
        )
        student.save()
        return redirect('studentList')
    return render(request, 'add_student.html')

def editStudent(request,myid):
    student=studentModel.objects.get(id=myid)
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        age=request.POST.get('age')
        phone=request.POST.get('phone')

        student=studentModel(
            id=myid,
            name=name,
            address=address,
            age=age,
            phone=phone
        )
        student.save()
        return redirect('studentList')
    context={
        'student':student
    }
    return render(request, 'edit_student.html',context)

def deleteStudent(request,myid):
    student=studentModel.objects.get(id=myid)
    student.delete()
    return redirect('studentList')

def viewStudent(request,myid):
    student=studentModel.objects.get(id=myid)

    context={
        'student':student
    }
    return render(request, 'view_student.html',context)


# --------Teacher 
def teacherList(request):
    teacher_data=teacherModel.objects.all()

    context={
        'teacher_data':teacher_data
    }
    return render(request, 'teacher_list.html',context)

def add_teacher(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        age=request.POST.get('age')
        phone=request.POST.get('phone')

        teacher=teacherModel(
            name=name,
            address=address,
            age=age,
            phone=phone,
        )
        teacher.save()
        return redirect('teacherList')
    return render(request, 'add_teacher.html')


def editTeacher(request,myid):
    teacher=teacherModel.objects.get(id=myid)
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        age=request.POST.get('age')
        phone=request.POST.get('phone')

        teacher=teacherModel(
            id=myid,
            name=name,
            address=address,
            age=age,
            phone=phone
        )
        teacher.save()
        return redirect('teacherList')
    context={
        'teacher':teacher
    }
    return render(request, 'edit_teacher.html',context)


def deleteTeacher(request,myid):
    teacher=teacherModel.objects.get(id=myid)
    teacher.delete()
    return redirect('teacherList')

def viewTeacher(request,myid):
    teacher=teacherModel.objects.get(id=myid)

    context={
        'teacher':teacher
    }
    return render(request, 'view_teacher.html',context)