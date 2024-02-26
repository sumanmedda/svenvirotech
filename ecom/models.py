from django.db import models
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=40)
    # product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    product_image= models.ImageField(upload_to='images/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=255)
    def __str__(self):
        return self.name
