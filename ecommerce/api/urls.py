from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('categories-list/', views.categoriesList, name='categories-list'),
    path('products-list/', views.productsList, name='products-list'),
    path('create-category/', views.createCategory, name='create-category'),
    path('create-product/', views.createProduct, name='create-product'),
    path('update-product/<str:pk>/', views.updateProduct, name='update-product'),
    path('update-category/<str:pk>/', views.updateCategory, name='update-category'),
    path('delete-category/<str:pk>/', views.deleteCategory, name='delete-category'),
    path('delete-product/<str:pk>/', views.deleteProduct, name='delete-product'),
    path('add-to-cart/', views.addToCart, name='add-to-cart'),
    path('view-cart/', views.viewCart, name='view-cart'),
    path('register/', views.register, name='register'),
    path('api-auth/', include('rest_framework.urls')),
    # path('place-order/<str:pk>/', views.placeOrder, name='place-order'),
    
]