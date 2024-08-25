from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.core.base_classes.models import BaseModel


class User(AbstractUser, BaseModel):
    """Base User model for user management"""

    first_name = models.CharField(
        _("USER_MODEL_FIRST_NAME"),
        help_text=_("USER_MODEL_FIRST_NAME_HELP_TEXT"),
        max_length=255,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        _("USER_MODEL_LAST_NAME"),
        help_text=_("USER_MODEL_LAST_NAME_HELP_TEXT"),
        max_length=255,
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        _("USER_MODEL_AVATAR"),
        help_text=_("USER_MODEL_AVATAR_HELP_TEXT"),
        upload_to="user_avatar",
        blank=True,
        null=True,
    )
    description = models.TextField(
        _("USER_MODEL_DESCRIPTION"),
        help_text=_("USER_MODEL_DESCRIPTION_HELP_TEXT"),
        blank=True,
        null=True,
    )
    mobile = models.CharField(
        _("USER_MODEL_MOBIL"),
        help_text=_("USER_MODEL_MOBIL_HELP_TEXT"),
        max_length=255,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        _("USER_MODEL_EMAIL"),
        help_text=_("USER_MODEL_EMAIL_HELP_TEXT"),
        max_length=255,
        blank=True,
        null=True,
    )

    def get_full_name(self) -> str:
        """return fullname of user

        Returns:
            str: fullname
        """
        name: str = f"{self.first_name} {self.last_name}"
        return name

    def get_list_of_groups(self) -> list[str]:
        """return user groups

        Returns:
            list[str]: list of user groups
        """
        groups_list: list[str] = self.groups.all().order_by("id").cache().values_list("name", flat=True)
        return groups_list
