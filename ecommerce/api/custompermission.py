from rest_framework import permissions

class CustomerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_customer  or request.user.is_superuser:
            return True
        else:
            return False
        
class VendorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if request.user.is_Vendor or request.user.is_superuser:
            
            return True
        else:
            return False
        
