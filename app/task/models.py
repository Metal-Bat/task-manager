from django.db import models
from django.utils.translation import gettext_lazy as _

from app.core.base_classes.models import BaseModel
from app.user.models import User


class Sprint(BaseModel):
    """
    Sprint management model

    **filed list:**
    - title
    - state
    """

    class SprintState(models.TextChoices):
        BACKLOG = "BACKLOG"
        ACTIVE = "ACTIVE"
        FUTURE = "FUTURE"

    title = models.CharField(
        _("SPRINT_MODEL_TITLE"),
        help_text=_("SPRINT_MODEL_TITLE_HELP_TEXT"),
        max_length=255,
        unique=True,
    )
    state = models.CharField(
        _("SPRINT_MODEL_STATE"),
        help_text=_("SPRINT_MODEL_STATE_HELP_TEXT"),
        max_length=255,
        choices=SprintState,
        default=SprintState.FUTURE,
    )

    def __str__(self) -> str:
        """return sprint name

        Returns:
            str: sprint task
        """
        name: str = f"{self.title!r} - {self.state!r}"
        return name


class Task(BaseModel):
    """
    Task management model

    **filed list:**
    - title
    - sprint
    - state
    - assigned_to
    - reviewed_by
    - due_date
    """

    class TaskState(models.TextChoices):
        PEND = "PEND"
        TO_DEVELOP = "TO_DEVELOP"
        DEVELOPING = "DEVELOPING"
        TO_REVIEW = "TO_REVIEW"
        APPROVED = "APPROVED"
        TO_TEST = "TO_TEST"
        DELIVERED = "DELIVERED"

    title = models.CharField(
        _("TASK_MODEL_TITLE"),
        help_text=_("TASK_MODEL_SPRINT_HELP_TEXT"),
        max_length=255,
    )
    sprint = models.ForeignKey(
        Sprint,
        verbose_name=_("TASK_MODEL_SPRINT"),
        help_text=_("TASK_MODEL_SPRINT_HELP_TEXT"),
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    state = models.CharField(
        _("TASK_MODEL_STATE"),
        help_text=_("TASK_MODEL_STATE_HELP_TEXT"),
        max_length=255,
        choices=TaskState,
        default=TaskState.TO_DEVELOP,
    )
    assigned_to = models.ForeignKey(
        User,
        verbose_name=_("TASK_MODEL_ASSIGNED_TO"),
        help_text=_("TASK_MODEL_ASSIGNED_TO_HELP_TEXT"),
        related_name="assigned",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    reviewed_by = models.ForeignKey(
        User,
        verbose_name=_("TASK_MODEL_REVIEWED_BY"),
        help_text=_("TASK_MODEL_REVIEWED_BY_HELP_TEXT"),
        related_name="reviews",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    due_date = models.DateTimeField(
        _("TASK_MODEL_DUE_DATE"),
        help_text=_("TASK_MODEL_DUE_DATE_HELP_TEXT"),
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        """name of task

        Returns:
            str: contain task name and state
        """
        name: str = f"{self.sprint!r} - {self.title!r} {self.state}"
        return name
