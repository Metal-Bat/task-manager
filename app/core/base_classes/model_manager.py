from django.db.models import Manager


class ActiveModelManager(Manager):
    """perform an only **active** filter on any queryset"""

    def get_queryset(self):
        """override get_queryset to return only **active** list"""

        return super().get_queryset().filter(is_active=True)


class DeletedModelManager(Manager):
    """perform an only **deactivated** filter on any queryset"""

    def get_queryset(self):
        """override get_queryset to return only **deactivated** list"""

        return super().get_queryset().filter(is_active=False)
