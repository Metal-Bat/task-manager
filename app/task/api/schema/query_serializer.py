from rest_framework import serializers


class SprintFilterSchema(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    title__icontains = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    created_at__lte = serializers.DateTimeField(required=False)
    created_at__gte = serializers.DateTimeField(required=False)
    modified_at = serializers.DateTimeField(required=False)
    modified_at__lte = serializers.DateTimeField(required=False)
    modified_at__gte = serializers.DateTimeField(required=False)
    state = serializers.CharField(required=False)
    state__icontains = serializers.CharField(required=False)
    ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
    )
    ORDERING_CHOICES: list[tuple[str, str]] = [
        ("title", "Title (ascending)"),
        ("-title", "Title (descending)"),
        ("created_at", "Created At (ascending)"),
        ("-created_at", "Created At (descending)"),
        ("modified_at", "Modified At (ascending)"),
        ("-modified_at", "Modified At (descending)"),
    ]
    ordering = serializers.ChoiceField(
        required=False,
        choices=ORDERING_CHOICES,
        help_text="Comma-separated list of fields to order by. Use '-' before a field name for descending order.",
    )


class TaskFilterSchema(serializers.Serializer):
    title = serializers.CharField(required=False)
    title__icontains = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    created_at__lte = serializers.DateTimeField(required=False)
    created_at__gte = serializers.DateTimeField(required=False)
    modified_at = serializers.DateTimeField(required=False)
    modified_at__lte = serializers.DateTimeField(required=False)
    modified_at__gte = serializers.DateTimeField(required=False)
    state = serializers.CharField(required=False)
    state__icontains = serializers.CharField(required=False)
    sprint = serializers.IntegerField(required=True)
    ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
    )
    ORDERING_CHOICES: list[tuple[str, str]] = [
        ("title", "Title (ascending)"),
        ("-title", "Title (descending)"),
        ("created_at", "Created At (ascending)"),
        ("-created_at", "Created At (descending)"),
        ("modified_at", "Modified At (ascending)"),
        ("-modified_at", "Modified At (descending)"),
    ]
    ordering = serializers.ChoiceField(
        required=False,
        choices=ORDERING_CHOICES,
        help_text="Comma-separated list of fields to order by. Use '-' before a field name for descending order.",
    )
