import django_filters
from django.core.exceptions import ValidationError

from app.task.models import Sprint, Task


class SprintFilter(django_filters.FilterSet):
    ids = django_filters.BaseInFilter(field_name="id", lookup_expr="in")
    ordering = django_filters.filters.OrderingFilter(
        fields=(
            ("title", "title"),
            ("created_at", "created_at"),
            ("modified_at", "modified_at"),
        ),
        field_labels={
            "title": "Title",
            "created_at": "Created At",
            "modified_at": "Modified At",
        },
    )

    class Meta:
        model = Sprint
        fields: dict[str, list[str]] = {
            "title": ["exact", "icontains"],
            "created_at": ["exact", "lte", "gte"],
            "modified_at": ["exact", "lte", "gte"],
            "state": ["exact", "icontains"],
        }


class TaskFilter(django_filters.FilterSet):
    ids = django_filters.BaseInFilter(field_name="id", lookup_expr="in")
    sprint = django_filters.NumberFilter(required=True)
    ordering = django_filters.filters.OrderingFilter(
        fields=(
            ("title", "title"),
            ("created_at", "created_at"),
            ("modified_at", "modified_at"),
        ),
        field_labels={
            "title": "Title",
            "created_at": "Created At",
            "modified_at": "Modified At",
        },
    )

    class Meta:
        model = Task
        fields: dict[str, list[str]] = {
            "title": ["exact", "icontains"],
            "created_at": ["exact", "lte", "gte"],
            "modified_at": ["exact", "lte", "gte"],
            "state": ["exact", "icontains"],
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "sprint" not in self.data:
            raise ValidationError("The 'sprint' filter is required.")
