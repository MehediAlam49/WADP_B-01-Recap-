from django.urls import path
from tasks.views import *

urlpatterns = [
    path('', register_page, name='register_page'),
    path('login-page/', login_page, name='login_page'),
    path('logout-page/', logout_page, name='logout_page'),
    path('home/', home, name='home'),

    #task
    path('task-list/', taskList, name='taskList'),
    path('add-task/', addTask, name='addTask'),
    path('edit-task/<str:p_id>', editTask, name='editTask'),
    path('delete-task/<str:p_id>', deleteTask, name='deleteTask'),
]
