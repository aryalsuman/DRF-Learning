from traceback import print_tb
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView,CreateAPIView
from items.models import Categories,Product,AddToCart,Alluser,Order
from api.serializers import CategoriesListSerializers,ProductListSerializers, AddToCartSerializers, AlluserSerializers, OrderSerializers,RegisterUserSerializers
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
from api.custompermission import CustomerPermission,VendorPermission
from django.contrib.auth.hashers import make_password



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
    permission_classes = [IsAdminUser]
    
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
    permission_classes = [VendorPermission]
    

class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializers
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        password=make_password(request.data.get('password'))

        if serializer.is_valid():
            # serializer.data.get('password')=make_password(serializer.data.get('password'))
            
            # serializer.save()
            serializer.save(password=password)
            user=Alluser.objects.get(username=request.data['username'])
            
            if user.is_customer==True:
                group=Group.objects.get(name='customer')
                user.groups.add(group)
            if user.is_Vendor==True:
                group=Group.objects.get(name='vendor')
                user.groups.add(group)
            token=get_tokens_for_user(user)
            #return serializer.data and token using response
            print(token)
            print(serializer.data)
            return Response({"user":serializer.data,"token":token},status=status.HTTP_201_CREATED) 
                
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class LoginUser(CreateAPIView):
#     serializer_class =LoginUserSerializers
#     def post(self,request):
#         serializer=self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user=authenticate(username=request.data['username'],password=request.data['password'])
#             if user is not None:
#                 token=get_tokens_for_user(user)
#                 return Response({"user":serializer.data,"token":token},status=status.HTTP_200_OK)
#             else:
#                 return Response({"error":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    

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
       
class UserResetPasswordEmail(CreateAPIView):
    serializer_class=serializers.UserResetPasswordEmailSerializers
    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        print(serializer.is_valid(raise_exception=True))
        print(serializer)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
class UserResetPassword(CreateAPIView):
    serializer_class=serializers.UserResetPasswordSerializers
    def post(self, request,id,token):
        serializer=self.serializer_class(data=request.data,context={'id':id,'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({"Message":"Password is reset."},status=status.HTTP_200_OK)
    
class UserPermission(ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user=request.user
        permission=user.get_all_permissions()
        print(permission)
        Response(permission,status=status.HTTP_200_OK)
        
        
class GroupPermission(ListCreateAPIView):
    serializer_class=serializers.GroupSerializers
    queryset=Group.objects.all()
    # permission_classes = [IsAdminUser]
    # def get(self,request):
    #     group=Group.objects.all()
    #     serializer=self.serializer_class(group,many=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    # def post(self,request):
    #     serializer=self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_200_OK)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class GroupPermissionDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.GroupSerializers
    queryset=Group.objects.all()
    # permission_classes = [IsAdminUser]
    # def get(self,request,id):
    #     group=Group.objects.get(id=id)
    #     serializer=self.serializer_class(group)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    # def put(self,request,id):
    #     group=Group.objects.get(id=id)
    #     serializer=self.serializer_class(group,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_200_OK)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # def delete(self,request,id):
    #     group=Group.objects.get(id=id)
    #     group.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
class AddToCartView(ListCreateAPIView):
    serializer_class=serializers.AddToCartSerializers
    permission_classes = [IsAuthenticated]
    def get(self,request):
        cart=AddToCart.objects.filter(customer__username=request.user.username)
        serializer=self.serializer_class(cart,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        customer=Alluser.objects.get(username=request.user.username)
        if AddToCart.objects.filter(customer=customer,product=request.data['product']).exists():
                product=AddToCart.objects.get(customer=customer,product=request.data['product'])
                product.quantity=int(product.quantity)+int(request.data['quantity'])
                product.save()
                return Response({"mes":"Added","data":product.quantity},status=status.HTTP_200_OK)
        if serializer.is_valid():
            customer=Alluser.objects.get(username=request.user.username)
            serializer.save(customer=customer)
            return Response({"mes":"Added","data":serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
    
    
