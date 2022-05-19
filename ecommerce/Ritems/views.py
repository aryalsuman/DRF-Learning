import imp
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import CategoriesListSerializers,ProductListSerializers, AddToCartSerializers, AlluserSerializers
# Create your views here.
from items.models import Categories, Product, AddToCart, Alluser, Order

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def categories(request,pk=None):
    print(request.method,pk)
    if request.method == 'GET' and pk is None:
        categories = Categories.objects.all()
        serializer = CategoriesListSerializers(categories, many=True)
        
        return Response(serializer.data, status=200)
    if request.method == 'GET' and pk is not None:
        print ("get individual category")
        categories = Categories.objects.get(pk=pk)
        serializer = CategoriesListSerializers(categories)
        return Response(serializer.data, status=200)
        
    if request.method == 'POST' and pk is None:
        serializer = CategoriesListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    if request.method == 'PUT' and pk is not None:
        categories = Categories.objects.get(pk=pk)
        serializer = CategoriesListSerializers(instance=categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    if request.method == 'DELETE' and pk is not None:
        categories = Categories.objects.get(pk=pk)
        categories.delete()
        return Response(status=204)
    