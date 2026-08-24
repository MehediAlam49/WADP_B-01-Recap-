from django.urls import path
from authApp.views import *

urlpatterns = [
    path('', signup, name='signup'),
    path('signin/', signin, name='signin'),
]
