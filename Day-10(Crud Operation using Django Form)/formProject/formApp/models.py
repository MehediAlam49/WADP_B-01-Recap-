from django.db import models

# Create your models here.
class productModel(models.Model):
    product_name=models.CharField(max_length=100,null=True)
    product_price=models.FloatField(null=True)
    product_description=models.TextField(null=True)
    product_qty=models.PositiveIntegerField(null=True)
    product_img=models.ImageField(upload_to='media/product-imgs')

    def __str__(self):
        return f'{self.product_name}'