from django.db import models

# Create your models here.
class studentModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=20,null=True)

    def __str__(self):
        return f'{self.name}'
