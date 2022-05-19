from rest_framework import permissions

class CustomerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='customer').exists()  or request.user.is_superuser:
            return True
        else:
            return False
        
class VendorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if request.user.groups.filter(name='vendor').exists() or request.user.is_superuser:
            
            return True
        else:
            return False
        
