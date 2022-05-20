from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from items.models import Categories, Product, AddToCart, Alluser, Order

class CategoriesListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields = '__all__'
class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class AddToCartSerializers(serializers.ModelSerializer):
    class Meta:
        model = AddToCart
        fields = '__all__'
        
class AlluserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alluser
        fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class RegisterUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alluser
        fields = ['username','password','is_customer','is_Vendor']
        
class LoginUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alluser
        fields = ['username','password']