from rest_framework.request import Request

from app.core.permission import IsStaff


class SprintManger(IsStaff):
    def has_permission(self, request: Request, view: object) -> bool:
        permission: bool = False
        staff_user: bool = super().has_permission(request, view)

        if staff_user:
            permission: bool = "sprint_admin" in request.user.get_list_of_groups()

        return permission


class TaskManger(IsStaff):
    def has_permission(self, request: Request, view: object) -> bool:
        permission: bool = False
        staff_user: bool = super().has_permission(request, view)

        if staff_user:
            permission: bool = "task_admin" in request.user.get_list_of_groups()

        return permission
