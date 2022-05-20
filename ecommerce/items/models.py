
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
    vendor=models.ManyToManyField(Alluser,related_name='vendor')
    def __str__(self):
        return self.name
    
class AddToCart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    customer=models.OneToOneField(Alluser,on_delete=models.CASCADE)
    def __str__(self):
        return self.product.name

# Model for order placed by customer from addtocart 
class Order(models.Model):
    vendor=models.OneToOneField(Alluser,on_delete=models.CASCADE,related_name='vendorfororder')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='productfororder')
    customer=models.ForeignKey(Alluser,on_delete=models.CASCADE,related_name='customerfororder')
    def __str__(self):
        return(str(self.customer)+'to'+str(self.vendor)+'for'+str(self.product))