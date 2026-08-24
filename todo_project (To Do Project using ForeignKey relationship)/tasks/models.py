from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    full_name=models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.full_name}'

class TaskModel(models.Model):
    STATUS=[
        ('Pending','Pending'),
        ('Inprogress','Inprogress'),
        ('Completed','Completed')
    ]
    Title=models.CharField(max_length=100,null=True)
    Description=models.TextField(null=True)
    Status=models.CharField(choices=STATUS,null=True,max_length=20)
    Due_date=models.DateField(null=True)
    Created_at=models.DateTimeField(auto_now_add=True)
    Created_by=models.ForeignKey(CustomUserModel, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.Title}'