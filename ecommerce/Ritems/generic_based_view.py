from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from items.models import Categories
from api.serializers import CategoriesListSerializers,ProductListSerializers

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from.pagination import MyLimitOffsetPagination

from Ritems.models import ProductofR
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
    
class ProductsList(ListCreateAPIView):
    queryset = ProductofR.objects.all()
    serializer_class = ProductListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = MyLimitOffsetPagination
    filterset_fields = ['name','category']
    search_fields = ['name','category']
    ordering_fields = ['name','category']
    
class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = ProductofR.objects.all()
    serializer_class = ProductListSerializers