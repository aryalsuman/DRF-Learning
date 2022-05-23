from traceback import print_tb
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView,CreateAPIView
from items.models import Categories,Product,AddToCart,Alluser,Order
from api.serializers import CategoriesListSerializers,ProductListSerializers, AddToCartSerializers, AlluserSerializers, OrderSerializers,RegisterUserSerializers,LoginUserSerializers
from api import serializers
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from.pagination import MyLimitOffsetPagination
# from api.custompermission import CustomPermission
from items.models import Product,Categories,AddToCart,Alluser,Order
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated,IsAdminUser



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
# from Ritems.models import Product
class CategoriesList(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = MyLimitOffsetPagination
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
    

class CategoriesDetail(RetrieveUpdateDestroyAPIView):
    
    queryset = Categories.objects.all()
    serializer_class = CategoriesListSerializers
    permission_classes = [IsAuthenticated]
    
class ProductsList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = MyLimitOffsetPagination
    filterset_fields = ['name','category']
    search_fields = ['name','category']
    ordering_fields = ['name','category']
    
class ProductDetail(RetrieveUpdateDestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    

class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializers
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=Alluser.objects.get(username=request.data['username'])
            token=get_tokens_for_user(user)
            #return serializer.data and token using response
            print(token)
            print(serializer.data)
            return Response({"user":serializer.data,"token":token},status=status.HTTP_201_CREATED) 
                
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginUser(CreateAPIView):
    serializer_class =LoginUserSerializers
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=authenticate(username=request.data['username'],password=request.data['password'])
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({"user":serializer.data,"token":token},status=status.HTTP_200_OK)
            else:
                return Response({"error":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    

class UserChangePassword(CreateAPIView):
    serializer_class=serializers.UserChangePasswordSerializers
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            user=Alluser.objects.get(username=request.user.username)
            user.set_password(serializer.data['new_password'])
            user.save()
            return Response({"message":"Password Changed Successfully"},status=status.HTTP_200_OK)
       