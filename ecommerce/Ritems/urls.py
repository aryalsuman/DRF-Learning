from django.urls import path, include, re_path
from . import api_based_view
from . import views
from . import generic_based_view


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('categories', generic_based_view.CategoriesList.as_view(), name='categories'),
    path('categories/<int:pk>', generic_based_view.CategoriesDetail.as_view(), name='category'),
    path('products', generic_based_view.ProductsList.as_view(), name='products'),
    path('products/<int:pk>', generic_based_view.ProductDetail.as_view(), name='product'),
    path('register', generic_based_view.RegisterUser.as_view(), name='register'),
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login', generic_based_view.LoginUser.as_view(), name='login'),
]
urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  
]
