from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Checks if user is a profile owner, if not allows access to read-only
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user