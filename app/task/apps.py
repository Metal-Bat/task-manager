from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TaskConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.task"
    verbose_name = _("TASKS")
