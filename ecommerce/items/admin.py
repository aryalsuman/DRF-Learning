from atexit import register
from django.contrib import admin
from items.models import Categories, Product,AddToCart,Alluser,Order
from django.contrib.auth.models import User
# Register your models here.
admin.site.register([Categories, Product, AddToCart])
admin.site.register(Order)


from django.contrib.auth.admin import UserAdmin

from .models import Alluser

class CustomUserAdmin(UserAdmin):
        model=User
        list_display= ("username","is_customer","is_Vendor")
        fieldsets=(
            (None,{'fields':('username','password')}),
            ("User Profile",{'fields':('is_customer','is_Vendor')}),
            ("Permissions",{'fields':('is_staff','is_superuser')}),
            ("Advanced OPtions",{'fields':('groups','user_permissions')}),
            ("Users Info",{'fields':('first_name','last_name','email')}),
        )


admin.site.register(Alluser, CustomUserAdmin)