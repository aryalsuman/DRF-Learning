from django.urls import path
from . import api_based_view
from . import views
from . import generic_based_view
urlpatterns = [
    path('categories', generic_based_view.CategoriesList.as_view(), name='categories'),
    path('categories/<int:pk>', generic_based_view.CategoriesDetail.as_view(), name='category'),
    
    
]
