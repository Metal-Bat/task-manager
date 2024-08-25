from app.core.base_classes.serializer import PaginatedResponseSchemaSerializer, ResponseSchemaSerializer
from app.task.api.serializers import (
    SprintListSerializer,
    SprintRetrieveSerializer,
    TaskInfoSerializer,
    TaskListSerializer,
)


class PaginatedSprintResponseSerializer(PaginatedResponseSchemaSerializer):
    results = SprintListSerializer(many=True)


class SprintDetailResponseSerializer(ResponseSchemaSerializer):
    result = SprintRetrieveSerializer()


class PaginatedTaskResponseSerializer(PaginatedResponseSchemaSerializer):
    results = TaskListSerializer(many=True)


class TaskDetailResponseSerializer(ResponseSchemaSerializer):
    result = TaskInfoSerializer()
