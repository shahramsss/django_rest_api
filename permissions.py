from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadonly(BasePermission):
    message = "Permission denied: you are not the owner!"

    def has_permission(self, request, view):
        # اطمینان از اینکه کاربر احراز هویت شده است
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # اجازه دسترسی به همه برای متدهای امن (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True

        # بررسی اینکه آیا شیء دارای فیلد user هست و مالک آن با کاربر برابر است
        return hasattr(obj, "user") and obj.user == request.user
