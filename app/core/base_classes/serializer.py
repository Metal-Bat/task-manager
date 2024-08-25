from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    """
    Abstract Serializer
    """

    id = serializers.IntegerField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    modified_at = serializers.DateTimeField(read_only=True)

    class Meta:
        abstract = True
        fields = [
            "id",
            "is_active",
            "created_at",
            "modified_at",
        ]


class ResponseSchemaSerializer(serializers.Serializer):
    message = serializers.DictField(read_only=True)
    success = serializers.BooleanField(read_only=True)
    error_code = serializers.IntegerField(read_only=True)
    result = serializers.DictField(read_only=True)


class PaginatedResponseSchemaSerializer(serializers.Serializer):
    count = serializers.IntegerField(read_only=True)
    next = serializers.CharField(allow_null=True, read_only=True)
    previous = serializers.CharField(allow_null=True, read_only=True)
    results = serializers.DictField(read_only=True)
