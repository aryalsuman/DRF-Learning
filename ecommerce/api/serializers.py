from dataclasses import field
from pyexpat import model
from tkinter.ttk import Style
from rest_framework import serializers
from items.models import Categories, Product, AddToCart, Alluser, Order
from django.contrib.auth import authenticate
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
        
class UserChangePasswordSerializers(serializers.Serializer):
    password=serializers.CharField(max_length=100,style={'input_type':'password'})
    new_password=serializers.CharField(max_length=100,style={'input_type':'password'})
    confirm_password=serializers.CharField(max_length=100,style={'input_type':'password'})
    class Meta:
        fields = ['password','new_password','confirm_password']
    def validate(self,data):
        user=self.context.get('user')
        authenticated_user=authenticate(username=user.username,password=data['password'])
        if authenticated_user is not None:
            if data['new_password'] == data['confirm_password']:
               return data
            else:
                raise serializers.ValidationError("Password and confirm password must be same")
        else:
            raise serializers.ValidationError('Incorrect Password')
        