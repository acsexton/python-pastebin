from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission allowing only owners of a snippet to edit.
    """

    def has_object_permission(self, request, view, obj):
        # Always allow GET, HEAD, or OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow write permissions for the owner of a snippet
        return obj.owner == request.user
