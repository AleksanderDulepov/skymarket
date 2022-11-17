from rest_framework import permissions

from users.models import UserRoles


class OwnerOrAdminPermission(permissions.BasePermission):
    message="You aren'r owner or admin"

    def has_object_permission(self, request, view, obj):
        if (request.user.id==obj.author.id) | (request.user.role==UserRoles.ADMIN):
            return True
        return False
