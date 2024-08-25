from django.contrib import admin

from app.core.base_classes.admin import BaseAdminClass
from app.task.models import Sprint, Task


@admin.register(Sprint)
class SprintAdmin(BaseAdminClass):
    list_display = ("title", "state", "created_at", "modified_at")
    list_filter = ("state",)


@admin.register(Task)
class TaskAdmin(BaseAdminClass):
    list_display = ("title", "state", "created_at", "modified_at")
    search_fields = (
        "title",
        "sprint__title",
    )
    list_filter = ("state",)

    raw_id_fields = ("assigned_to", "reviewed_by", "sprint")
