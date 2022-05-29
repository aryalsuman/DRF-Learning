from asyncore import read
from dataclasses import field
from lib2to3.pgen2 import token
from pyexpat import model
from tkinter.ttk import Style
from rest_framework import serializers
from items.models import Categories, Product, AddToCart, Alluser, Order
from django.contrib.auth import authenticate

from Ritems.utils import sendEmail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.models import Group,Permission

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
        
# class LoginUserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Alluser
#         fields = ['username','password']
        
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
        
class UserResetPasswordEmailSerializers(serializers.Serializer):
    username=serializers.CharField(max_length=100)
    class Meta:
        fields = ['username']
    
    def validate(self, data):
        
        if Alluser.objects.filter(username=data['username']).exists():
            user=Alluser.objects.get(username=data['username'])
            token=PasswordResetTokenGenerator().make_token(user)
            link="http://localhost:3000/reset_password/"+urlsafe_base64_encode(force_bytes(user.id))+'/'+str(token)
            message_data={
                'subject':'Reset Password',
                'body':'Click on the link to reset your password.'+link,
                'to_email':user.email,
                
            }
            print(sendEmail(message_data))
            return data
            
        else:
            raise serializers.ValidationError("User with this username doesn't exist")
        
class UserResetPasswordSerializers(serializers.Serializer):
    password1=serializers.CharField(max_length=100,style={'input_type':'password'})
    password2=serializers.CharField(max_length=100,style={'input_type':'password'})
    
    class Meta:
        fields = ['password1','password2']
        
    def validate(self,data):
        id=self.context.get('id')
        id=urlsafe_base64_decode(id)
        token=self.context.get('token')
        print("checking TOken")
        user=Alluser.objects.get(id=id)
        if PasswordResetTokenGenerator().check_token(user,token):
            if data['password1']==data['password2']:
                
                user.set_password(data['password1'])
                return data
            else:
                raise serializers.ValidationError("Password and confirm password must be same")
        else:
            raise serializers.ValidationError("Invalid Token")



class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        
class AddToCartSerializers(serializers.ModelSerializer):
    product=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = AddToCart
        fields = ['product','quantity']
        
        
class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'