
from itertools import product
from django.shortcuts import render,HttpResponse

from .custompermission import CustomerPermission,VendorPermission
from items.models import Categories, Product ,AddToCart,Alluser
#DRf imports
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from api.serializers import CategoriesListSerializers,ProductListSerializers, AddToCartSerializers, AlluserSerializers


from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.views import APIView

from django.contrib.auth.models import Group




url='http://localhost'+':'+str(8000)

@api_view(['GET'])

def apiOverview(request):
    api_url={
        "ListCategories":f"{url}/api/categories-list/",
        "ListProducts":f"{url}/api/products-list/",
        "CreateProduct":f"{url}/api/create-product/",
        "CreateCategory":f"{url}/api/create-category/",
        "UpdateProduct":f"{url}/api/update-product/<str:pk>/",
        "UpdateCategory":f"{url}/api/update-category/<str:pk>/",
        "DeleteProduct":f"{url}/api/delete-product/<str:pk>/",
        "DeleteCategory":f"{url}/api/delete-category/<str:pk>/",
        "AddToCart":f"{url}/api/add-to-cart/",
        "ViewCart":f"{url}/api/view-cart/",
        "Register":f"{url}/api/register/",
        
        
        
        
    }
    return Response(api_url)
@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAdminUser])
def categoriesList(request):
    categories=Categories.objects.all()
    serializer=CategoriesListSerializers(categories,many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated,CustomerPermission,VendorPermission])
def productsList(request):
    products=Product.objects.all()
    serializer=ProductListSerializers(products,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAdminUser])
def createCategory(request):
    serializers=CategoriesListSerializers(data=request.data)
    print(serializers)
    print(type(serializers))
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated,VendorPermission])
def createProduct(request):
    serializers=ProductListSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated,VendorPermission])
def updateProduct(request,pk):
    
    data=Product.objects.get(id=pk)
    serializers=ProductListSerializers(instance=data,data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)
    
@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAdminUser])
def updateCategory(request,pk):
    data=Categories.objects.get(id=pk)
    serializers=CategoriesListSerializers(instance=data,data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAdminUser])
def deleteCategory(request,pk):
    data_to=Categories.objects.get(id=pk)
    serializers=CategoriesListSerializers(data_to)
    data_to.delete()
    return Response(serializers.data)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated,VendorPermission])
def deleteProduct(request,pk):
    data_to=Product.objects.get(id=pk)
    serializers=ProductListSerializers(data_to)
    data_to.delete()
    return Response(serializers.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated,CustomerPermission])
def addToCart(request):
    serializer=AddToCartSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)
    
@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated,CustomerPermission])
def viewCart(request):
    cart=AddToCart.objects.all()
    serializer=AddToCartSerializers(cart,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication])
def register(request):
    user=Alluser.objects.create_user(**request.data)
    if user.is_customer:
        user.groups.add(Group.objects.get(name='customer'))
    user.save()
    serializer=AlluserSerializers(user)
    return Response(serializer.data)    

#view for palce order
# @api_view(['POST'])
# @authentication_classes([SessionAuthentication])
# def placeOrder(request):
    