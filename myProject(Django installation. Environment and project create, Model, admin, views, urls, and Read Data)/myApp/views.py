from django.shortcuts import render,redirect
from myApp.models import *

# Create your views here.
def studentList(request):
    student_data=studentModel.objects.all()
    context={
        'student_data':student_data
    }
    return render(request, 'student-list.html',context)

def addStudent(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        student=studentModel(
            name=name,
            address=address,
            phone=phone

        )
        student.save()
        return redirect('studentList')
    return render(request, 'add-student.html')