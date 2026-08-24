from django.db import models

# Create your models here.
class studentModel(models.Model):
    ProfilePicture=models.ImageField(upload_to='Profile-img',null=True)
    FirstName=models.CharField(max_length=100,null=True)
    LastName=models.CharField(max_length=100,null=True)
    Department=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.FirstName}'