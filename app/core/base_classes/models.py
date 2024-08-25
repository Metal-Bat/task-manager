from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from app.core.base_classes.model_manager import ActiveModelManager, DeletedModelManager


class BaseModel(models.Model):
    """Abstract model for project base

    - rows
        - created at
        - modified at
        - is active
        - history on item

    - managers
        - active list manger for clear code
        - deactivated list manager for clear code
    """

    created_at = models.DateTimeField(_("ROW_CREATED_AT"), auto_now_add=True)
    modified_at = models.DateTimeField(_("ROW_LAST_MODIFICATION"), auto_now=True)
    is_active = models.BooleanField(_("ROW_ACTIVE"), default=True)

    history = HistoricalRecords(_("ROW_HISTORY"), inherit=True)

    objects = models.Manager()
    active_list = ActiveModelManager()
    deactivated_list = DeletedModelManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def, override]
        self.is_active = False
        self.save()
        return None
