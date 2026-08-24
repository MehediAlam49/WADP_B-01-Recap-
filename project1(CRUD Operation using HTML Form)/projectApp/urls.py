from django.urls import path
from projectApp.views import *

urlpatterns = [
    path('', studentList, name='studentList'),
    path('add-student/', add_student, name='add_student'),
    path('edit-student/<str:myid>', editStudent, name='editStudent'),
    path('delete-student/<str:myid>', deleteStudent, name='deleteStudent'),
    path('view-student/<str:myid>', viewStudent, name='viewStudent'),

    # ------Teacher
    path('teacher/',teacherList, name='teacherList'),
    path('add-teacher/', add_teacher, name='add_teacher'),
    path('edit-teacher/<str:myid>', editTeacher, name='editTeacher'),
    path('delete-teacher/<str:myid>', deleteTeacher, name='deleteTeacher'),
    path('view-teacher/<str:myid>', viewTeacher, name='viewTeacher'),
]
