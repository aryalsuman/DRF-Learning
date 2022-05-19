from rest_framework import serializers
from items.models import Categories, Product, AddToCart, Alluser, Order

from Ritems.models import ProductofR
class CategoriesListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields = '__all__'
class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductofR
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