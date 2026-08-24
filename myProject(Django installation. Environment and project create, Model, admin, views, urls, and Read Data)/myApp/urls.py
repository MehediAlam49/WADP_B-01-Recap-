from django.urls import path
from myApp.views import *

urlpatterns = [
    path('', studentList, name='studentList'),
    path('add-student/', addStudent, name='addStudent'),
]
