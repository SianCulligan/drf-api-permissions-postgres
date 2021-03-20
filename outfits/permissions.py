from rest_framework import permissions
import rest_framework

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.outfit_wearer is None:
            return True
        
        return obj.outfit_wearer == request.user
