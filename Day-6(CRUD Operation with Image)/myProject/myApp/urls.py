from django.urls import path
from myApp.views import *

urlpatterns = [
    path('', student, name='student'),
    path('add-student/', addStudent, name='addStudent'),
    path('edit-student/<str:id>', editStudent, name='editStudent'),
    path('delete-student/<str:id>', deleteStudent, name='deleteStudent'),
    path('view-student/<str:id>', viewStudent, name='viewStudent'),
]
