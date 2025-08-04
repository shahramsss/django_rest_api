from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadonly(BasePermission):
    message = "permission denied, you are not owner!"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
