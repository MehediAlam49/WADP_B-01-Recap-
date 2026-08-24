from django.urls import path
from authApp.views import *

urlpatterns = [
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_page, name='logout_page'),
]
