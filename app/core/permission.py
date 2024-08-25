from rest_framework import permissions
from rest_framework.request import Request


class IsActive(permissions.BasePermission):
    def has_permission(self, request: Request, view: object) -> bool:
        permission: bool = request.user.is_active
        return permission


class IsStaff(IsActive):
    def has_permission(self, request: Request, view: object) -> bool:
        active_user = super().has_permission(request, view)
        permission: bool = active_user and request.user.is_staff
        return permission


class IsSuperAdmin(IsActive):
    def has_permission(self, request: Request, view: object) -> bool:
        active_user = super().has_permission(request, view)
        permission: bool = active_user and request.user.is_staff
        return permission
