from typing import Any

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from app.core.base_classes.serializer import ResponseSchemaSerializer
from app.core.response_former import paginated_data, response_formatter
from app.core.special_permissions.sprint_permissions import SprintManger, TaskManger
from app.task.api.filters import SprintFilter, TaskFilter
from app.task.api.schema.query_serializer import SprintFilterSchema, TaskFilterSchema
from app.task.api.schema.responses import (
    PaginatedSprintResponseSerializer,
    PaginatedTaskResponseSerializer,
    SprintDetailResponseSerializer,
    TaskDetailResponseSerializer,
)
from app.task.api.serializers import (
    SprintCreateSerializer,
    SprintListSerializer,
    SprintPartialUpdateSerializer,
    SprintRetrieveSerializer,
    SprintUpdateSerializer,
    TaskCreateSerializer,
    TaskInfoSerializer,
    TaskListSerializer,
    TaskPartialUpdateSerializer,
    TaskUpdateSerializer,
)
from app.task.models import Sprint, Task


class SprintViewSet(ViewSet):
    def get_permissions(self) -> list[AllowAny] | list[Any]:
        """mange permission on action **(not the best practice but small one)**"""

        if self.action in ["retrieve", "list"]:
            return [AllowAny()]
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [SprintManger()]
        return super().get_permissions()

    @swagger_auto_schema(
        query_serializer=SprintFilterSchema,
        responses={"200": PaginatedSprintResponseSerializer(many=True)},
    )
    def list(self, request: Request) -> Response:
        """active sprint list **(ACTIVE MEANS NOT ARCHIVED)**"""

        queryset: Sprint = Sprint.active_list.all().order_by("id").cache()
        filterset: SprintFilter = SprintFilter(request.GET, queryset=queryset)

        if filterset.is_valid():
            queryset: Sprint = filterset.qs

        response: Response = paginated_data(request, SprintListSerializer, queryset)
        return response

    @swagger_auto_schema(
        request_body=SprintCreateSerializer,
        responses={
            "200": SprintDetailResponseSerializer(),
            "400": ResponseSchemaSerializer(),
        },
    )
    def create(self, request: Request) -> Response:
        """create sprint"""

        serializer = SprintCreateSerializer(data=request.data)
        if serializer.is_valid():
            sprint: Sprint = serializer.create(serializer.validated_data)
            serializer: SprintRetrieveSerializer = SprintRetrieveSerializer(sprint)
            response: Response = response_formatter(serializer.data)
            return response

        response: Response = response_formatter(
            status=400,
            message=serializer.error_messages,
            error_code=1001,
        )
        return response

    @swagger_auto_schema(
        responses={
            "200": SprintDetailResponseSerializer(),
            "404": ResponseSchemaSerializer(),
        },
    )
    def retrieve(self, request: Request, pk: int = None) -> Response:
        """retrieve information of sprint"""

        queryset: Sprint = get_object_or_404(
            Sprint,
            pk=pk,
            is_active=True,
        )
        serializer: SprintRetrieveSerializer = SprintRetrieveSerializer(queryset)
        response: Response = response_formatter(serializer.data)
        return response

    @swagger_auto_schema(
        request_body=SprintUpdateSerializer,
        responses={
            "200": SprintDetailResponseSerializer(),
            "404": ResponseSchemaSerializer(),
        },
    )
    def update(self, request: Request, pk: int = None) -> Response:
        """update selected queryset"""
        queryset: Sprint = get_object_or_404(
            Sprint,
            pk=pk,
            is_active=True,
        )
        serializer: SprintUpdateSerializer = SprintUpdateSerializer(queryset, data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            serializer: SprintRetrieveSerializer = SprintRetrieveSerializer(queryset)
            response = response_formatter(serializer.data)
            return response

        response: Response = response_formatter(
            status=400,
            message=serializer.error_messages,
            error_code=1001,
        )
        return response

    @swagger_auto_schema(
        request_body=SprintPartialUpdateSerializer,
        responses={
            "200": SprintDetailResponseSerializer(),
            "404": ResponseSchemaSerializer(),
        },
    )
    def partial_update(self, request: Request, pk: int = None) -> Response:
        """partial update selected queryset"""
        queryset: Sprint = get_object_or_404(
            Sprint,
            pk=pk,
            is_active=True,
        )
        serializer: SprintPartialUpdateSerializer = SprintPartialUpdateSerializer(
            queryset,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            queryset = serializer.save()
            serializer: SprintRetrieveSerializer = SprintRetrieveSerializer(queryset)
            response = response_formatter(serializer.data)
            return response

        response: Response = response_formatter(
            status=400,
            message=serializer.error_messages,
            error_code=1001,
        )
        return response

    @swagger_auto_schema(
        responses={
            "200": ResponseSchemaSerializer(),
            "404": ResponseSchemaSerializer(),
        },
    )
    def destroy(self, request: Request, pk: int = None) -> Response:
        queryset: Sprint = get_object_or_404(
            Sprint,
            pk=pk,
            is_active=True,
        )
        queryset.is_active = False
        queryset.save(update_fields=["is_active"])
        response: Response = response_formatter()
        return response


class TaskViewSet(ViewSet):
    def get_permissions(self) -> list[AllowAny] | list[Any]:
        """mange permission on action **(not the best practice but small one)**"""

        if self.action in ["retrieve", "list"]:
            return [AllowAny()]
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [TaskManger()]
        return super().get_permissions()

    @swagger_auto_schema(
        query_serializer=TaskFilterSchema,
        responses={"200": PaginatedTaskResponseSerializer(many=True)},
    )
    def list(self, request: Request) -> Response:
        """active task list **(ACTIVE MEANS NOT ARCHIVED)**"""
        queryset: Task = Task.active_list.all().order_by("id").cache()

        filterset: TaskFilter = TaskFilter(request.GET, queryset=queryset)

        if filterset.is_valid():
            queryset: Task = filterset.qs

        response: Response = paginated_data(request, TaskListSerializer, queryset)
        return response

    @swagger_auto_schema(
        request_body=TaskCreateSerializer,
        responses={
            "200": TaskDetailResponseSerializer(),
            "400": ResponseSchemaSerializer(),
        },
    )
    def create(self, request: Request) -> Response:
        """create task"""

        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            task: Task = serializer.create(serializer.validated_data)
            serializer: TaskInfoSerializer = TaskInfoSerializer(task)
            response: Response = response_formatter(serializer.data)
            return response

        response: Response = response_formatter(
            status=400,
            message=serializer.error_messages,
            error_code=1001,
        )
        return response

    @swagger_auto_schema(
        responses={
            "200": TaskDetailResponseSerializer,
            "404": ResponseSchemaSerializer(),
        }
    )
    def retrieve(self, request: Request, pk=None) -> Response:
        """retrieve information of task"""

        queryset: Task = get_object_or_404(
            Task,
            pk=pk,
            is_active=True,
            sprint__is_active=True,
        )
        serializer = TaskInfoSerializer(queryset)
        response: Response = response_formatter(serializer.data)
        return response

    @swagger_auto_schema(
        request_body=TaskUpdateSerializer,
        responses={
            "200": TaskDetailResponseSerializer(),
            "404": ResponseSchemaSerializer(),
        },
    )
    def update(self, request: Request, pk: int = None) -> Response:
        """update selected queryset"""
        queryset: Task = get_object_or_404(
            Task,
            pk=pk,
            is_active=True,
            sprint__is_active=True,
        )
        serializer: TaskUpdateSerializer = TaskUpdateSerializer(queryset, data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            serializer: TaskInfoSerializer = TaskInfoSerializer(queryset)
            response: Response = response_formatter(serializer.data)
            return response

        response: Response = response_formatter(
            status=400,
            message=serializer.error_messages,
            error_code=1001,
        )
        return response

    @swagger_auto_schema(
        request_body=TaskPartialUpdateSerializer,
        responses={
            "200": TaskDetailResponseSerializer(),
            "404": ResponseSchemaSerializer(),
        },
    )
    def partial_update(self, request: Request, pk: int = None) -> Response:
        """partial update selected queryset"""
        queryset: Task = get_object_or_404(
            Task,
            pk=pk,
            is_active=True,
            sprint__is_active=True,
        )
        serializer: TaskPartialUpdateSerializer = TaskPartialUpdateSerializer(
            queryset,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            queryset = serializer.save()
            serializer: TaskInfoSerializer = TaskInfoSerializer(queryset)
            response: Response = response_formatter(serializer.data)
            return response

        response: Response = response_formatter(
            status=400,
            message=serializer.error_messages,
            error_code=1001,
        )
        return response

    @swagger_auto_schema(
        responses={
            "200": ResponseSchemaSerializer(),
            "404": ResponseSchemaSerializer(),
        },
    )
    def destroy(self, request: Request, pk: int = None) -> Response:
        queryset: Task = get_object_or_404(
            Task,
            pk=pk,
            is_active=True,
            sprint__is_active=True,
        )
        queryset.is_active = False
        queryset.save(update_fields=["is_active"])
        response: Response = response_formatter()
        return response
