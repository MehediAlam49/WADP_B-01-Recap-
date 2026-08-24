from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class custumModel(AbstractUser):
    USER=[
        ('Teacher','Teacher'),
        ('Student','Student')
    ]
    GENDER=[
        ('Male','Male'),
        ('Female','Female')
    ]
    UserType=models.CharField(choices=USER,max_length=100)
    Gender=models.CharField(choices=GENDER,max_length=100)
    Education=models.CharField(max_length=100,null=True)