from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from items.models import Categories
from api.serializers import CategoriesListSerializers

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from.pagination import MyLimitOffsetPagination


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