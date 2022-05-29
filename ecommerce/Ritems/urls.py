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
     path('login', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('changepassword', generic_based_view.UserChangePassword.as_view(), name='changepassword'),
    path('resetpasswordemail', generic_based_view.UserResetPasswordEmail.as_view(), name='resetpasswordemail'),
    path('resetpassword/<str:id>/<str:token>', generic_based_view.UserResetPassword.as_view(), name='resetpassword'),
    path('groups', generic_based_view.GroupPermission.as_view(), name='groups'),
    path('groups/<int:pk>', generic_based_view.GroupPermissionDetail.as_view(), name='group'),
    path('addtocart', generic_based_view.AddToCartView.as_view(), name='addtocart'),
    path('order/<int:id>', generic_based_view.OrderView.as_view(), name='order'),
]
urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  
]
