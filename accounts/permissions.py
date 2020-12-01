from rest_framework import permissions

''' Authenticated User can update own profile'''

class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id