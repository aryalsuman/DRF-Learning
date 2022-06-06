
from itertools import product
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Alluser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_Vendor = models.BooleanField(default=False)
    
class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    vendor=models.ForeignKey(Alluser,on_delete=models.CASCADE,default=0)
    def __str__(self):
        return self.name
    
class AddToCart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    customer=models.ForeignKey(Alluser,related_name='customer',on_delete=models.CASCADE)
    def __str__(self):
        # a=self.customer.all()
         return self.product.name +'by'+self.customer.username
     
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    customer=models.ForeignKey(Alluser,related_name='Orderofcustomer',on_delete=models.CASCADE)
    vendor=models.ForeignKey(Alluser,related_name='OrderForvendor',on_delete=models.CASCADE)
    city = models.CharField(max_length=100,default=None)
    Payment_Choices = (('COD','Cash On Delivery'),("Wallet",'eSewa'),("Bank",'Bank Transfer'))
    payment=models.CharField(max_length=100,choices=Payment_Choices,default='COD')
    def __str__(self) :
        return self.product.name +'by'+self.customer.username+'to'+self.vendor.username