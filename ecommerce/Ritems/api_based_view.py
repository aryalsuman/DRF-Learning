from tokenize import Name
from unicodedata import name
from rest_framework.views import APIView
from items.models import Categories, Product, AddToCart, Alluser, Order
from rest_framework.response import Response
from rest_framework import status
from api.serializers import CategoriesListSerializers,ProductListSerializers, AddToCartSerializers, AlluserSerializers
from rest_framework.filters import SearchFilter, OrderingFilter
class CategoriesList(APIView):
    def get(self, request):
        print(request.query_params.get('name'))
        if request.query_params.get('name'):
            name=request.query_params['name']
            categories=Categories.objects.filter(name__iexact=name)
        else:
            categories=Categories.objects.all()
        # categories = Categories.objects.all()
        serializer = CategoriesListSerializers(categories, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategoriesListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoriesDetail(APIView):
    def get_object(self, pk):
        try:
            return Categories.objects.get(pk=pk)
        except Categories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        categories = self.get_object(pk)
        serializer = CategoriesListSerializers(categories)
        return Response(serializer.data)
    def put(self, request, pk):
        categories = self.get_object(pk)
        serializer = CategoriesListSerializers(instance=categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        categories = self.get_object(pk)
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)